#載入 Flask 所有相關的工具
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session

import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='root',
    database='website'
)

cursor = db.cursor()

#建立 Application 物件，設定靜態檔案的處理
app=Flask(__name__, static_folder="static", static_url_path="/")

app.secret_key="HD"

@app.route('/')
def index():
    if 'user' in session:
        return redirect('/member')
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    name=request.form['username']
    account=request.form['newaccount']
    password=request.form['newpassword']
    
    cursor.execute('select * from member where usename=%s',(account,))
    user = cursor.fetchall()

    if (name == '') or (account == '') or (password == '') :
        return redirect("/error?message=請輸入帳號、密碼")
    if user:
        return redirect("/error?message=帳號已經被註冊")
    else:
        cursor.execute('INSERT INTO `member` (name,usename,password) VALUES (%s,%s,%s)',(name,account,password))
        db.commit()
        return redirect('/')
    

@app.route('/signin', methods=["POST"])
def signin():
    account=request.form['account']
    password=request.form['password']
    cursor.execute('select * from member where usename=%s and password=%s',(account,password))
    user = cursor.fetchall()
    if user:
        session['user'] = account
        return redirect('/member')
    if (account == '') or (password == ''):
        return redirect("/error?message=請輸入帳號、密碼")
    return redirect("/error?message=帳號、密碼輸入錯誤")

#會員頁面    
@app.route('/member')
def member():
    if 'user' in session:
        account=session['user']
        cursor.execute('select * from member where usename=%s',(account,))
        user = cursor.fetchall()
        userdata=(user[0])
        username=userdata[1]
        return render_template('member.html', name=username, username=session['user'])
    return redirect('/index')

#錯誤頁面
@app.route('/error')
def error():
    message=request.args.get("message","")
    return render_template('error.html',msg=message)

#登出
@app.route('/signout')
def signout():
    session.pop('user')
    return redirect('/')

#會員查詢
@app.route('/api/members')
def api_members():
    if 'user' in session:
        username = request.args.get('username')
        cursor.execute('select * from `member` where usename=%s',(username,))
        user = cursor.fetchall()
        if user:
            userdata=(user[0])
            data = {'data':{
                'id': userdata[0],
                'name': userdata[1],
                'username': userdata[2]
            }}
            return data
        else:
            data = {
                'data': None
            }
            return data
    return redirect('/index')

#修改會員姓名

@app.route('/api/member', methods=['POST'])
def api_membernameupdate():
    if 'user' in session:
        data = request.get_json('name')
        account = session['user']
        newName = data['name']
        mysql = 'UPDATE member SET name=%s WHERE usename=%s'
        cursor.execute(mysql, (newName,account))
        db.commit()

        data = {'ok': 'True'}
        return data
    else:
        data = {'error': 'True'}
        return data

#指定埠號
app.run (port=3000,debug=True)
