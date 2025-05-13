import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

class LoginScreen(toga.Box):
    def __init__(self, app, **style):
        super().__init__(style=Pack(direction=COLUMN, padding=20, alignment=CENTER, **style))
        self.app = app

        login_title = toga.Label(
            "Login Menu",
            style=Pack(padding=5, alignment=CENTER),
        )

        login = toga.Button(
            "Login",
            on_press=self.go_back,
            style=Pack(padding=5),
        )

        register = toga.Button(
            "Register",
            style=Pack(padding=5),
        )

        login_guest = toga.Button(
            "Login as Guest",
            on_press=self.go_back,
            style=Pack(padding=5),
        )

        self.add(login_title, login, register, login_guest)

    def go_back(self, widget):
        self.app.show_home()