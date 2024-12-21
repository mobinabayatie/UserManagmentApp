from ttkbootstrap import Window, Frame, Label, Entry,Button
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business_logic import UserBusinessLogic
from PressentationLayer import main_view


class RegisterFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.main_view = main_view
        self.user_business_logic = UserBusinessLogic()

        self.grid_columnconfigure(0, weight=1)

        self.title_label = Label(self, text="Register Form")
        self.title_label.grid(row=0, column=1, pady=10, sticky="w")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        self.password_entry = Entry(self)
        self.password_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.firstname_label = Label(self, text="Firstname:")
        self.firstname_label.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="e")

        self.firstname_entry = Entry(self)
        self.firstname_entry.grid(row=3, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.lastname_label = Label(self, text="Lastname:")
        self.lastname_label.grid(row=4, column=0, pady=(0, 10), padx=10, sticky="e")

        self.lastname_entry = Entry(self)
        self.lastname_entry.grid(row=4, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.register_button = Button(self, text="Register",command=self.register, bootstyle="success")
        self.register_button.grid(row=5, column=1, pady=(0, 10), padx=(0, 20))

    def register(self):
        first_name = self.firstname_entry.get()
        last_name = self.lastname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        result = self.user_business_logic.Register_user(username, password, first_name, last_name)
        if result.success:
            Messagebox.showinfo("Success",
                                "user registered successfully! wait until your account update to active by Admin")
        else:
            Messagebox.showerror("Error", result.message)
