from app.models import Choice
from sqlalchemy.orm import Session

def create_choice(db: Session, text: str, question_id: int):
    choice = Choice(text=text, question_id=question_id)
    db.add(choice)
    db.commit()
    db.refresh(choice)
    return choice

def get_choice(db: Session, choice_id: int):
    return db.query(Choice).get(choice_id)
