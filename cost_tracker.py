#!/usr/bin/env python3
"""
Cost Tracker - Monitor and track OpenAI API usage costs

Provides detailed tracking of token usage, costs in USD and INR,
and budget management for the question classification system.
"""

import json
import logging
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
import requests

@dataclass
class UsageRecord:
    """Record of a single API usage"""
    timestamp: str
    model: str
    input_tokens: int
    output_tokens: int
    cost_usd: float
    cost_inr: float
    question_id: Optional[str] = None
    operation: Optional[str] = None  # "subject_detection" or "triplet_selection"

@dataclass
class CostSummary:
    """Summary of costs and usage"""
    total_requests: int
    total_input_tokens: int
    total_output_tokens: int
    total_cost_usd: float
    total_cost_inr: float
    average_cost_per_request_usd: float
    average_cost_per_request_inr: float
    start_time: str
    end_time: str

class CostTracker:
    """
    Track OpenAI API usage costs and token consumption
    
    Features:
    - Real-time cost tracking
    - Budget alerts
    - Usage analytics
    - Cost optimization suggestions
    """
    
    def __init__(self, budget_limit_usd: float = 10.0, cost_file: str = "logs/api_costs.json"):
        """
        Initialize cost tracker

        Args:
            budget_limit_usd: Maximum budget in USD
            cost_file: File to store cost tracking data
        """
        self.budget_limit_usd = budget_limit_usd
        self.cost_file = cost_file
        self.logger = logging.getLogger(__name__)
        
        # Current session stats
        self.session_stats = {
            'requests': 0,
            'input_tokens': 0,
            'output_tokens': 0,
            'cost_usd': 0.0,
            'cost_inr': 0.0,
            'start_time': datetime.now().isoformat()
        }
        
        # Pricing for GPT-4o mini (per million tokens)
        self.pricing = {
            'gpt-4o-mini': {
                'input': 0.15,   # $0.15 per 1M tokens
                'output': 0.60   # $0.60 per 1M tokens
            },
            'gpt-4o': {
                'input': 5.00,   # $5.00 per 1M tokens
                'output': 20.00  # $20.00 per 1M tokens
            }
        }
        
        # Exchange rate (will be updated from API)
        self.usd_to_inr_rate = 85.79  # Default fallback rate
        
        # Load existing data
        self.usage_records: List[UsageRecord] = []
        self.load_cost_data()
        
        # Update exchange rate
        self.update_exchange_rate()

        # Ensure logs directory exists
        os.makedirs('logs', exist_ok=True)
        os.makedirs(os.path.dirname(self.cost_file), exist_ok=True)
    
    def update_exchange_rate(self) -> bool:
        """
        Update USD to INR exchange rate from API
        
        Returns:
            True if update successful, False otherwise
        """
        try:
            # Try to get current exchange rate
            response = requests.get(
                "https://api.exchangerate-api.com/v4/latest/USD",
                timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                if 'rates' in data and 'INR' in data['rates']:
                    self.usd_to_inr_rate = data['rates']['INR']
                    self.logger.info(f"Updated exchange rate: 1 USD = {self.usd_to_inr_rate:.2f} INR")
                    return True
        except Exception as e:
            self.logger.warning(f"Failed to update exchange rate: {e}")
        
        self.logger.info(f"Using fallback exchange rate: 1 USD = {self.usd_to_inr_rate:.2f} INR")
        return False
    
    def calculate_cost(self, model: str, input_tokens: int, output_tokens: int) -> Tuple[float, float]:
        """
        Calculate cost for token usage
        
        Args:
            model: Model name (e.g., 'gpt-4o-mini')
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
        
        Returns:
            Tuple of (cost_usd, cost_inr)
        """
        if model not in self.pricing:
            self.logger.warning(f"Unknown model for pricing: {model}")
            model = 'gpt-4o-mini'  # Default to most cost-effective
        
        pricing = self.pricing[model]
        
        # Calculate cost in USD (pricing is per million tokens)
        input_cost_usd = (input_tokens / 1_000_000) * pricing['input']
        output_cost_usd = (output_tokens / 1_000_000) * pricing['output']
        total_cost_usd = input_cost_usd + output_cost_usd
        
        # Convert to INR
        total_cost_inr = total_cost_usd * self.usd_to_inr_rate
        
        return total_cost_usd, total_cost_inr
    
    def record_usage(self, model: str, input_tokens: int, output_tokens: int, 
                    question_id: Optional[str] = None, operation: Optional[str] = None) -> UsageRecord:
        """
        Record API usage and calculate costs
        
        Args:
            model: Model used
            input_tokens: Input tokens consumed
            output_tokens: Output tokens generated
            question_id: Optional question identifier
            operation: Optional operation type
        
        Returns:
            UsageRecord with cost information
        """
        # Calculate costs
        cost_usd, cost_inr = self.calculate_cost(model, input_tokens, output_tokens)
        
        # Create usage record
        record = UsageRecord(
            timestamp=datetime.now().isoformat(),
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cost_usd=cost_usd,
            cost_inr=cost_inr,
            question_id=question_id,
            operation=operation
        )
        
        # Add to records
        self.usage_records.append(record)
        
        # Update session stats
        self.session_stats['requests'] += 1
        self.session_stats['input_tokens'] += input_tokens
        self.session_stats['output_tokens'] += output_tokens
        self.session_stats['cost_usd'] += cost_usd
        self.session_stats['cost_inr'] += cost_inr
        
        # Save to file
        self.save_cost_data()
        
        # Check budget
        self.check_budget_alert()
        
        self.logger.info(f"API usage recorded: {input_tokens}+{output_tokens} tokens, "
                        f"${cost_usd:.4f} (Rs.{cost_inr:.2f})")
        
        return record
    
    def check_budget_alert(self) -> bool:
        """
        Check if budget threshold reached
        
        Returns:
            True if budget alert should be triggered
        """
        total_cost = self.get_total_cost_usd()
        
        if total_cost >= self.budget_limit_usd:
            self.logger.error(f"BUDGET EXCEEDED! Total cost: ${total_cost:.2f} "
                            f"(Limit: ${self.budget_limit_usd:.2f})")
            return True
        elif total_cost >= self.budget_limit_usd * 0.8:
            self.logger.warning(f"Budget alert: ${total_cost:.2f} of ${self.budget_limit_usd:.2f} used "
                              f"({total_cost/self.budget_limit_usd*100:.1f}%)")
            return True
        
        return False
    
    def get_total_cost_usd(self) -> float:
        """Get total cost in USD across all records"""
        return sum(record.cost_usd for record in self.usage_records)
    
    def get_total_cost_inr(self) -> float:
        """Get total cost in INR across all records"""
        return sum(record.cost_inr for record in self.usage_records)
    
    def get_session_summary(self) -> Dict:
        """Get current session summary"""
        return {
            **self.session_stats,
            'end_time': datetime.now().isoformat(),
            'avg_tokens_per_request': (
                (self.session_stats['input_tokens'] + self.session_stats['output_tokens']) / 
                max(1, self.session_stats['requests'])
            ),
            'budget_used_percentage': (self.get_total_cost_usd() / self.budget_limit_usd) * 100,
            'remaining_budget_usd': self.budget_limit_usd - self.get_total_cost_usd()
        }
    
    def get_cost_summary(self, days_back: int = 7) -> CostSummary:
        """
        Get cost summary for specified period
        
        Args:
            days_back: Number of days to include in summary
        
        Returns:
            CostSummary object
        """
        cutoff_date = datetime.now() - timedelta(days=days_back)
        
        # Filter records within period
        recent_records = [
            record for record in self.usage_records
            if datetime.fromisoformat(record.timestamp) >= cutoff_date
        ]
        
        if not recent_records:
            return CostSummary(0, 0, 0, 0.0, 0.0, 0.0, 0.0, "", "")
        
        total_input_tokens = sum(r.input_tokens for r in recent_records)
        total_output_tokens = sum(r.output_tokens for r in recent_records)
        total_cost_usd = sum(r.cost_usd for r in recent_records)
        total_cost_inr = sum(r.cost_inr for r in recent_records)
        
        return CostSummary(
            total_requests=len(recent_records),
            total_input_tokens=total_input_tokens,
            total_output_tokens=total_output_tokens,
            total_cost_usd=total_cost_usd,
            total_cost_inr=total_cost_inr,
            average_cost_per_request_usd=total_cost_usd / len(recent_records),
            average_cost_per_request_inr=total_cost_inr / len(recent_records),
            start_time=min(r.timestamp for r in recent_records),
            end_time=max(r.timestamp for r in recent_records)
        )
    
    def generate_cost_report(self) -> str:
        """
        Generate detailed cost report
        
        Returns:
            Formatted cost report string
        """
        session = self.get_session_summary()
        weekly = self.get_cost_summary(7)
        monthly = self.get_cost_summary(30)
        
        report_lines = []
        report_lines.append("💰 OPENAI API COST REPORT")
        report_lines.append("=" * 50)
        
        # Current session
        report_lines.append("\n📊 Current Session:")
        report_lines.append(f"  Requests: {session['requests']}")
        report_lines.append(f"  Total tokens: {session['input_tokens'] + session['output_tokens']:,}")
        report_lines.append(f"  Input tokens: {session['input_tokens']:,}")
        report_lines.append(f"  Output tokens: {session['output_tokens']:,}")
        report_lines.append(f"  Cost: ${session['cost_usd']:.4f} (₹{session['cost_inr']:.2f})")
        
        # Weekly summary
        if weekly.total_requests > 0:
            report_lines.append("\n📅 Last 7 Days:")
            report_lines.append(f"  Requests: {weekly.total_requests}")
            report_lines.append(f"  Total tokens: {weekly.total_input_tokens + weekly.total_output_tokens:,}")
            report_lines.append(f"  Cost: ${weekly.total_cost_usd:.4f} (₹{weekly.total_cost_inr:.2f})")
            report_lines.append(f"  Avg per request: ${weekly.average_cost_per_request_usd:.4f}")
        
        # Budget status
        total_cost = self.get_total_cost_usd()
        budget_used = (total_cost / self.budget_limit_usd) * 100
        report_lines.append(f"\n💳 Budget Status:")
        report_lines.append(f"  Used: ${total_cost:.4f} of ${self.budget_limit_usd:.2f} ({budget_used:.1f}%)")
        report_lines.append(f"  Remaining: ${self.budget_limit_usd - total_cost:.4f}")
        
        # Cost optimization suggestions
        if session['requests'] > 10:
            avg_tokens = session['avg_tokens_per_request']
            report_lines.append(f"\n💡 Optimization Suggestions:")
            if avg_tokens > 4000:
                report_lines.append("  - Consider reducing prompt length to save costs")
            if session['cost_usd'] / session['requests'] > 0.005:
                report_lines.append("  - Consider using batch processing for better rates")
            if budget_used > 80:
                report_lines.append("  - Consider switching to Ollama fallback to save costs")
        
        return "\n".join(report_lines)
    
    def save_cost_data(self):
        """Save cost tracking data to file"""
        try:
            data = {
                'budget_limit_usd': self.budget_limit_usd,
                'usd_to_inr_rate': self.usd_to_inr_rate,
                'usage_records': [asdict(record) for record in self.usage_records],
                'session_stats': self.session_stats,
                'last_updated': datetime.now().isoformat()
            }
            
            with open(self.cost_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.logger.error(f"Failed to save cost data: {e}")
    
    def load_cost_data(self):
        """Load cost tracking data from file"""
        try:
            if os.path.exists(self.cost_file):
                with open(self.cost_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Load usage records
                if 'usage_records' in data:
                    self.usage_records = [
                        UsageRecord(**record) for record in data['usage_records']
                    ]
                
                # Load other settings
                if 'budget_limit_usd' in data:
                    self.budget_limit_usd = data['budget_limit_usd']
                if 'usd_to_inr_rate' in data:
                    self.usd_to_inr_rate = data['usd_to_inr_rate']
                
                self.logger.info(f"Loaded {len(self.usage_records)} usage records")
                
        except Exception as e:
            self.logger.warning(f"Failed to load cost data: {e}")
    
    def estimate_cost_for_questions(self, num_questions: int, model: str = 'gpt-4o-mini') -> Tuple[float, float]:
        """
        Estimate cost for processing a number of questions
        
        Args:
            num_questions: Number of questions to process
            model: Model to use for estimation
        
        Returns:
            Tuple of (estimated_cost_usd, estimated_cost_inr)
        """
        # Estimate tokens per question based on our prompts
        # Stage 1: ~950 input + 50 output tokens
        # Stage 2: ~2700 input + 80 output tokens
        estimated_input_tokens = num_questions * (950 + 2700)  # 3650 per question
        estimated_output_tokens = num_questions * (50 + 80)    # 130 per question
        
        cost_usd, cost_inr = self.calculate_cost(model, estimated_input_tokens, estimated_output_tokens)
        
        return cost_usd, cost_inr
    
    def can_afford_questions(self, num_questions: int, model: str = 'gpt-4o-mini') -> bool:
        """
        Check if we can afford to process the given number of questions
        
        Args:
            num_questions: Number of questions to process
            model: Model to use for cost calculation
        
        Returns:
            True if within budget, False otherwise
        """
        estimated_cost, _ = self.estimate_cost_for_questions(num_questions, model)
        current_cost = self.get_total_cost_usd()
        
        return (current_cost + estimated_cost) <= self.budget_limit_usd

# Convenience functions
def create_cost_tracker(budget_usd: float = 10.0) -> CostTracker:
    """Create a cost tracker with specified budget"""
    return CostTracker(budget_limit_usd=budget_usd)

def estimate_classification_cost(num_questions: int) -> str:
    """Quick cost estimation for question classification"""
    tracker = CostTracker()
    cost_usd, cost_inr = tracker.estimate_cost_for_questions(num_questions)
    
    return f"Estimated cost for {num_questions} questions: ${cost_usd:.4f} (₹{cost_inr:.2f})"

# Module testing
if __name__ == "__main__":
    print("🧪 COST TRACKER TESTING")
    print("=" * 40)
    
    # Create test tracker
    tracker = CostTracker(budget_limit_usd=5.0)
    
    # Test cost calculation
    print("📊 Cost Calculation Test:")
    cost_usd, cost_inr = tracker.calculate_cost('gpt-4o-mini', 1000, 100)
    print(f"1000 input + 100 output tokens: ${cost_usd:.6f} (₹{cost_inr:.4f})")
    
    # Test usage recording
    print("\n📝 Usage Recording Test:")
    record = tracker.record_usage('gpt-4o-mini', 950, 50, "test_q1", "subject_detection")
    print(f"Recorded: ${record.cost_usd:.6f} (₹{record.cost_inr:.4f})")
    
    # Test cost estimation
    print("\n💰 Cost Estimation Test:")
    print(estimate_classification_cost(100))
    print(estimate_classification_cost(1000))
    
    # Test budget check
    print(f"\n💳 Budget Check:")
    print(f"Can afford 1000 questions: {tracker.can_afford_questions(1000)}")
    
    print("\n✅ Cost tracker testing completed!")