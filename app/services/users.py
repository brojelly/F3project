from app.models import User
from config import db
from flask import abort


def create_user(name, age, gender, email):
    """
    사용자를 생성하는 함수.

    Args:
        name (str): 사용자 이름.
        age (str): 사용자 나이 (Enum 값).
        gender (str): 사용자 성별