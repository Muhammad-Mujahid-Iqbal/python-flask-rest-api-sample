from configs import db
from flask import request
from flask_restful import Resource
from models.User import User, UserSchema
from resources.authentication import authentication_required
from werkzeug.security import generate_password_hash


class UsersResource(Resource):
    """
    View/Resource class containing getAll and post methods for User class
    """

    @authentication_required
    def get(self):
        """
        HTTP Get method to get all users information
        """
        users = User.query.all()
        users_schema = UserSchema(many=True)
        return users_schema.dump(users)

    def post(self):
        """
        HTTP Post method to save a user information
        """

        if "password" not in request.json:
            return "Password is required", 400
        hashed_password = generate_password_hash(request.json["password"], method="sha256")
        new_user = User(
            first_name=request.json["first_name"],
            last_name=request.json["last_name"],
            email=request.json["email"],
            phone=request.json["phone"],
            adress=request.json["adress"],
            password=hashed_password,
        )
        user_schema = UserSchema()
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)


class UserResource(Resource):
    """
    View/Resource class containing get,put and delete methods for User class
    """

    @authentication_required
    def get(self, user_id):
        """
        HTTP Get method to get a user's information against given userID
        """
        user = User.query.get_or_404(user_id)
        user_schema = UserSchema()
        return user_schema.dump(user)

    @authentication_required
    def delete(self, user_id):
        """
        HTTP Delete method to remove a user's information against given userID
        """
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return "User deleted successfully", 200

    @authentication_required
    def patch(self, user_id):
        """
        HTTP Patch method to update a user's information against given userID
        """
        user = User.query.get_or_404(user_id)
        user_schema = UserSchema()
        if "first_name" in request.json:
            user.first_name = request.json["first_name"]

        if "last_name" in request.json:
            user.last_name = request.json["last_name"]

        if "email" in request.json:
            user.email = request.json["email"]

        if "adress" in request.json:
            user.adress = request.json["adress"]

        if "phone" in request.json:
            user.phone = request.json["phone"]

        db.session.commit()
        return user_schema.dump(user)
