from app.models import Choice, Question
from config import db
from flask import abort


def create_choice(content, sqe, question_id, is_active=True):
    """
    선택지를 생성하는 함수.

    Args:
        content (str): 선택지 내용.
        sqe (int): 선택지 순서.
        question_id (int): 선택지가 속한 질문 ID.
        is_active (bool): 선택지 활성화 여부 (기본값: True).

    Returns:
        dict: 생성된 선택지의 직렬화된 데이터.

    Raises:
        400: 질문이 존재하지 않을 경우.
    """
    # 질문 존재 여부 확인
    question = Question.query.get(question_id)
    if question is None:
        abort(400, description="해당 질문이 존재하지 않습니다.")

    # 선택지 생성
    choice = Choice(
        content=content,
        sqe=sqe,
        question_id=question_id,
        is_active=is_active
    )

    # 데이터베이스에 저장
    db.session.add(choice)
    db.session.commit()

    # 생성된 선택지 반환
    return choice.to_dict()


def get_choices_by_question_id(question_id):
    """
    특정 질문 ID에 대한 선택지 목록을 조회하는 함수.

    Args:
        question_id (int): 선택지를 조회할 질문 ID.

    Returns:
        list: 선택지의 직렬화된 데이터 목록.

    Raises:
        404: 질문이 존재하지 않을 경우.
    """
    # 질문 존재 여부 확인
    question = Question.query.get(question_id)
    if question is None:
        abort(404, description="질문을 찾을 수 없습니다.")

    # 선택지 조회
    choices = Choice.query.filter_by(question_id=question_id).all()

    # 선택지 목록 반환
    return [c.to_dict() for c in choices]