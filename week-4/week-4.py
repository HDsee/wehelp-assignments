#載入 Flask 所有相關的工具
from email import message
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
#建立 Application 物件，設定靜態檔案的處理
app=Flask(__name__, static_folder="static", static_url_path="/")

app.secret_key="HD"

@app.route('/')
def index():
    if 'user' in session:
        return redirect('/member')
    return render_template('index.html')

@app.route('/signin', methods=["POST"])
def signin():
    account=request.form['account']
    password=request.form['password']
    if (account == 'test') and (password == 'test'):
        session['user'] = account
        return redirect('/member')
    if (account == '') or (password == ''):
        return redirect("/error?message=請輸入帳號、密碼")
    return redirect("/error?message=帳號、密碼輸入錯誤")

@app.route('/member')
def member():
    if 'user' in session:
        return render_template('member.html')
    return redirect('/index')

@app.route('/error')
def error():
    message=request.args.get("message","")
    return render_template('error.html',msg=message)

@app.route('/signout')
def signout():
    session.pop('user')
    return redirect('/')

#指定埠號
app.run (port=3000)
