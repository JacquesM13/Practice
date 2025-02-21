from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_bank.append(Question(text=question_text, answer=question_answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    user_answer = quiz.next_question()

print(f"\nQuiz complete. Your final score was {quiz.score}/{quiz.question_number}")