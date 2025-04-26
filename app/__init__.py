from config import db
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv

from app.models import Image
from app.views import routes  # 블루프린트 가져오기

migrate = Migrate()
load_dotenv()

def create_app():
    application = Flask(__name__)

    # 애플리케이션 설정
    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    # 데이터베이스 초기화
    db.init_app(application)

    # 마이그레이션 초기화
    migrate.init_app(application, db)

    # 블루프린트 등록
    application.register_blueprint(routes, url_prefix="/")

    return application
