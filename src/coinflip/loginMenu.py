import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
from toga import Box, Button, ImageView, Label, Image
import os

class LoginMenu(toga.Box):
    def __init__(self, app, **style):
        super().__init__(style=Pack(direction=COLUMN, padding=20, alignment=CENTER, **style))
        self.app = app

        logo_path = os.path.join(self.app.paths.app, 'resources', 'logo.png')
        logo = Image(logo_path)
        logo_view = ImageView(
            image=logo, 
            style=Pack(height=100, width=100, padding=(20, 0))
        )

        welcome_label = toga.Label(
            "Welcome to\nCoinFlip!", 
            style=Pack(text_align=CENTER, font_size=24, padding=(10, 0))
        )

        login = toga.Button(
            "Login",
            on_press=self.show_login,
            style=Pack(padding=5),
        )

        register = toga.Button(
            "Register",
            on_press=self.show_register,
            style=Pack(padding=5),
        )

        login_guest = toga.Button(
            "Login as Guest",
            on_press=self.go_home,
            style=Pack(padding=5),
        )

        self.add(logo_view, welcome_label, login, register, login_guest)

    def go_home(self, widget):
        self.app.show_home()

    def show_login(self, widget):
        self.app.show_login_screen()
    
    def show_register(self, widget):
        self.app.show_register_screen()