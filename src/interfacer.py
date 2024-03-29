from datetime import datetime

class HomeMessage:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = datetime.now()

class GeneCmdr:
    def __init__(self, user_name):
        self.user_name = user_name
        self.inbox = []

    def send_message(self, receiver, content):
        new_message = Message(self.user_name, receiver, content)
        self.inbox.append(new_message)

    def check_inbox(self):
        if not self.inbox:
            return "No new messages"
        else:
            messages = [f"{msg.sender} ({msg.timestamp}): {msg.content}" for msg in self.inbox]
            return messages

    def display_sinbox(self):
        inbox_content = self.check_inbox()
        if inbox_content == "No new messages":
            print("Inbox:", inbox_content)
        else:
            print(f"Inbox for {self.user_name}:")
            for msg in inbox_content:
                print(msg)

    
