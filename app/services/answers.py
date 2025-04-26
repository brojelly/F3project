from app.models import Answer, User, Choice
from config import db
from flask import abort


def create_answers(answer_data_list):
    """
    answer_data_list: [
        {"user_id": 1, "choice_id": 2},
        {"user_id": 1, "choice_id": 4}
    ]
    """

    created = []

    for item in answer_data_list:
        user_id = item.get("user_id")
        choice_id = item.get("choice_id")

        # 유저, 선택지 존재 확인
        if not User.query.get(user_id):
            abort(400, description=f"User ID {user_id} not found.")
        if not Choice.query.get(choice_id):
            abort(400, description=f"Choice ID {choice_id} not found.")

        # 답변 생성 및 추가
        answer = Answer(user_id=user_id, choice_id=choice_id)
        db.session.add(answer)
        created.append(answer)

    # 데이터베이스 커밋
    db.session.commit()

    # 응답 반환
    return {
        "message": f"User: {answer_data_list[0]['user_id']}'s answers Success Create",
        "answers": [a.to_dict() for a in created]
    }