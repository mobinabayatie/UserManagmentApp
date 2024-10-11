from Common.Entities.User import User
from Common.Responsemodels.response import Response
from DataAccessLayer.User_data_access import UserDataAccess


class UserBusinessLogic:
    def __init__(self):
        self.user_data_access = UserDataAccess()

    def login(self, username, password):
        if len(username) < 3 or len(password) < 3:
            return Response(False, "Invalid request.", None)

        user = self.user_data_access.get_user_with_username_password(username, password)

        if not user:
            return Response(False, "Invalid username or password.", None)
        else:
            return Response(True, None, user)

    def Register_user(self, first_name, last_name, username, password):
        if len(username) < 3 or len(password) < 3:
            return Response(False, "Invalid request.", None)

        if self.user_data_access.get_user_with_username(username):
            return Response(False, "Username already exists.", None)

        user = User(None, first_name, last_name, username, password)
        self.user_data_access.add_user(user)
        return Response(True, "User registered successfully.", user)
