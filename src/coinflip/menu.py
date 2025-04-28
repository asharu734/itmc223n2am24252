import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

class MenuScreen(toga.Box):
    def __init__(self, app, **style):
        super().__init__(style=Pack(direction=COLUMN, padding=20, alignment=CENTER, **style))
        self.app = app

        menu_title = toga.Label(
            "Main Menu"
        )

        home_button = toga.Button(
            "Home",
            style=Pack(padding=5),
        )

        settings_button = toga.Button(
            "Settings",
            style=Pack(padding=5),
        )

        logout_button = toga.Button(
            "Logout",
            style=Pack(padding=5),
        )