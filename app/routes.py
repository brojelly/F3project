from flask import Blueprint, request, jsonify
from app.models import User, db, Question, Choices, Answer, Image

# Blueprint 정의
routes = Blueprint("views", __name__)

# 기본 연결 확인
@routes.route("/", methods=["GET"])
def check_connection():
    return jsonify({"message": "Success Connect"})

# 메인 이미지 가져오기
@routes.route("/image/main", methods=["GET"])
def get_main_image():
    return jsonify({"image": "https://example.com/image.jpg"})

# 회원가입
@routes.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "이미 존재하는 계정 입니다."}), 400
    
    user = User(
        name=data["name"],
        email=data["email"],
        age=data["age"],
        gender=data["gender"]
    )
    db.session.add(user)
    db.session.commit()
    
    return jsonify({"message": f"{data['name']}님 회원가입을 축하합니다", "user_id": user.id}), 200

# 특정 질문 가져오기
@routes.route("/questions/<int:question_id>", methods=["GET"])
def get_question(question_id):
    question = Question.query.get_or_404(question_id)
    choices = [{"id": c.id, "content": c.content, "is_active": c.is_active} for c in question.choices]
    
    return jsonify({
        "id": question.id,
        "title": question.title,
        "image": question.image_url,
        "choices": choices
    })

# 질문 개수 확인
@routes.route("/questions/count", methods=["GET"])
def get_question_count():
    total = Question.query.count()
    return jsonify({"total": total})

# 특정 질문의 선택지 가져오기
@routes.route("/choice/<int:question_id>", methods=["GET"])
def get_choices(question_id):
    question = Question.query.get_or_404(question_id)
    choices = [{"id": c.id, "content": c.content, "is_active": c.is_active} for c in question.choices]
    
    return jsonify({"choices": choices})

# 답변 제출
@routes.route("/submit", methods=["POST"])
def submit_answers():
    data = request.get_json()
    for answer in data:
        user_answer = Answer(
            user_id=answer["user_id"],
            choice_id=answer["choice_id"]
        )
        db.session.add(user_answer)
    db.session.commit()
    
    return jsonify({"message": f"User: {data[0]['user_id']}'s answers Success Create"})

# 이미지 생성
@routes.route("/image", methods=["POST"])
def create_image():
    data = request.get_json()
    new_image = Image(url=data["url"])
    db.session.add(new_image)
    db.session.commit()
    
    return jsonify({"message": f"ID: {new_image.id} Image Success Create"})

# 질문 생성
@routes.route("/question", methods=["POST"])
def create_question():
    data = request.get_json()
    new_question = Question(
        title=data["title"],
        image_url=data["image_url"]
    )
    db.session.add(new_question)
    db.session.commit()
    
    return jsonify({"message": f"Title: {new_question.title} Success Create"})

# 선택지 생성
@routes.route("/choice", methods=["POST"])
def create_choice():
    data = request.get_json()
    question = Question.query.get(data["question_id"])
    if not question:
        return jsonify({"message": "Question not found"}), 404
    
    new_choice = Choices(
        content=data["content"],
        is_active=data["is_active"],
        question_id=question.id
    )
    db.session.add(new_choice)
    db.session.commit()
    
    return jsonify({"message": f"Content: {new_choice.content} Success Create"})