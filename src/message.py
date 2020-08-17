from datetime import datetime
from database import DataBase
from push import Push


DATABASE = DataBase()


class Message:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        # Get current time
        self.time = datetime.now().strftime("%H:%M:%S")

    def write(self):
        # Send content, author, time to both push and write
        DATABASE.write(self.content, self.author, self.time)
        Push(self.content, self.author, self.time)
