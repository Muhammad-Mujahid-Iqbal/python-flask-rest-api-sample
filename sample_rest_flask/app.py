from configs import api, app
from resources.authentication import TokenResource
from resources.user import UserResource, UsersResource

# Register views/resources
api.add_resource(UsersResource, "/users")
api.add_resource(UserResource, "/user/<int:user_id>")
api.add_resource(TokenResource, "/api/token")


if __name__ == "__main__":
    app.run(debug=True)
