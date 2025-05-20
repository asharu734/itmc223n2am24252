import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
from toga import ImageView, Image
import os

class LoginMenu(toga.Box):
    def __init__(self, app, **style):
        super().__init__(style=Pack(direction=COLUMN, padding=20, alignment=CENTER, **style))
        self.app = app
        
        logo_view = ImageView(
            image='resources/Logos/logo.png', 
            style=Pack(height=130, width=130, padding=(20, 0))
        )

        hajijuja_logo_view = ImageView(
            image='resources/Logos/Company Logo.png', 
            style=Pack(height=30, width=73, padding=(20, 0))
        )
  
        welcome_label = toga.Label(
            "Welcome to\nCoinFlip!", 
            style=Pack(text_align=CENTER, font_size=28, font_weight = "bold", padding=(10, 0))
        )

        slogan_label = toga.Label(
            "Track Your Savings, Track Your Life.", 
            style=Pack(text_align=CENTER, font_size=14, padding=7)
        )
        
        login_button = toga.Button(
            "Login",
            on_press=self.show_login,
            style=Pack(font_size=18, padding=10, width=280, height=70, alignment = 'center', background_color = "#E3B726", color = "white")
        )

        register = toga.Button(
            "Register",
            on_press=self.show_register,
            style=Pack(font_size=18, padding=10, width=280, height=70, alignment = 'center', background_color = "#E3B726", color = "white")
        )

        login_guest = toga.Button(
            "Login as Guest",
            on_press=self.go_home,
            style=Pack(font_size=18, padding=10, width=280, height=70, alignment = 'center', background_color = "#E3B726", color = "white")
        )

        self.add(logo_view, welcome_label, slogan_label, login_button, register, login_guest, hajijuja_logo_view)

    def go_home(self, widget):
        self.app.show_home()

    def show_login(self, widget):
        self.app.show_login_screen()
    
    def show_register(self, widget):
        self.app.show_register_screen()