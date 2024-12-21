import sqlite3
from Common.Entities.User import User
from Common.Responsemodels.response import Response
from DataAccessLayer import database_name


class UserDataAccess:
    def get_user_with_username_password(self, username, password):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   password,
                   role_id,
                   is_active
            FROM   User
            Where  username = ?
            AND    password = ?""", (username, password))

            data = cursor.fetchone()

            if data:
                # user = User(data[0], data[1], data[2], data[3], None)
                user = User(*data)
                user.password = None

                return user

    def get_user_with_username(self, username, ):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   password,
                   role_id,
                   is_active
            FROM   User
            Where  username = ?
            """, (username,))
            data = cursor.fetchone()
            if data:
                return User(*data)

    def add_user(self, user):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
             INSERT INTO User(first_name,last_name,username,password,is_active)
             VALUES(?,?,?,?,0)
            """, (user.first_name, user.last_name, user.username, user.password_hash))
            connection.commit()

    def get_user_list(self, user_id):
        user_list = []
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
                SELECT id,
                       first_name,
                       last_name,
                       username,
                       password,
                       role_id,
                       is_active
                FROM   User
                WHERE  id != ?
            """, (user_id,))
            data = cursor.fetchall()
            for item in data:
                user = User(*item)
                user.password = None
                user_list.append(user)

        return Response(True, None, user_list)

    def update_is_active(self, user_id, new_value):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
                        UPDATE User 
                        SET is_active  = ?
                        WHERE id   = ? """, (new_value, user_id))
            connection.commit()
