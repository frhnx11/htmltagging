#!/usr/bin/env python3
"""
Rule-Based Question Classifier

Provides pattern-based classification for questions that follow specific formats.
This bypasses AI classification for known patterns, improving accuracy and reducing costs.
"""

import re
import logging
from typing import Dict, Optional, List, Tuple
from dataclasses import dataclass


@dataclass
class ClassificationRule:
    """Represents a classification rule"""
    pattern: str
    exam_type: str
    chapter: str
    topic: str
    subtopic: str
    description: str
    case_sensitive: bool = False


@dataclass
class RuleMatchResult:
    """Result of applying a classification rule"""
    matched: bool
    rule: Optional[ClassificationRule] = None
    confidence: float = 1.0
    reasoning: str = ""


class RuleBasedClassifier:
    """
    Pattern-based classifier for questions with known structures
    
    Applies predefined rules to classify questions without AI inference,
    providing 100% accuracy for matching patterns and cost savings.
    """
    
    def __init__(self, rules: List[ClassificationRule]):
        """
        Initialize rule-based classifier
        
        Args:
            rules: List of classification rules to apply
        """
        self.rules = rules
        self.logger = logging.getLogger(__name__)
        
        # Statistics
        self.stats = {
            'total_checks': 0,
            'rule_matches': 0,
            'matches_by_rule': {},
            'matches_by_exam': {}
        }
        
        self.logger.info(f"Rule-based classifier initialized with {len(rules)} rules")
    
    def classify_question(self, question: str, exam_type: str) -> RuleMatchResult:
        """
        Attempt to classify a question using predefined rules
        
        Args:
            question: Question text to classify
            exam_type: Exam type (TNPSC, Banking, SSC-Railways)
            
        Returns:
            RuleMatchResult indicating if a rule matched and the classification
        """
        self.stats['total_checks'] += 1
        
        # Clean question text
        question_clean = question.strip() if question else ""
        
        # Try each rule for the specific exam type
        for rule in self.rules:
            if rule.exam_type.upper() != exam_type.upper():
                continue
                
            if self._matches_pattern(question_clean, rule):
                # Rule matched
                self.stats['rule_matches'] += 1
                self._update_match_stats(rule, exam_type)
                
                self.logger.info(f"Rule matched for {exam_type}: {rule.description}")
                
                return RuleMatchResult(
                    matched=True,
                    rule=rule,
                    confidence=1.0,
                    reasoning=f"Matched rule: {rule.description}"
                )
        
        # No rules matched
        return RuleMatchResult(
            matched=False,
            reasoning="No matching rules found"
        )
    
    def _matches_pattern(self, question: str, rule: ClassificationRule) -> bool:
        """
        Check if question matches the rule pattern
        
        Args:
            question: Question text
            rule: Rule to check
            
        Returns:
            True if pattern matches
        """
        if not question:
            return False
            
        # Prepare pattern for matching
        pattern = rule.pattern
        flags = 0 if rule.case_sensitive else re.IGNORECASE
        
        # Check if pattern is at the start of question
        try:
            return bool(re.match(pattern, question, flags))
        except re.error as e:
            self.logger.error(f"Invalid regex pattern '{pattern}': {e}")
            return False
    
    def _update_match_stats(self, rule: ClassificationRule, exam_type: str):
        """Update statistics for rule matches"""
        rule_key = f"{rule.exam_type}_{rule.description}"
        self.stats['matches_by_rule'][rule_key] = self.stats['matches_by_rule'].get(rule_key, 0) + 1
        self.stats['matches_by_exam'][exam_type] = self.stats['matches_by_exam'].get(exam_type, 0) + 1
    
    def get_statistics(self) -> Dict:
        """Get classifier statistics"""
        total_checks = self.stats['total_checks']
        rule_matches = self.stats['rule_matches']
        
        return {
            'total_checks': total_checks,
            'rule_matches': rule_matches,
            'match_rate': rule_matches / total_checks if total_checks > 0 else 0,
            'cost_savings': rule_matches * 0.000054,  # Approximate cost per question
            'matches_by_rule': self.stats['matches_by_rule'],
            'matches_by_exam': self.stats['matches_by_exam']
        }
    
    def add_rule(self, rule: ClassificationRule):
        """Add a new classification rule"""
        self.rules.append(rule)
        self.logger.info(f"Added new rule: {rule.description}")
    
    def get_rules_for_exam(self, exam_type: str) -> List[ClassificationRule]:
        """Get all rules for a specific exam type"""
        return [rule for rule in self.rules if rule.exam_type.upper() == exam_type.upper()]


def create_default_rules() -> List[ClassificationRule]:
    """
    Create default classification rules
    
    Returns:
        List of predefined classification rules
    """
    rules = []
    
    # Banking: Quantity Comparison Questions
    rules.append(ClassificationRule(
        pattern=r"^In the question,?\s*two\s+quantities?\s+I\s+and\s+II\s+are\s+given",
        exam_type="Banking",
        chapter="Aptitude",
        topic="Quantity Comparision",  # Note: Keep original spelling from taxonomy
        subtopic="Quantity I & II (All Arithmetic topic)",
        description="Quantity comparison questions with quantities I and II",
        case_sensitive=False
    ))
    
    # Additional patterns can be added here for other exam types
    # Example for future expansion:
    # rules.append(ClassificationRule(
    #     pattern=r"^If\s+.*?\s+then\s+what\s+is\s+the\s+value",
    #     exam_type="TNPSC",
    #     chapter="Aptitude",
    #     topic="Problem Solving",
    #     subtopic="Value Calculation",
    #     description="Value calculation problems"
    # ))
    
    return rules


def get_classification_dict(rule: ClassificationRule) -> Dict[str, str]:
    """
    Convert rule to classification dictionary format
    
    Args:
        rule: Classification rule
        
    Returns:
        Dictionary with chapter, topic, subtopic
    """
    return {
        'chapter': rule.chapter,
        'topic': rule.topic,
        'subtopic': rule.subtopic
    }


if __name__ == "__main__":
    # Test the rule-based classifier
    logging.basicConfig(level=logging.INFO)
    
    # Create classifier with default rules
    rules = create_default_rules()
    classifier = RuleBasedClassifier(rules)
    
    # Test cases
    test_questions = [
        ("In the question, two quantities I and II are given. Quantity I: 25% of 480 Quantity II: 15% of 800", "Banking"),
        ("In the question two quantities I and II are given", "Banking"),
        ("What is the capital of India?", "Banking"),
        ("Calculate the compound interest", "TNPSC")
    ]
    
    print("Testing Rule-Based Classifier:")
    print("=" * 50)
    
    for question, exam_type in test_questions:
        result = classifier.classify_question(question, exam_type)
        print(f"\nQuestion: {question[:60]}...")
        print(f"Exam Type: {exam_type}")
        print(f"Matched: {result.matched}")
        
        if result.matched:
            print(f"Chapter: {result.rule.chapter}")
            print(f"Topic: {result.rule.topic}")
            print(f"Subtopic: {result.rule.subtopic}")
            print(f"Confidence: {result.confidence}")
        
        print(f"Reasoning: {result.reasoning}")
    
    # Show statistics
    print("\n" + "=" * 50)
    print("Classifier Statistics:")
    stats = classifier.get_statistics()
    for key, value in stats.items():
        print(f"{key}: {value}")