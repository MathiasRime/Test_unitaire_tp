class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        self.is_checked_out = True
        print(f"{self.title} by {self.author} has been checked out.")

    def check_in(self):
        self.is_checked_out = False
        print(f"{self.title} by {self.author} has been checked in.")

