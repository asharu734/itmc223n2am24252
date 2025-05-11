import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, ROW

class HomeScreen(toga.Box):
    def __init__(self, app, **style):
        super().__init__(style=Pack(direction=COLUMN, padding=20, **style))
        self.app = app

        top_bar = toga.Box(style=Pack(direction=ROW, padding=(0, 0, 10, 0)))

        hamburger_button = toga.Button(
            icon=toga.Icon("resources/icons/Menu.png"),
            on_press=self.open_menu,
            style=Pack(padding=5, width=40, height=40)
        )

        add_chest_container = toga.Box(style=Pack(direction=ROW, padding_top=10))

        add_chest_container.add(toga.Box(style=Pack(flex=1)))

        add_chest_button = toga.Button(
            icon=toga.Icon('resources/icons/add_chest.png'),
            on_press=self.open_create_chest,
            style=Pack(padding=5, width=40, height=40)
        )
        
        add_chest_container.add(add_chest_button)
        add_chest_container.add(toga.Box(style=Pack(flex=1)))


        top_bar.add(hamburger_button)
        self.add(top_bar)
        self.refresh_chests()
        self.add(add_chest_container)

    def refresh_chests(self):
        for child in self.children[1:-1]:
            self.remove(child)

        if not self.app.chests:
            empty_message = toga.Label(
                """
                No chests yet :(
                Press the button on the bottom
                to make one now!
                """,
                style=Pack(padding=5, alignment=CENTER, font_family="WorkSansSemiBold", color="orange"),
            )
            self.insert(1, empty_message)
        else:
            for chest in self.app.chests:
                chest_box = toga.Box(style=Pack(direction=ROW, padding=10, alignment=CENTER))

                color_icon = toga.ImageView(toga.Image(chest["color"]), style=Pack(width=40, height=40))
                chest_info = toga.Label(
                    f"{chest['name']} - Php{chest['amount']} - Due: {chest['deadline']}",
                    style=Pack(padding_left=10, font_family="WorkSansSemiBold"),
                )

                chest_box.add(color_icon, chest_info)
                self.insert(len(self.children) - 1, chest_box)

    def open_create_chest(self, widget):
        self.app.show_create_chest()

    def open_menu(self, widget):
        self.app.show_menu()
