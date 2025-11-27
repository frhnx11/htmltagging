#!/usr/bin/env python3
"""
Test script for rule-based classification integration

Tests the integration of rule-based classifier with exam-specific classifier
for Banking questions that start with quantity comparison patterns.
"""

import os
import sys
import logging
from config import get_config

# Setup logging for testing
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)

def test_banking_rule_integration():
    """Test rule-based classification for Banking questions"""
    
    print("="*60)
    print("TESTING BANKING RULE-BASED CLASSIFICATION INTEGRATION")
    print("="*60)
    
    try:
        # Import the classifier
        from exam_specific_classifier import ExamSpecificClassifier
        
        # Get configuration
        config = get_config()
        
        # Create Banking classifier
        classifier = ExamSpecificClassifier("Banking", config)
        
        # Test questions
        test_questions = [
            {
                "question": "In the question, two quantities I and II are given. Quantity I: 25% of 480 Quantity II: 15% of 800. Which is greater?",
                "explanation": "Calculate both quantities and compare them.",
                "expected_rule_match": True,
                "expected_chapter": "Aptitude",
                "expected_topic": "Quantity Comparision",
                "expected_subtopic": "Quantity I & II (All Arithmetic topic)"
            },
            {
                "question": "In the question two quantities I and II are given for comparison. Find which is larger.",
                "explanation": "Simple comparison problem.",
                "expected_rule_match": True,
                "expected_chapter": "Aptitude",
                "expected_topic": "Quantity Comparision",
                "expected_subtopic": "Quantity I & II (All Arithmetic topic)"
            },
            {
                "question": "What is the simple interest on Rs. 5000 at 8% per annum for 3 years?",
                "explanation": "Use SI formula P*R*T/100",
                "expected_rule_match": False,
                "expected_chapter": None,  # Should use AI classification
                "expected_topic": None,
                "expected_subtopic": None
            }
        ]
        
        print(f"Testing {len(test_questions)} questions...")
        print()
        
        results = []
        for i, test_case in enumerate(test_questions, 1):
            print(f"Test {i}: {test_case['question'][:60]}...")
            
            # Classify the question
            result = classifier.classify_question(
                test_case['question'], 
                test_case['explanation']
            )
            
            if result:
                print(f"  ✅ Classification successful:")
                print(f"     Chapter: {result['chapter']}")
                print(f"     Topic: {result['topic']}")
                print(f"     Subtopic: {result['subtopic']}")
                print(f"     Confidence: {result['confidence']:.2f}")
                
                # Verify rule-based expectations
                if test_case['expected_rule_match']:
                    if (result['chapter'] == test_case['expected_chapter'] and
                        result['topic'] == test_case['expected_topic'] and
                        result['subtopic'] == test_case['expected_subtopic']):
                        print(f"  ✅ Rule-based classification MATCHED expected result")
                        results.append("PASS")
                    else:
                        print(f"  ❌ Rule-based classification FAILED - wrong mapping")
                        results.append("FAIL")
                else:
                    print(f"  ✅ Non-rule question processed (likely AI classified)")
                    results.append("PASS")
            else:
                print(f"  ❌ Classification failed")
                results.append("FAIL")
            
            print()
        
        # Show classifier statistics
        stats = classifier.stats
        print("CLASSIFIER STATISTICS:")
        print("-"*40)
        print(f"Total classifications: {stats['total_classifications']}")
        print(f"Successful: {stats['successful_classifications']}")
        print(f"Failed: {stats['failed_classifications']}")
        print(f"Rule-based matches: {stats['rule_based_matches']}")
        print(f"OpenAI requests: {stats['openai_requests']}")
        print(f"Cost savings (USD): ${stats['cost_savings_usd']:.6f}")
        print(f"Average response time: {stats['average_response_time']:.3f}s")
        
        # Show rule classifier statistics if available
        if classifier.rule_classifier:
            rule_stats = classifier.rule_classifier.get_statistics()
            print("\nRULE CLASSIFIER STATISTICS:")
            print("-"*40)
            print(f"Total checks: {rule_stats['total_checks']}")
            print(f"Rule matches: {rule_stats['rule_matches']}")
            print(f"Match rate: {rule_stats['match_rate']:.2%}")
            print(f"Cost savings: ${rule_stats['cost_savings']:.6f}")
        
        # Summary
        passed = results.count("PASS")
        failed = results.count("FAIL")
        print(f"\nTEST SUMMARY:")
        print(f"PASSED: {passed}/{len(test_questions)}")
        print(f"FAILED: {failed}/{len(test_questions)}")
        
        if failed == 0:
            print("🎉 ALL TESTS PASSED!")
        else:
            print("❌ Some tests failed")
            
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure all dependencies are available")
    except Exception as e:
        print(f"❌ Test error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_banking_rule_integration()