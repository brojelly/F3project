from app.models import Answer
from sqlalchemy.orm import Session

def create_answer(db: Session, text: str, question_id: int):
    answer = Answer(text=text, question_id=question_id)
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer

def get_answer(db: Session, answer_id: int):
    return db.query(Answer).get(answer_id)
