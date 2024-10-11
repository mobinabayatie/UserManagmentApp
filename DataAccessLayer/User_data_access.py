import sqlite3
from Common.Entities.User import User
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
                   password
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
                   password
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
             INSERT INTO User(first_name,last_name,username,password)
             VALUES(?,?,?,?)
            """, (user.first_name, user.last_name, user.username, user.password))
            connection.commit()
