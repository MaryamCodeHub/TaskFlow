def authenticate_user(username, password):
    # TODO: implement real authentication
    if username == "admin" and password == "password":
        return True
    return False
