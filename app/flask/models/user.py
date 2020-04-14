from db import db
from passlib.context import CryptContext

#crittografia password
pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
) 

class UserModel(db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80))
    password = db.Column(db.String(80))
    info = db.Column(db.String(80))


    def __init__(self, user, password, info):
        self.user = user
        self.password = password
        self.info = info
            
    def encrypt_password(self):
        return pwd_context.encrypt(self.password)


    def check_encrypted_password(self, hashed):
        return pwd_context.verify(self.password, hashed)   
    

    def json(self):
        return {
            'id': self.id,
            'user': self.user,
            'password': self.password,
            'info': self.info,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, user):
        return cls.query.filter_by(user=user).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
   