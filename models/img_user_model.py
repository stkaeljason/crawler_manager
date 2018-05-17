from ext import db

class ImgUser(db.Model):
    # 表的名字:
    __tablename__ = 'instagram_img_user'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    img_user_id = db.Column(db.String(30), unique=True)
    img_user_name = db.Column(db.String(100),nullable=False)
    full_name = db.Column(db.String(100),nullable=True)
    user_profile_url = db.Column(db.String(150),nullable=True)
    image_counts = db.Column(db.Integer,nullable=True)
    crawled_time = db.Column(db.String(20),nullable=True)
    is_crawled = db.Column(db.Integer,nullable=False)