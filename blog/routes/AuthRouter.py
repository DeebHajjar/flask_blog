from flask import Blueprint
from blog.controllers.auth.UserController import UserController


AuthRouter = Blueprint("auth_controller", __name__)

AuthRouter.route("/login", methods=["GET", "POST"])(UserController.user_login)
AuthRouter.route("/register", methods=["GET", "POST"])(UserController.user_register)
AuthRouter.route("/logout")(UserController.user_logout)
AuthRouter.route('/reset_password', methods=["GET", "POST"])(UserController.reset_request)
AuthRouter.route('/reset_password/<token>', methods=["GET", "POST"])(UserController.reset_pass)
AuthRouter.route("/account")(UserController.user_account)
