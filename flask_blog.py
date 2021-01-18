from flask import Flask, render_template
app = Flask(__name__)

# 可以針對同一個function設置不同的route
@app.route("/")
@app.route("/home")
def home():
    # 會直接去找templates資料夾底下的檔案
    return render_template('home.html')

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

# 下面這個condition為true的情況為，直接執行這個py檔
if __name__ == '__main__':
    # debug設為True時，直接在本機執行，python程式碼修改時，會自動reload，
    # 但debug設為False時，python程式碼修改時，需要重啟web server，才會reload changes
    app.run(debug=True)