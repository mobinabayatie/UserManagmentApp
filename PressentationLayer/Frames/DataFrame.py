
import jdatetime
from ttkbootstrap import Frame, Label, Entry, Button

class DateFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)
        self.main_view = main_view

        self.grid_columnconfigure(0, weight=1)

        self.date_label = Label(self, text="Enter date (YYYY-MM-DD):")
        self.date_label.grid(row=0, column=0, pady=10)

        self.date_entry = Entry(self)
        self.date_entry.grid(row=1, column=0, pady=10)

        self.convert_button = Button(self, text="Convert to Shamsi", command=self.convert_to_shamsi)
        self.convert_button.grid(row=2, column=0, pady=10)

        self.result_label = Label(self, text="")
        self.result_label.grid(row=3, column=0, pady=10)

    def convert_to_shamsi(self):
        try:
            selected_date = self.date_entry.get()
            year, month, day = map(int, selected_date.split('-'))

            shamsi_date = jdatetime.date.fromgregorian(day=day, month=month, year=year)
            self.result_label.config(text=f"Shamsi Date: {shamsi_date}")
        except ValueError:
            self.result_label.config(text="Invalid date format. Use YYYY-MM-DD.")