from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
'''
random SECRET_KEY取得方法:
在terminal下輸入
python
>>>import secrets
>>>secrets.token_hex(16)
'''
app.config['SECRET_KEY'] = 'e29ed5b83e8b533582d7a3f1f29d3e7f'
# 「三個/」代表與此py檔的相對路徑
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
'''
create db in terminal:
python
>>from flask_blog import db
>>db.create_all()
'''
db = SQLAlchemy(app)

posts = [
            {
                'author': 'Corey Schafer',
                'title': 'Blog Post 1',
                'content': 'First post content',
                'date_posted': 'April 20, 2018'
            },
            {
                'author': 'Jane Doe',
                'title': 'Blog Post 2',
                'content': 'Second post content',
                'date_posted': 'April 21, 2018'
            }
        ]

class User(db.Model):
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

# 可以針對同一個function設置不同的route
@app.route("/")
@app.route("/home")
def home():
    # 會直接去找templates資料夾底下的檔案
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    # 要加上下面這行才會去validate每個欄位
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            # flash的第二個參數(category)用success或danger的用意是搭配Bootstrap的class命名(會套用不同顏色)
            # https://getbootstrap.com/docs/4.0/components/alerts/
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

# 下面這個condition為true的情況為，直接執行這個py檔
if __name__ == '__main__':
    # debug設為True時，直接在本機執行，python程式碼修改時，會自動reload，
    # 但debug設為False時，python程式碼修改時，需要重啟web server，才會reload changes
    app.run(debug=True)