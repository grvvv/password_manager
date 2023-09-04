import json
from tkinter import messagebox


class Search:
    def __init__(self, site_input):
        try:
            with open("data.json", mode="r") as file:
                self.data = json.load(file)
                self.site = site_input
        except FileNotFoundError:
            messagebox.showwarning(title="Huh?", message="No Data File Found.")
        else:
            self.find()

    def find(self):
        if self.site in self.data:
            searched_pass = self.data[self.site]["password"]
            messagebox.askokcancel(title=f"{self.site}", message=f"Email: {self.site} \nPassword: {searched_pass}")
        else:
            messagebox.showwarning(title="Error", message="No details for the website exists.")
