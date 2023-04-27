from flask_simplelogin import SimpleLogin


def verify_login(user):
    return user.get("username") == "admin" and user.get("password") == "12345"


def init_app(app):
    SimpleLogin(app, login_checker=verify_login)
