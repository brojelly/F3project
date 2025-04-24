from app.models import User
from config import db
from flask import abort


def create_user(name, age, gender, email):
    # 중복 이메일 체크
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        abort(400, description="이미 존재하는 계정 입니다.")

    new_user = User(
        name=name,
        age=age,
        gender=gender,
        email=email
    )

    db.session.add(new_user)
    db.session.commit()

    return new_user.to_dict()

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404, description="유저를 찾을 수 없습니다.")
    return user.to_dict()