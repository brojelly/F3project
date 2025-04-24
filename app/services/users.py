from app.models import User
from sqlalchemy.orm import Session

def create_user(db: Session, username: str):
    user = User(username=username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int):
    return db.query(User).get(user_id)
