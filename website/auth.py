from .firebase import get_db
from firebase_admin import firestore

db=get_db()

def auth_register(username,password,confirmedpassword):
    users=db.collection('website').document('database').get().to_dict()['user']
    if len(password)<8:
        return 1;
    if password!=confirmedpassword:
        return 2;
    for item in users:
        if item==username:
            return 3;
    inituserdb={ 'password': password,'chats':[ { 'name': 'dafault', 'img': '../static/img/chat-page/profile-pic/InterfaceGeometricCircle.svg', 'chat':[] }]}
    db.collection('user').document(username).set(inituserdb)
    db.collection('website').document('database').update({'user':firestore.ArrayUnion([username])})
    return 0;

def auth_login(username,password):
    user=db.collection('user').document(username).get()
    if user.exists and password==user.to_dict()['password']:
        return 0;
    return 1;