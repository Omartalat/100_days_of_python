#!/usr/bin/python3
"""
This module contains the QuizBank class which represents a quiz bank.

Attributes:
- question_number (int): The current question number.
- score (int): The current score.
- question_list (list): A list of Question objects representing the quiz questions.

Methods:
- still_has_questions(): Checks if there are still questions remaining in the quiz.
- next_question(): Displays the next question and prompts the user for an answer.
- check_answer(user_answer, correct_answer): Checks if the user's answer is correct and updates the score accordingly.
"""


class QuizBank:
    """
    A class representing a quiz bank.
    """

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        """
        Checks if there are still questions remaining in the quiz.

        Returns:
        - bool: True if there are still questions remaining, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Displays the next question and prompts the user for an answer.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)? ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        Checks if the user's answer is correct and updates the score accordingly.

        Parameters:
        - user_answer (str): The user's answer.
        - correct_answer (str): The correct answer.

        Prints:
        - "You got it right!" if the user's answer is correct.
        - "That's wrong!" if the user's answer is incorrect.
        - The correct answer.
        - The current score.
        """
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The right answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")
