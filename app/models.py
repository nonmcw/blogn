from . import db
from datetime import datetime

class Role(db.Model):
    __tables__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default_role = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role')
    
    def __repr__():
        return '<Role %r>' % self.name
    
class User(db.Model):
    __tables__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
