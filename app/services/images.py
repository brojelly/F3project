from app.models import Image
from sqlalchemy.orm import Session

def create_image(db: Session, url: str, description: str = ""):
    image = Image(url=url, description=description)
    db.add(image)
    db.commit()
    db.refresh(image)
    return image

def get_image(db: Session, image_id: int):
    return db.query(Image).get(image_id)
