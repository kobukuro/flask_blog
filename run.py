from flaskblog import app  # 因為flaskblog是一個package，所以會去讀__init__.py

'''
create db in terminal:
python
>>from flaskblog import db
>>db.create_all()
>>from flaskblog.models import User, Post
>>User.query.all()
'''

# 下面這個condition為true的情況為，直接執行這個py檔
if __name__ == '__main__':
    # debug設為True時，直接在本機執行，python程式碼修改時，會自動reload，
    # 但debug設為False時，python程式碼修改時，需要重啟web server，才會reload changes
    app.run(debug=True)