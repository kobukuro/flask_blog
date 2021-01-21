from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

db = SQLAlchemy(app)

from flaskblog import routes
