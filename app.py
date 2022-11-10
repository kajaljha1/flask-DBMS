from flask import Flask,render_template,request,redirect,url_for
import database as db

app=Flask(__name__)
@app.route('/')
def home():
    return render_template("login.html")

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if not (name1==None or pwd==None):
        return redirect(url_for('index'))

@app.route('/index')
def index():
    data=db.readall()
    print(data)
    return render_template("index.html",data=data,msg="Welcome to LifeCare Hospital \n' WE GIVE YOU THE CARE YOU DESERVE!' ")

@app.route('/insert')
def insert():
    id=request.args.get('ID')
    name=request.args.get('Name')
    age=request.args.get('Age')
    location=request.args.get('Location')
    gender=request.args.get('Gender')
    print(id,name,age,location,gender)
    if not(id==None or name==None or age==None or location==None or gender==None):
        db.insertrecord(id,name,age,location,gender)
        return redirect(url_for('index'))
    return render_template("insert.html")
@app.route('/delete/<id>')
def delete(id):
    db.deleterecord(id)
    return redirect(url_for('index'))
@app.route('/update')
def updaterecord():
    id=request.args.get("ID")
    name=request.args.get("Name")
    age=request.args.get("Age")
    location=request.args.get('Location')
    gender=request.args.get('Gender')
    data=(id,name,age,location,gender)
    db.updaterecord(data)
    return redirect(url_for('index'))

@app.route('/update/<id>')
def update(id):
    data=db.readbyid(id)
    return render_template("update.html",data=data)

app.run(debug=True)