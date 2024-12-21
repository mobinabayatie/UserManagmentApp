from PressentationLayer.Frames.DataFrame import DateFrame
from PressentationLayer.Frames.register import RegisterFrame
from PressentationLayer.window import Window
from PressentationLayer.Frames.login import LoginFrame
from PressentationLayer.Frames.home import HomeFrame
from  PressentationLayer.Frames.user_managment import UserManagementFrame


class MainView:
    def __init__(self):
        self.frames = {}
        self.window = Window()


        self.add_frames("user_management", UserManagementFrame(self.window, self))
        self.add_frames("register", RegisterFrame(self.window, self))
        self.add_frames("home", HomeFrame(self.window, self))
        self.add_frames("login", LoginFrame(self.window, self))
        # self.add_frames("date_frame", DateFrame(self.window, self))

        self.window.show()

    def add_frames(self, name, frame):
        self.frames[name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def switch_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
        return frame
