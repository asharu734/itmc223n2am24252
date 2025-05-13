import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import hashlib
import os

RESOURCES_DIR = os.path.join(os.path.dirname(__file__), "resources")
FILE_PATH = os.path.join(RESOURCES_DIR, "users.txt")

class RegisterScreen(toga.Box):
    def __init__(self, app, switch_to_login):
        super().__init__(style=Pack(direction=COLUMN, padding=20, alignment='center'))
        self.app = app
        self.switch_to_login = switch_to_login

        self.username_input = toga.TextInput(placeholder='New Username')
        self.password_input = toga.PasswordInput(placeholder='New Password')
        register_button = toga.Button('Register', on_press=self.register, style=Pack(padding_top=10))
        back_button = toga.Button('Go back', on_press= self.show_login, style=Pack(padding_top=10))
        self.status_label = toga.Label('', style=Pack(padding_top=10))

        self.add(self.username_input)
        self.add(self.password_input)
        self.add(register_button)
        self.add(back_button)
        self.add(self.status_label)

    def register(self, widget):
        username = self.username_input.value.strip()
        password = self.password_input.value.strip()

        if not username or not password:
            self.status_label.text = "Please fill both fields."
            return

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            with open(FILE_PATH, "r") as f:
                for line in f:
                    stored_user, _ = line.strip().split(":")
                    if username == stored_user:
                        self.status_label.text = "User already exists."
                        return
        except FileNotFoundError:
            pass  # If file doesn't exist, that's fine

        with open(FILE_PATH, "a") as f:
            f.write(f"{username}:{hashed_password}\n")

        self.status_label.text = "Registration successful!"

    
    def show_login(self, widget):
        self.app.show_login()
