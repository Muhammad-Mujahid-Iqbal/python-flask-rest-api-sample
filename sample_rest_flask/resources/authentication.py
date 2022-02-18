import datetime
from functools import wraps

import jwt
from flask import jsonify, make_response, request
from flask_restful import Resource
from models.User import User
from Utils import SECRET_KEY
from werkzeug.security import check_password_hash


class TokenResource(Resource):
    """
    View/Resource class containing GET method for Token
    """

    def get(self):
        """
        HTTP Get method to provide access token against given email and password
        """
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return make_response("could not verify", 401, {"Authentication": 'login required"'})

        user = User.query.filter_by(email=auth.username).first()
        if check_password_hash(user.password, auth.password):
            token = jwt.encode(
                {"user_id": user.id, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},
                SECRET_KEY,
                "HS256",
            )
            return jsonify({"token": token})

        return make_response("could not verify", 401, {"Authentication": '"login required"'})


def authentication_required(func):
    """
    Method to authenticate token against each API call
    """

    @wraps(func)
    def decorator(*args, **kwargs):
        """
        Implementation of decorator for token authentication method
        """
        token = None

        if "HTTP_AUTHORIZATION" in request.headers.environ:
            token = request.headers.environ["HTTP_AUTHORIZATION"].split(" ")[1]

        if not token:
            return jsonify({"message": "a valid token is missing"})
        try:
            if jwt.decode(token, SECRET_KEY, algorithms=["HS256"]):
                pass

        except:
            return jsonify({"message": "Token is invalid"})

        return func(*args, **kwargs)

    return decorator
