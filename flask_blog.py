from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home Page</h1>"

# 下面這個condition為true的情況為，直接執行這個py檔
if __name__ == '__main__':
    app.run(debug=True)