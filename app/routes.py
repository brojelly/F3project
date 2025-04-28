from flask import Blueprint, jsonify, request

from app.models import Choices
from app.services import answers, choices, images, questions, users

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET"])
def connect():
    return jsonify({"message": "Success Connect"}), 200

@routes.route("/image/main", methods=["GET"])
def get_main_image():
    image = images.get_main_image()
    if image and image.url:
        return jsonify({"image": image.url}), 200
    else:
        return jsonify({"image": None}), 200

@routes.route("/signup", methods=["POST"])
def signup_page():
    try:
        user = users.create_user()
        return (
            jsonify({
                "message": f"{user.name}님 회원가입을 축하합니다",
                "user_id": user.id,
            }),
            201,
        )
    except ValueError:
        return jsonify({"message": "이미 존재하는 계정 입니다."}), 400

@routes.route("/question/<int:question_id>", methods=["GET"])
def question_page(question_id):
    """
    특정 질문 ID에 대한 질문과 선택지를 반환합니다.
    (간단 버전: id, title, image url, choices)
    """
    question = questions.get_question_by_id(question_id)
    if not question:
        return jsonify({"error": "질문을 찾을 수 없습니다."}), 404

    choice_list = Choices.query.filter_by(question_id=question_id, is_active=True).order_by(Choices.sqe.desc()).all()

    return jsonify({
        "id": question.id,
        "title": question.title,
        "image": question.image.url if question.image else None,
        "choices": [
            {
                "id": choice.id,
                "content": choice.content,
                "is_active": choice.is_active
            } for choice in choice_list
        ]
    }), 200

@routes.route("/questions/<int:question_id>", methods=["GET"])
def get_question(question_id):
    """
    프론트 요구사항: id, title, image url, choices 배열로 반환
    """
    question = questions.get_question_by_id(question_id)
    if not question:
        return jsonify({"error": "질문을 찾을 수 없습니다."}), 404

    choice_list = choices.get_choices_by_question_id(question_id)

    return jsonify({
        "id": question.id,
        "title": question.title,
        "image": question.image.url if question.image else None,
        "choices": [
            {
                "id": choice.id,
                "content": choice.content,
                "is_active": choice.is_active
            }
            for choice in choice_list
        ]
    }), 200

@routes.route("/choice/<int:question_id>", methods=["GET"])
def get_choice_list(question_id):
    choice_list = choices.get_choices_by_question_id(question_id)
    return jsonify({
        "choices": [
            {
                "id": choice.id,
                "content": choice.content,
                "is_active": choice.is_active
            } for choice in choice_list
        ]
    }), 200

@routes.route("/questions/count", methods=["GET"])
def count_question():
    count = questions.get_question_count()
    return jsonify({"total": count}), 200

@routes.route("/submit", methods=["POST"])
def submit_answer():
    data_list = request.get_json()
    if not isinstance(data_list, list) or not data_list:
        return jsonify({"message": "Invalid data"}), 400

    for answer_data in data_list:
        # 수정 포인트 ✅ user_id로 받음
        if "user_id" not in answer_data or "choice_id" not in answer_data:
            return jsonify({"message": "user_id 또는 choice_id가 없습니다."}), 400
        answers.submit_answer(answer_data)

    user_id = int(data_list[0]["user_id"])
    return jsonify({"message": f"User: {user_id}'s answers Success Create"}), 201

@routes.route("/image", methods=["POST"])
def create_image():
    try:
        image = images.create_image()
        return jsonify({"message": f"ID: {image.id} Image Success Create"}), 201
    except ValueError:
        return jsonify({"message": "error"}), 400

@routes.route("/question", methods=["POST"])
def create_questions():
    try:
        question = questions.create_question()
        return jsonify({"message": f"Title: {question.title} question Success Create"}), 201
    except ValueError:
        return jsonify({"message": "error"}), 400

@routes.route("/choice", methods=["POST"])
def create_choice():
    try:
        choice = choices.create_choice()
        return jsonify({"message": f"Content: {choice.content} choice Success Create"}), 201
    except ValueError:
        return jsonify({"message": "error"}), 400

