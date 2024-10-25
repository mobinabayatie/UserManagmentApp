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
            if user.is_active:
                return Response(True, None, user)
            else:
                return Response(False, "your account is not active", None)

    def Register_user(self, first_name, last_name, username, password):
        if len(username) < 3 or len(password) < 3:
            return Response(False, "Invalid request.", None)

        if self.user_data_access.get_user_with_username(username):
            return Response(False, "Username already exists.", None)

        user = User(None, first_name, last_name, username, password)
        self.user_data_access.add_user(user)
        return Response(True, "User registered successfully.", user)

    def get_current_uer(self, current_user):
        if not current_user.is_active:
            return Response(False, "your account is not active", None)
        if current_user.show_role_title() != "Admin":
            return Response(False, "Access denied!", None)
        user_list = self.user_data_access.get_user_list(current_user.id)
        return Response(True, None, user_list)

    def get_user_list(self, current_user):
        if not current_user.is_active:
            return Response(False, "Your account is deactive.", None)

        if current_user.show_role_title() != "Admin":
            return Response(False, "Access Denied.", None)

        user_list = self.user_data_access.get_user_list(current_user.id)

        return Response(True, None, user_list)

    def active_user(self, current_user, user_list):
        if not current_user.is_active:
            return Response(False, "Your account is deactive.", None)

        if current_user.show_role_title() != "Admin":
            return Response(False, "Access Denied.", None)

        for user_id in user_list:
            self.user_data_access.update_is_active(user_id, 1)

    def deactive_user(self, current_user, user_list):
        if not current_user.is_active:
            return Response(False, "Your account is deactive.", None)

        if current_user.show_role_title() != "Admin":
            return Response(False, "Access Denied.", None)

        for user_id in user_list:
            self.user_data_access.update_is_active(user_id, 0)
