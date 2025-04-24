from app.models import Choice, Question
from config import db
from flask import abort


def create_choice(content, sqe, question_id, is_active=True):
    # 질문 존재 여부 확인
    question = Question.query.get(question_id)
    if question is None:
        abort(400, description="해당 질문이 존재하지 않습니다.")

    choice = Choice(
        content=content,
        sqe=sqe,
        question_id=question_id,
        is_active=is_active
    )

    db.session.add(choice)
    db.session.commit()

    return choice.to_dict()


def get_choices_by_question_id(question_id):
    question = Question.query.get(question_id)
    if question is None:
        abort(404, description="질문을 찾을 수 없습니다.")

    choices = Choice.query.filter_by(question_id=question_id).all()
    return [c.to_dict() for c in choices]