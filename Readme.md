# 📦 F3project 팀원별 업무 분담 (레벨 기준)

---

## 🔷 형묵 (Level 1) – 프로젝트 초기 설정 & 구조 세팅

### 📌 주요 역할
- GitHub 레포지토리 생성 및 프로젝트 초기화
- 가상환경 생성 및 requirements.txt 작성
- Flask 및 DB 환경 세팅

### 📄 작성 및 생성할 파일
- `.venv/` (가상환경)
- `config.py`
- `run.py`
- `wsgi.py`
- `requirements.txt`
- `app/__init__.py`
- 발표자료 (5분 발표용 PPT)


---

## 🔷 kimjiyong1022 (Level 2) – ORM 모델 및 CRUD 함수 구현

### 📌 주요 역할
- SQLAlchemy 모델 정의
- 각 모델의 CRUD 함수 작성 (생성, 조회)

### 📄 작성 및 생성할 파일
- `app/models.py`
- `app/services/users.py`
- `app/services/questions.py`
- `app/services/choices.py`
- `app/services/images.py`
- `app/services/answers.py`

---

## 🔷 jhryu627 (Level 3) – API 라우팅 구현

### 📌 주요 역할
- CRUD 함수와 Flask 라우팅 연결
- API 요구사항에 따라 routes.py 작성
- Swagger 문서화 (`flask-smorest` 기반)

### 📄 작성할 파일
- `app/routes.py`

### 🔗 라우팅 예시
- `/signup` (POST)
- `/image/main` (GET)
- `/questions/<id>` (GET)
- `/questions/count` (GET)
- `/choice/<question_id>` (GET)
- `/submit` (POST)

---

## 🔷 aidoneus9 (Level 4) – EC2 배포 & 발표 자료 제작

### 📌 주요 역할
- EC2 인스턴스 생성 및 접속
- 배포 스크립트 실행 (gunicorn + nginx)


### 📁 작성 및 실행할 항목
- `executions/` 폴더 내부 설정 파일 (`gunicorn.service`, `nginx.conf` 등)
- `scripts/` 폴더 내부 배포 스크립트 (`ssl.sh`, `nginx.sh`, `mysql.sh`, `launch.sh`, `terminate.sh`, 등)

---

✅ 전체 파일 구조는 `oz_form/` 기준으로 통일합니다.
✅ 협업은 GitHub 레포지토리 [https://github.com/brojelly/F3project.git](https://github.com/brojelly/F3project.git) 를 사용합니다.
✅ 각자 맡은 레벨 완료 후 PR 요청 및 팀장(형묵) 리뷰 필수!



