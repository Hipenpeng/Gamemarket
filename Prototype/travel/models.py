from . import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False) #should be 128 in length to store hash
    adsPc = db.relationship('PC', backref='author', lazy=True)


class PC(db.Model):
    __tablename__ = 'pc'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    currency = db.Column(db.String(3))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_name = db.Column(db.String(100))
    user_email = db.Column(db.String(100))
    condition = db.Column(db.String(100))

    def __repr__(self):
        return "<Name: {}>".format(self.name)

class Xbox(db.Model):
    __tablename__ = 'xbox'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    currency = db.Column(db.String(3))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_name = db.Column(db.String(100))
    user_email = db.Column(db.String(100))
    condition = db.Column(db.String(100))

    def __repr__(self):
        return "<Name: {}>".format(self.name)

class Nintendo(db.Model):
    __tablename__ = 'nintendo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    currency = db.Column(db.String(3))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_name = db.Column(db.String(100))
    user_email = db.Column(db.String(100))
    condition = db.Column(db.String(100))

    def __repr__(self):
        return "<Name: {}>".format(self.name)

class PlayStation(db.Model):
    __tablename__ = 'playstation'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    currency = db.Column(db.String(3))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_name = db.Column(db.String(100))
    user_email = db.Column(db.String(100))
    condition = db.Column(db.String(100))

    def __repr__(self):
        return "<Name: {}>".format(self.name)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    nintendo_id = db.Column(db.Integer, db.ForeignKey('nintendo.id'))
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    user = db.relationship('User', backref='comment_user')

    def __repr__(self):
        return "<Comment: {}>".format(self.text)

class CommentP(db.Model):
    __tablename__ = 'commentsP'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    playstation_id = db.Column(db.Integer, db.ForeignKey('playstation.id'))
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    user = db.relationship('User', backref='comment_userP')

    def __repr__(self):
        return "<Comment: {}>".format(self.text)

class CommentX(db.Model):
    __tablename__ = 'commentsX'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    xbox_id = db.Column(db.Integer, db.ForeignKey('xbox.id'))
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    user = db.relationship('User', backref='comment_userX')

    def __repr__(self):
        return "<Comment: {}>".format(self.text)

class CommentPC(db.Model):
    __tablename__ = 'commentsPC'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pc_id = db.Column(db.Integer, db.ForeignKey('pc.id'))
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    user = db.relationship('User', backref='comment_userPC')

    def __repr__(self):
        return "<Comment: {}>".format(self.text)

class OrderX(db.Model):
    __tablename__='orders_X'
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    xbox_id = db.Column(db.Integer, db.ForeignKey('xbox.id'))
    owner_name = db.Column(db.String(10))
    image = db.Column(db.String(100))
    date = db.Column(db.String(3))
    created_at = db.Column(db.DateTime, default=datetime.now())


class OrderPS(db.Model):
    __tablename__='orders_PS'
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    playstation_id = db.Column(db.Integer, db.ForeignKey('playstation.id'))
    owner_name = db.Column(db.String(10))
    image = db.Column(db.String(100))
    date = db.Column(db.String(3))
    created_at = db.Column(db.DateTime, default=datetime.now())

class OrderPC(db.Model):
    __tablename__='orders_PC'
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pc_id = db.Column(db.Integer, db.ForeignKey('pc.id'))
    owner_name = db.Column(db.String(10))
    image = db.Column(db.String(100))
    date = db.Column(db.String(3))
    created_at = db.Column(db.DateTime, default=datetime.now())

class OrderNi(db.Model):
    __tablename__='orders_Ni'
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    nintendo_id = db.Column(db.Integer, db.ForeignKey('nintendo.id'))
    owner_name = db.Column(db.String(10))
    image = db.Column(db.String(100))
    date = db.Column(db.String(3))
    created_at = db.Column(db.DateTime, default=datetime.now())