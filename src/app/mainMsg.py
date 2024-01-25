from datetime import datetime

class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = datetime.now()

class Messenger:
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

    def display_inbox(self):
        inbox_content = self.check_inbox()
        if inbox_content == "No new messages":
            print("Inbox:", inbox_content)
        else:
            print(f"Inbox for {self.user_name}:")
            for msg in inbox_content:
                print(msg)

# Example usage
"""
user1 = Messenger("Alice")
user2 = Messenger("Bob")

user1.send_message("Bob", "Hey, how's it going?")
user2.send_message("Alice", "Hi Alice! Everything's good, thanks.")

user1.display_inbox()
user2.display_inbox()"""