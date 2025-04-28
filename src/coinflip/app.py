"""
Hajijuja application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class CoinFlip(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

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
            style=Pack(padding=5),
        )

        #main_box elements:
        main_box.add(hamburger_button)
        main_box.add(empty_dashboard_message)
        main_box.add(add_chest_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return CoinFlip()
