from ttkbootstrap import Button, Label, Entry, Frame
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business_logic import UserBusinessLogic
from Common.Decorators.performance_logger import performance_logger_decorator


class LoginFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.show_password = False

        self.main_view = main_view
        self.user_business_logic = UserBusinessLogic()

        self.grid_columnconfigure(1, weight=1)

        self.title_label = Label(self, text="Login Form")
        self.title_label.grid(row=0, column=1, pady=10, sticky="w")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.login_button = Button(self, text="Login", bootstyle="primary", command=self.login)
        self.login_button.grid(row=3, column=1, pady=(0, 10), sticky="w")

        self.register_button = Button(self, text="Register", bootstyle="success", command=self.register)
        self.register_button.grid(row=4, column=1, pady=(0, 10), sticky="w")

        self.show_button = Button(self, text="SHOW", command=self.toggle_password, bootstyle="info")
        self.show_button.grid(row=2, column=2)

    @performance_logger_decorator(" LoginFrame")
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        result = self.user_business_logic.login(username, password)

        if result.success:
            # messagebox.showinfo("Information",f"Welcome {result.data.get_fullname()}")
            home_frame = self.main_view.switch_frame("home")
            home_frame.set_current_user(result.data)

            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
        else:
            Messagebox.show_error("Error", result.message)

    def toggle_password(self):
        if self.show_password:
            self.password_entry.config(show='*')
            self.show_button.config(text="SHOW")
        else:
            self.password_entry.config(show='')
            self.show_button.config(text="Hide")
            self.show_password = not self.show_password

    def register(self):
        register_frame = self.main_view.switch_frame("register")
