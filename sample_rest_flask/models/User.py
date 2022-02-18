from configs import db
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class User(db.Model):
    """
    Model class for table USER
    """

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(255))
    phone = db.Column(db.Integer)
    adress = db.Column(db.String(500))
    password = db.Column(db.String(500))

    def __repr__(self):
        """
        To Representation method for class User
        """
        return self.first_name + " " + self.last_name


class UserSchema(ma.Schema):
    """
    Schema class for model User for converting model to JSON
    """

    class Meta:
        """
        Meta class for UserSchema
        """

        fields = ("id", "first_name", "last_name", "email", "phone", "adress", "password")
        model = User
