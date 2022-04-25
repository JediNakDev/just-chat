from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key='lfvmklskvm obkfpasfk.fdvorebjer'
    app.config['SECRET KEY'] = 'vcrjjsafklhe;lfzcx kltmjf g;lb'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app