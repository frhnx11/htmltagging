#!/usr/bin/env python3
"""
OpenAI Client - Handle interactions with OpenAI API for question classification

Provides a robust interface to OpenAI's GPT-4o mini API with cost tracking,
error handling, and fallback capabilities.
"""

import json
import logging
import time
import os
from typing import Dict, Optional, List, Tuple
from datetime import datetime
import requests

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    OpenAI = None

from cost_tracker import CostTracker

class OpenAIClient:
    """
    OpenAI API client for question classification
    
    Features:
    - GPT-4o mini integration
    - Cost tracking and budget management
    - Rate limiting and error handling
    - Automatic retries and fallback
    - Token usage optimization
    """
    
    def __init__(self, config: Dict, cost_tracker: Optional[CostTracker] = None):
        """
        Initialize OpenAI client
        
        Args:
            config: Configuration dictionary with OpenAI settings
            cost_tracker: Optional cost tracker instance
        """
        self.config = config
        self.openai_config = config.get("openai", {})
        self.cost_tracker = cost_tracker or CostTracker()
        
        # Setup logging
        self.logger = logging.getLogger(__name__)
        
        # Check if OpenAI library is available
        if not OPENAI_AVAILABLE:
            self.logger.error("OpenAI library not installed. Install with: pip install openai")
            raise ImportError("OpenAI library required for OpenAI client")
        
        # Initialize OpenAI client
        api_key = self.get_api_key()
        if not api_key:
            raise ValueError("OpenAI API key not found. Set OPENAI_API_KEY environment variable")
        
        self.client = OpenAI(api_key=api_key)
        
        # Configuration
        self.model = self.openai_config.get("model", "gpt-4o-mini")
        self.max_tokens = self.openai_config.get("max_tokens", 150)
        self.temperature = self.openai_config.get("temperature", 0.02)
        self.max_retries = self.openai_config.get("max_retries", 3)
        self.retry_delay = self.openai_config.get("retry_delay", 2)
        self.timeout = self.openai_config.get("timeout", 30)
        
        # Statistics
        self.stats = {
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "total_input_tokens": 0,
            "total_output_tokens": 0,
            "average_response_time": 0,
            "rate_limit_hits": 0,
            "quota_exhausted": False,
            "last_request_time": 0
        }
        
        # Rate limiting
        self.rate_limit = {
            "requests_per_minute": self.openai_config.get("requests_per_minute", 100),
            "tokens_per_minute": self.openai_config.get("tokens_per_minute", 100000),
            "last_reset": time.time(),
            "requests_this_minute": 0,
            "tokens_this_minute": 0
        }
        
        self.logger.info(f"OpenAI client initialized with model: {self.model}")
        
    def get_api_key(self) -> Optional[str]:
        """
        Get OpenAI API key from environment or config
        
        Returns:
            API key or None if not found
        """
        # Try environment variable first
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            return api_key
        
        # Try config file
        api_key = self.openai_config.get("api_key")
        if api_key and not api_key.startswith("sk-"):
            self.logger.warning("API key in config doesn't look valid (should start with 'sk-')")
        
        return api_key
    
    def check_rate_limits(self, estimated_tokens: int = 0) -> bool:
        """
        Check if request would exceed rate limits
        
        Args:
            estimated_tokens: Estimated tokens for the request
        
        Returns:
            True if request can proceed, False if rate limited
        """
        now = time.time()
        
        # Reset counters if a minute has passed
        if now - self.rate_limit["last_reset"] >= 60:
            self.rate_limit["requests_this_minute"] = 0
            self.rate_limit["tokens_this_minute"] = 0
            self.rate_limit["last_reset"] = now
        
        # Check limits
        if (self.rate_limit["requests_this_minute"] >= self.rate_limit["requests_per_minute"] or
            self.rate_limit["tokens_this_minute"] + estimated_tokens >= self.rate_limit["tokens_per_minute"]):
            return False
        
        return True
    
    def wait_for_rate_limit(self, estimated_tokens: int = 0):
        """
        Wait if rate limit would be exceeded
        
        Args:
            estimated_tokens: Estimated tokens for the request
        """
        while not self.check_rate_limits(estimated_tokens):
            wait_time = 60 - (time.time() - self.rate_limit["last_reset"])
            if wait_time > 0:
                self.logger.info(f"Rate limit reached, waiting {wait_time:.1f}s")
                time.sleep(min(wait_time + 1, 10))  # Wait with max 10s chunks
            else:
                break
    
    def estimate_tokens(self, text: str) -> int:
        """
        Estimate token count for text (rough approximation)
        
        Args:
            text: Text to estimate
        
        Returns:
            Estimated token count
        """
        # Rough approximation: ~4 characters per token
        return len(text) // 4 + 50  # Add buffer for safety
    
    def make_request(self, prompt: str, question: str = "", operation: str = "") -> Optional[str]:
        """
        Make a request to OpenAI API
        
        Args:
            prompt: The prompt to send
            question: Question being classified (for logging)
            operation: Operation type (for cost tracking)
        
        Returns:
            Response text or None if failed
        """
        if self.stats["quota_exhausted"]:
            self.logger.error("API quota exhausted, cannot make request")
            return None
        
        # Check budget
        if not self.cost_tracker.can_afford_questions(1):
            self.logger.error("Budget exhausted, cannot make request")
            return None
        
        start_time = time.time()
        estimated_tokens = self.estimate_tokens(prompt)
        
        # Wait for rate limits
        self.wait_for_rate_limit(estimated_tokens)
        
        # Try the request with retries
        for attempt in range(self.max_retries):
            try:
                self.logger.debug(f"Making OpenAI request (attempt {attempt + 1}/{self.max_retries})")
                
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an expert educational content classifier. Follow instructions precisely and return only valid JSON responses."
                        },
                        {
                            "role": "user", 
                            "content": prompt
                        }
                    ],
                    max_tokens=self.max_tokens,
                    temperature=self.temperature,
                    timeout=self.timeout
                )
                
                # Extract response
                if response.choices and response.choices[0].message:
                    response_text = response.choices[0].message.content
                    
                    # Track token usage
                    input_tokens = response.usage.prompt_tokens
                    output_tokens = response.usage.completion_tokens
                    
                    # Record cost
                    self.cost_tracker.record_usage(
                        model=self.model,
                        input_tokens=input_tokens,
                        output_tokens=output_tokens,
                        question_id=question[:50] if question else None,
                        operation=operation
                    )
                    
                    # Update stats
                    self.stats["total_requests"] += 1
                    self.stats["successful_requests"] += 1
                    self.stats["total_input_tokens"] += input_tokens
                    self.stats["total_output_tokens"] += output_tokens
                    
                    # Update rate limit counters
                    self.rate_limit["requests_this_minute"] += 1
                    self.rate_limit["tokens_this_minute"] += input_tokens + output_tokens
                    
                    # Update response time
                    response_time = time.time() - start_time
                    self.stats["average_response_time"] = (
                        (self.stats["average_response_time"] * (self.stats["successful_requests"] - 1) + response_time) /
                        self.stats["successful_requests"]
                    )
                    
                    self.logger.debug(f"OpenAI request successful: {input_tokens}+{output_tokens} tokens, "
                                    f"{response_time:.2f}s")
                    
                    return response_text
                else:
                    self.logger.error("Empty response from OpenAI")
                    
            except Exception as e:
                error_msg = str(e).lower()
                
                # Handle different types of errors
                if "rate_limit" in error_msg or "rate limit" in error_msg:
                    self.stats["rate_limit_hits"] += 1
                    wait_time = min(60, (attempt + 1) * self.retry_delay)
                    self.logger.warning(f"Rate limit hit, waiting {wait_time}s before retry")
                    time.sleep(wait_time)
                    continue
                    
                elif "quota" in error_msg or "billing" in error_msg:
                    self.stats["quota_exhausted"] = True
                    self.logger.error(f"API quota exhausted: {e}")
                    break
                    
                elif "timeout" in error_msg:
                    self.logger.warning(f"Request timeout (attempt {attempt + 1}): {e}")
                    if attempt < self.max_retries - 1:
                        time.sleep(self.retry_delay * (attempt + 1))
                        continue
                        
                elif "connection" in error_msg or "network" in error_msg:
                    self.logger.warning(f"Connection error (attempt {attempt + 1}): {e}")
                    if attempt < self.max_retries - 1:
                        time.sleep(self.retry_delay * (attempt + 1))
                        continue
                        
                else:
                    self.logger.error(f"OpenAI API error: {e}")
                    break
        
        # All attempts failed
        self.stats["failed_requests"] += 1
        self.stats["total_requests"] += 1
        
        self.logger.error(f"OpenAI request failed after {self.max_retries} attempts")
        return None
    
    def test_connection(self) -> bool:
        """
        Test connection to OpenAI API
        
        Returns:
            True if connection successful, False otherwise
        """
        try:
            test_prompt = "Respond with exactly: 'Test successful'"
            response = self.make_request(test_prompt, operation="connection_test")
            
            if response and "test successful" in response.lower():
                self.logger.info("OpenAI API connection test successful")
                return True
            else:
                self.logger.warning(f"OpenAI API test unexpected response: {response}")
                return False
                
        except Exception as e:
            self.logger.error(f"OpenAI API connection test failed: {e}")
            return False
    
    def get_stats(self) -> Dict:
        """
        Get current statistics
        
        Returns:
            Dictionary of statistics
        """
        total_tokens = self.stats["total_input_tokens"] + self.stats["total_output_tokens"]
        
        return {
            **self.stats,
            "total_tokens": total_tokens,
            "success_rate": (
                self.stats["successful_requests"] / max(1, self.stats["total_requests"]) * 100
            ),
            "average_tokens_per_request": (
                total_tokens / max(1, self.stats["successful_requests"])
            ),
            "model": self.model,
            "quota_exhausted": self.stats["quota_exhausted"]
        }
    
    def get_cost_summary(self) -> str:
        """
        Get cost summary from cost tracker
        
        Returns:
            Formatted cost summary
        """
        return self.cost_tracker.generate_cost_report()
    
    def can_continue(self) -> bool:
        """
        Check if client can continue making requests
        
        Returns:
            True if can continue, False if should stop
        """
        return (
            not self.stats["quota_exhausted"] and
            self.cost_tracker.can_afford_questions(1)
        )

def create_openai_client(config: Dict, budget_usd: float = 10.0) -> Optional[OpenAIClient]:
    """
    Create OpenAI client with error handling
    
    Args:
        config: Configuration dictionary
        budget_usd: Budget limit in USD
    
    Returns:
        OpenAIClient instance or None if creation failed
    """
    try:
        cost_tracker = CostTracker(budget_limit_usd=budget_usd)
        client = OpenAIClient(config, cost_tracker)
        
        # Test connection
        if client.test_connection():
            return client
        else:
            logging.error("OpenAI client connection test failed")
            return None
            
    except Exception as e:
        logging.error(f"Failed to create OpenAI client: {e}")
        return None

# Module testing
if __name__ == "__main__":
    print("🧪 OPENAI CLIENT TESTING")
    print("=" * 40)
    
    # Test configuration
    test_config = {
        "openai": {
            "model": "gpt-4o-mini",
            "max_tokens": 100,
            "temperature": 0.02,
            "max_retries": 2
        }
    }
    
    try:
        # Create client
        print("🔧 Creating OpenAI client...")
        client = create_openai_client(test_config, budget_usd=1.0)
        
        if client:
            print("✅ Client created successfully")
            
            # Test simple request
            print("\n📝 Testing simple request...")
            response = client.make_request(
                "Respond with exactly: 'Hello from GPT-4o mini'",
                operation="test"
            )
            
            if response:
                print(f"✅ Response: {response}")
            else:
                print("❌ No response received")
            
            # Show stats
            print(f"\n📊 Client Stats:")
            stats = client.get_stats()
            for key, value in stats.items():
                print(f"  {key}: {value}")
            
            # Show cost summary
            print(f"\n💰 Cost Summary:")
            print(client.get_cost_summary())
            
        else:
            print("❌ Failed to create client")
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
    
    print("\n✅ OpenAI client testing completed!")