from flask import Blueprint, request, jsonify, render_template
from app.models import User, db, Question, Choices, Answer, Image

# Blueprint 정의
routes = Blueprint("views", __name__)

# 기본 연결 확인
@routes.route("/", methods=["GET"])
def check_connection():
    return render_template("index.html", message="Success Connect")

# 메인 이미지 가져오기
@routes.route("/image/main", methods=["GET"])
def get_main_image():
    image = Image.query.filter_by(type="main").first()

    if not image:
        return render_template("error.html", message="메인 이미지를 찾을 수 없습니다."), 404

    return render_template("main_image.html", image=image.url.replace('/static/', ''))



# 회원가입
@routes.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        data = request.form
        if User.query.filter_by(email=data["email"]).first():
            return render_template("error.html", message="이미 존재하는 계정 입니다."), 400
        
        user = User(
            name=data["name"],
            email=data["email"],
            age=data["age"],
            gender=data["gender"]
        )
        db.session.add(user)
        db.session.commit()
        return render_template("success.html", message=f"{data['name']}님 회원가입을 축하합니다!")
    return render_template("signup.html")

# 특정 질문 가져오기
@routes.route("/questions/<int:question_id>", methods=["GET"])
def get_question(question_id):
    question = Question.query.get_or_404(question_id)
    choices = [{"id": c.id, "content": c.content, "is_active": c.is_active} for c in question.choices]
    return render_template("question.html", question=question, choices=choices)

# 질문 개수 확인
@routes.route("/questions/count", methods=["GET"])
def get_question_count():
    total = Question.query.count()
    return render_template("questions_count.html", total=total)

# 특정 질문의 선택지 가져오기
@routes.route("/choice/<int:question_id>", methods=["GET"])
def get_choices(question_id):
    question = Question.query.get_or_404(question_id)
    choices = [{"id": c.id, "content": c.content, "is_active": c.is_active} for c in question.choices]
    return render_template("choices.html", question=question, choices=choices)

# 답변 제출
@routes.route("/submit", methods=["POST"])
def submit_answers():
    data = request.form
    for user_id, choice_id in zip(data.getlist("user_id"), data.getlist("choice_id")):
        user_answer = Answer(
            user_id=user_id,
            choice_id=choice_id
        )
        db.session.add(user_answer)
    db.session.commit()
    return render_template("success.html", message="답변이 성공적으로 제출되었습니다!")

# 이미지 생성
@routes.route("/image", methods=["GET", "POST"])
def create_image():
    if request.method == "POST":
        data = request.form
        new_image = Image(url=data["url"], type=data["type"])
        db.session.add(new_image)
        db.session.commit()
        return render_template("success.html", message=f"ID: {new_image.id} 이미지가 성공적으로 생성되었습니다!")
    return render_template("create_image.html")

# 질문 생성
@routes.route("/question", methods=["GET", "POST"])
def create_question():
    if request.method == "POST":
        data = request.form
        new_question = Question(
            title=data["title"],
            sqe=data["sqe"],
            image_id=data["image_id"]
        )
        db.session.add(new_question)
        db.session.commit()
        return render_template("success.html", message=f"질문 '{new_question.title}'이 성공적으로 생성되었습니다!")
    return render_template("create_question.html")

# 선택지 생성
@routes.route("/choice", methods=["GET", "POST"])
def create_choice():
    if request.method == "POST":
        data = request.form
        question = Question.query.get(data["question_id"])
        if not question:
            return render_template("error.html", message="질문을 찾을 수 없습니다."), 404
        
        new_choice = Choices(
            content=data["content"],
            is_active=data.get("is_active", "true") == "true",
            sqe=data["sqe"],
            question_id=question.id
        )
        db.session.add(new_choice)
        db.session.commit()
        return render_template("success.html", message=f"선택지 '{new_choice.content}'이 성공적으로 생성되었습니다!")
    return render_template("create_choice.html")