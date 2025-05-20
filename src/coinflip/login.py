import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
from toga import ImageView, Image
import hashlib
import os


RESOURCES_DIR = os.path.join(os.path.dirname(__file__), "resources")
FILE_PATH = os.path.join(RESOURCES_DIR, "users.txt")

class LoginScreen(toga.Box):
    def __init__(self, app, switch_to_register):
        super().__init__(style=Pack(direction=COLUMN, padding=20, alignment='center'))
        self.app = app
        self.switch_to_register = switch_to_register

        greet_label = toga.Label(
            "Welcome back!\nIt’s great seeing\nyou again.", 
            style=Pack(text_align=CENTER, font_size=25, font_weight = "bold", padding=30)
        )

        self.username_input = toga.TextInput(placeholder='username', style=Pack(font_size=15, height=40, width=300))
        self.password_input = toga.PasswordInput(placeholder='password',  style=Pack(font_size=15, height=40, width=300))
        login_button = toga.Button('Login', on_press=self.login, style=Pack(font_size=17, height=60, width=190, padding_top=10, background_color = "#E3B726", color = "white"))
        register_button = toga.Button('Sign up here', on_press=lambda w: self.switch_to_register(), style=Pack(font_size=17, height=60, width=190, padding_top=10, background_color = "#E3B726", color = "white"))
        back_button = toga.Button('Go back', on_press= self.show_login, style=Pack(font_size=17, height=60, width=190, padding_top=10, background_color = "#E3B726", color = "white"))
        self.status_label = toga.Label('', style=Pack(font_size=12, text_align=CENTER, padding_top=5))

        self.add(greet_label)
        self.add(self.username_input)
        self.add(self.password_input)
        self.add(self.status_label)
        self.add(login_button)
        self.add(register_button)
        self.add(back_button)

    def login(self, widget):
        username = self.username_input.value.strip()
        password = self.password_input.value.strip()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            with open(FILE_PATH, "r") as f:
                for line in f:
                    stored_user, stored_hash = line.strip().split(":")
                    if username == stored_user and hashed_password == stored_hash:
                        self.app.show_home()
            self.status_label.text = "Invalid username or password."
        except FileNotFoundError:
            self.status_label.text = "No users registered yet."
    
    def show_login(self, widget):
        self.app.show_login()
