class User:
    def __init__(self, id, firstname, lastname, username, password):
        self.id = id
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.password = password

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"


