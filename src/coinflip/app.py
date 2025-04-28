"""
Hajijuja application
"""

import toga
from coinflip.home import HomeScreen
from coinflip.createChest import CreateChestScreen
from coinflip.menu import MenuScreen

class CoinFlip(toga.App):
    def startup(self):
        toga.Font.register(
            family="WorkSansSemiBold",
            path="resources/WorkSansSemiBold.ttf"
        )

        self.main_window = toga.MainWindow(title=self.formal_name)

        # Set the starting screen
        self.home_screen = HomeScreen(self)
        self.create_chest_screen = CreateChestScreen(self)
        self.menu = MenuScreen(self)

        self.main_window.content = self.home_screen
        self.main_window.show()

    def show_create_chest(self):
        self.main_window.content = self.create_chest_screen

    def show_home(self):
        self.main_window.content = self.home_screen

    def show_menu(self):
        self.main_window.content = self.menu

def main():
    return CoinFlip()

#beeware-venv/Script/activate
#kung di gumana try mo cd ..