import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
import hashlib
import os

RESOURCES_DIR = os.path.join(os.path.dirname(__file__), "resources")
FILE_PATH = os.path.join(RESOURCES_DIR, "users.txt")

class RegisterScreen(toga.Box):
    def __init__(self, app, switch_to_login):
        super().__init__(style=Pack(direction=COLUMN, padding=20, alignment='center'))
        self.app = app
        self.switch_to_login = switch_to_login

        greet_label = toga.Label(
            "Only a few more clicks\nand you'll be tracking\nyour savings in no time!", 
            style=Pack(text_align=CENTER, font_size=25, font_weight = "bold", padding=30)
        )

        self.username_input = toga.TextInput(placeholder='new username', style=Pack(font_size=15, height=40, width=300))
        self.password_input = toga.PasswordInput(placeholder='new password', style=Pack(font_size=15, height=40, width=300))
        register_button = toga.Button('Sign up', on_press=self.register, style=Pack(font_size=17, height=60, width=190, padding_top=10, background_color = "#E3B726", color = "white"))
        back_button = toga.Button('Go back', on_press= self.show_login, style=Pack(font_size=17, height=60, width=190, padding_top=10, background_color = "#E3B726", color = "white"))
        self.status_label = toga.Label('', style=Pack(font_size=12, text_align=CENTER, padding_top=5))

        self.add(greet_label)
        self.add(self.username_input)
        self.add(self.password_input) 
        self.add(self.status_label)
        self.add(register_button)
        self.add(back_button)

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
