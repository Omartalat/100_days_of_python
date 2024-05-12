#!/usr/bin/python3
"""
This script runs a quiz game using a set of predefined questions and answers.
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBank

question_bank = []

for question in question_data:
    text = question['question']
    answer = question['correct_answer']
    question_bank.append(Question(text, answer))

quiz = QuizBank(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
