from app.models import Image
from config import db
from flask import abort


def create_image(url, image_type):
    if image_type not in ["main", "sub"]:
        abort(400, description="Invalid image type: must be 'main' or 'sub'")

    image = Image(
        url=url,
        type=image_type
    )

    db.session.add(image)
    db.session.commit()

    return image.to_dict()

def get_main_image():
    image = Image.query.filter_by(type="main").first()
    if image is None:
        abort(404, description="메인 이미지를 찾을 수 없습니다.")
    return image.to_dict()