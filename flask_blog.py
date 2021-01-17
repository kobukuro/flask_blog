from flask import Flask
app = Flask(__name__)

# 可以針對同一個function設置不同的route
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

# 下面這個condition為true的情況為，直接執行這個py檔
if __name__ == '__main__':
    # debug設為True時，直接在本機執行，python程式碼修改時，會自動reload，
    # 但debug設為False時，python程式碼修改時，需要重啟web server，才會reload changes
    app.run(debug=True)