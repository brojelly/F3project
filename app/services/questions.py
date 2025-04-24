from app.models import Question
from sqlalchemy.orm import Session

def create_question(db: Session, text: str, user_id: int):
    question = Question(text=text, user_id=user_id)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

def get_question(db: Session, question_id: int):
    return db.query(Question).get(question_id)
