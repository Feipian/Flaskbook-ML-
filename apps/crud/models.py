from datetime import datetime

from apps.app import db
from werkzeug.security import generate_password_hash

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, index=True)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime, default = datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate = datetime.now
    )

    # setting Password attrbute
    @property
    def password(self):
        raise AttributeError("無法加載")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

