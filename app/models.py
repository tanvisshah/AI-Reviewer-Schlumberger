# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy import Column, Integer, String
# from app import db

# engine = create_engine('sqlite:///database.db', echo=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
# Base = declarative_base()
# Base.query = db_session.query_property()

# Set your classes here.

'''
class User(Base):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
'''

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from app import db
# from app import login


class User(UserMixin,db.Model):
    # __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    uploads = db.relationship('Uploads', backref='username', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#uploads.username

class Uploads(db.Model):
    upload_id = db.Column(db.Integer,primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_name = db.Column(db.String(255))
    version_number = db.Column(db.Integer)
    uploaded_filename = db.Column(db.String(255))
    modified_pdf_filename = db.Column(db.String(255))

    def __repr__(self):
        return '<Uploads {}{}{}>'.format(self.project_name,self.version_number,self.uploaded_filename)





# Create tables.
# Base.metadata.create_all(bind=engine)

