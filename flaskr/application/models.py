"""Data models."""
from . import db


class User(db.Model):
    """Data model for user accounts"""

    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    idUser = db.Column(
        db.Integer,
        primary_key=True
    )
    firstName = db.Column(
        db.String(45),
        nullable=False
    )
    lastName = db.Column(
        db.String(45),
        nullable=False
    )
    fullName = db.Column(
        db.String(45),
        default=firstName+" "+lastName
    )
    createdOn = db.Column(
        db.Timestamp,
        nullable=False
    )
    username = db.Column(
        db.String(45),
        nullable=False
    )
    password = db.Column(
        db.String(45),
        nullable=False
    )
    phonenumber = db.Column(
        db.String(45),
        nullable=False
    )

    def __repr__(self):
        return '<User {}>'.format(self.fullName)


