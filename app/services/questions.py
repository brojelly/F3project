from app.models import Question, Image
from config import db
from flask import abort


def create_question(title, sqe, image_id, is_active=True):
    # 이미지 존재 여부 체크
    image = Image.query.get(image_id)
    if image is None:
        abort(400, description="이미지를 찾을 수 없습니다.")

    question = Question(
        title=title,
        sqe=sqe,
        image_id=image_id,
        is_active=is_active
    )

    db.session.add(question)
    db.session.commit()

    return question.to_dict()

def get_question_by_id(question_id):
    question = Question.query.get(question_id)
    if question is None:
        abort(404, description="질문을 찾을 수 없습니다.")
    return question.to_dict()

def get_total_question_count():
    total = Question.query.count()
    return {"total": total}