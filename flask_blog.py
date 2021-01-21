from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
'''
random SECRET_KEY取得方法:
在terminal下輸入
python
>>>import secrets
>>>secrets.token_hex(16)
'''
app.config['SECRET_KEY'] = 'e29ed5b83e8b533582d7a3f1f29d3e7f'

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