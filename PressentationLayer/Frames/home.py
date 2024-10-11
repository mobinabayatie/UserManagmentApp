from tkinter import Frame, Label, Button


class HomeFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.main_view=main_view

        self.grid_columnconfigure(0, weight=1)

        self.welcome_label = Label(self)
        self.welcome_label.grid(row=0, column=0, pady=10)

        self.logout_button = Button(self, text="Logout", command=self.logout)
        self.logout_button.grid(row=1, column=0, pady=(0, 10), padx=20, sticky="ew")

    def set_current_user(self, current_user):
        self.welcome_label.config(text=f"Welcome {current_user.get_fullname()}")

    def logout(self):
        self.main_view.switch_frame("login")