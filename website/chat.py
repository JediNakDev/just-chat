from .firebase import get_db
from firebase_admin import firestore
from flask import session

def chat_text(text,currentchat,username):
    db=get_db()
    userdb=db.collection('user').document(username).get().to_dict()
    chats=userdb['chats']
    chats[currentchat]['chat'].append(text)
    db.collection('user').document(username).update({'chats':chats})

def chat_add(name,profile,username):
    db=get_db()
    chat=[ { 'name': name, 'img': profile, 'chat':[] }]
    db.collection('user').document(username).update({'chats':firestore.ArrayUnion(chat)})
    chats=db.collection('user').document(username).get().to_dict()['chats']
    return len(chats)-1


def chat_setting(name,profile,username,currentchat):
    db=get_db()
    userdb=db.collection('user').document(username).get().to_dict()
    chats=userdb['chats']
    chats[currentchat]['img']=profile
    chats[currentchat]['name']=name
    db.collection('user').document(username).update({'chats':chats})


def chat_delete(index,username):
    db=get_db()
    chat=db.collection('user').document(username).get().to_dict()['chats'][index]
    db.collection('user').document(username).update({'chats':firestore.ArrayRemove([chat])})
    currentchat=int(session['currentchat'])
    if currentchat==index and currentchat==len(db.collection('user').document(username).get().to_dict()['chats']):
        session['currentchat']=currentchat-1