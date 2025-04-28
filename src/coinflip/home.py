import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

class HomeScreen(toga.Box):
    def __init__(self, app, **style):
        super().__init__(style=Pack(direction=COLUMN, padding=20, alignment=CENTER, **style))
        self.app = app

        hamburger_button = toga.Button(
            "Hamburger",
            style=Pack(padding=5),
        )

        empty_dashboard_message = toga.Label(
            """
            No chests  yet :(
            Press the button on the bottom
            to make one now!
            """,
            style=Pack(padding=5),
        )

        add_chest_button = toga.Button(
            "Add chest (+)",
            on_press=self.open_create_chest,
            style=Pack(padding=5),
        )

        self.add(hamburger_button, empty_dashboard_message, add_chest_button)

    def open_create_chest(self, widget):
        self.app.show_create_chest()
