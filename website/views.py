from flask import Blueprint, render_template, request, redirect, url_for, session
from .auth import auth_register,auth_login
from .firebase import get_db
from .chat import chat_text,chat_add,chat_delete,chat_setting

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/register', methods=["POST", "GET"])
def register():
    username=''
    if request.method == "POST":
        username=request.form["username"]
        password=request.form["password"]
        confirmedpassword=request.form["confirmedpassword"]
        status=auth_register(username, password, confirmedpassword)
        if status!=0:
            return render_template("register.html",status=status,username=username)
        else:
            session['username']=username
            session['currentchat']=0
            return redirect(url_for('views.chat'))
    return render_template("register.html",status=0)

@views.route('/login', methods=["POST", "GET"])
def login():
    username=''
    if request.method == "POST":
        username=request.form["username"]
        password=request.form["password"]
        status=auth_login(username, password)
        if status!=0:
            return render_template("login.html",status=status,username=username)
        else:
            session['username']=username
            db=get_db()
            userdb=db.collection('user').document(username).get().to_dict()
            session['currentchat']=0
            if len(userdb['chats'])==0:
                session['currentchat']=-1
            return redirect(url_for('views.chat'))
    return render_template("login.html",status=0,username=username)

@views.route('/chat', methods=["POST", "GET"])
def chat():
    username = session['username']      
    if request.method == "POST":
        if request.form["type"]=='chat':
            currentchat=request.form["index"]
            session['currentchat']=currentchat
        if request.form["type"]=='sent':
            currentchat=int(session['currentchat'])
            text=request.form["text"]
            if text!='':
                chat_text(text,currentchat,username)
        if request.form["type"]=='add':
            name=request.form["chat-name-add"]
            profile=request.form["chat-profile-add"]
            session['currentchat']=chat_add(name, profile,username)
        if request.form["type"]=='setting':
            currentchat=int(session['currentchat'])
            name=request.form["chat-name-add"]
            profile=request.form["chat-profile-setting"]
            chat_setting(name, profile,username,currentchat)
        if request.form["type"]=='delete':
            index=int(request.form["index"])
            chat_delete(index,username)
    db=get_db()
    userdb=db.collection('user').document(username).get().to_dict()
    currentchat=int(session['currentchat'])
    return render_template("chat.html",userdb=userdb,currentchat=currentchat,username=username)
