oz_form/                        # 프로젝트 폴더
├── .venv                       # 가상환경   
├── app/                        # Flask 애플리케이션 코드 폴더
│   ├── __init__.py             # 앱 초기화 및 설정 파일
│   ├── sevices/                # DB 상호작용 orm 코드 폴더
│   │   ├── users.py            # users 테이블 관련 orm 함수
│   │   ├── questions.py        # quetions 테이블 관련 orm 함수
│   │   ├── choices.py          # choices 테이블 관련 orm 함수
│   │   ├── images.py           # images 테이블 관련 orm 함수
│   │   └── answers.py          # answers 테이블 관련 orm 함수
│   ├── models.py               # SQLAlchemy 모델 정의
│   ├── routes.py               # 뷰 및 라우트 정의
├── config.py                   # Flask 및 데이터베이스 설정 파일
├── requirements.txt            # 필요한 Python 패키지 목록
├── run.py                      # 개발환경에서 테스트 하는 실행 파일
├── wsgi.py                     # 배포환경에서의 실행 파일
└── migrations/                 # Flask-Migrate를 위한 DB 마이그레이션 파일
                                # 추후 자동으로 생성됩니다!