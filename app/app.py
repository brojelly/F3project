from flask import Flask
from flasgger import Swagger
from app.config import db, Config  # Config 클래스 가져오기
from app.views import routes
from app.models import Image

def create_app():
    app = Flask(__name__)

    # Flask 설정
    app.config.from_object(Config)  # Config 클래스를 사용하여 설정 적용

    # 데이터베이스 초기화
    db.init_app(app)

    # Swagger 초기화
    Swagger(app)

    # 블루프린트 등록
    app.register_blueprint(routes, url_prefix="/")

    # 데이터베이스 테이블 생성
    with app.app_context():
        db.create_all()

    return app