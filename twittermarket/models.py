from datetime import datetime
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from twittermarket import db

# from flask import current_app
# from flaskblog import db, login_manager

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60), nullable = False)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    product = db.Column(db.String(20), nullable = False)
    location = db.Column(db.String(20), nullable = False)
    
    # def get_reset_token(self, expires_sec=1800):
    #     s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
    #     return s.dumps({'user_id': self.id}).decode('utf-8')

    # def verify_reset_token(token):
    #     s = Serializer(current_app.config['SECRET_KEY'])
    #     try:
    #         user_id = s.loads(token)['user_id']
    #     except:
    #         return None
    #     return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}', '{self.id}', '{self.password}')"
