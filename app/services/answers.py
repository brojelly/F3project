from flask import request, abort
from app.models import Answer
from config import db

def create_answer(data):
    answer = Answer(
        user_id=int(data.get("user_id", 0)),  # ✅ 수정완료
        choice_id=data["choice_id"],
    )
    db.session.add(answer)
    db.session.commit()

    return answer

def submit_answer(data):
    user_id = int(data.get("user_id", 0))  # ✅ 여기 중요
    choice_id = data.get("choice_id")       # ✅ 여기 중요

    if choice_id is None:
        abort(400, "choice_id가 없습니다.")  # 필수값 체크

    answer = Answer(
        user_id=user_id,
        choice_id=choice_id,
    )
    db.session.add(answer)
    db.session.commit()

    return answer

