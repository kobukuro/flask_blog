from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin

# this is for reloading the user from the user id stored in the session
# 讓login_manager知道怎麼找user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# 繼承UserMixin讓User model能有一些該有的欄位以及方法(flask_login需要)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # 因為會hash過，所以最後image_file固定會是長度20，password固定會是長度60
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # relationship第一個參數為Post，首字母大寫，因為指的是Post class
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # ForeignKey參數裡的user為小寫，因為指的是table名稱（class轉成table，名稱會變成全小寫）
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"