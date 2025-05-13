"""
Hajijuja application
"""

import toga
from coinflip.home import HomeScreen
from coinflip.createChest import CreateChestScreen
from coinflip.menu import MenuScreen
from coinflip.login import LoginScreen

class CoinFlip(toga.App):
    def startup(self):
        self.chests = []

        toga.Font.register(
            family="WorkSansSemiBold",
            path="resources/WorkSansSemiBold.ttf"
        )

        self.main_window = toga.MainWindow(title=self.formal_name)

        # Set the starting screen
        self.home_screen = HomeScreen(self)
        self.create_chest_screen = CreateChestScreen(self)
        self.menu = MenuScreen(self)
        self.login_screen = LoginScreen(self)

        self.main_window.content = self.login_screen
        self.main_window.show()

    def show_create_chest(self):
        self.main_window.content = self.create_chest_screen

    def show_home(self):
        self.home_screen.refresh_chests()
        self.main_window.content = self.home_screen
    
    def show_menu(self):
        self.main_window.content = self.menu

    def show_login(self):
        self.main_window.content = self.login_screen

def main():
    return CoinFlip()

#beeware-venv\Scripts\activate
#kung di gumana try mo cd ..