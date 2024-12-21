from ttkbootstrap import Window


class Window(Window):
    def __init__(self, title="User Management Application"):
        super().__init__(title=title,themename="superhero")
        self.geometry("500x300")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def show(self):
        self.mainloop()
