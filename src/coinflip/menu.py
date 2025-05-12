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
            on_press=self.go_back
        )

        settings_button = toga.Button(
            "Settings",
            style=Pack(padding=5),
        )

        logout_button = toga.Button(
            "Logout",
            style=Pack(padding=5),
        )

        self.add(menu_title, home_button, settings_button, logout_button)
        
    def go_back(self, widget):
        self.app.show_home()