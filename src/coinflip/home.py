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
            style=Pack(padding=5)
        )

        add_chest_container = toga.Box(style=Pack(direction=ROW, padding_top=10))

        add_chest_container.add(toga.Box(style=Pack(flex=1)))

        add_chest_button = toga.Button(
            icon=toga.Icon('resources/icons/add_chest.png'),
            on_press=self.open_create_chest,
            style=Pack(padding=5)
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

                chest_name = toga.Label(
                    chest["name"],
                    style=Pack(font_size=16, font_weight="bold", padding_bottom=5)
                )

                color_icon = toga.ImageView(toga.Image(chest["color"]), style=Pack(width=40, height=40))
                saved = chest.get("saved", 0)
                goal = chest["amount"]
                progress = min(saved / goal, 1.0) if goal else 0

                progress_bar = toga.ProgressBar(
                    max=1.0,
                    value=progress,
                    style=Pack(height=10, width=200, padding=(5, 0))
                )

                saved_label = toga.Label(
                    f"Saved: Php {saved:.2f} / Php {goal:.2f}",
                    style=Pack(padding_top=5)
                )

                amount_input = toga.NumberInput(style=Pack(width=100, padding=(5, 0)))

                def make_add_handler(chest, input_field):
                    def handler(widget):
                        val = input_field.value or 0
                        chest["saved"] = min(chest["saved"] + val, chest["amount"])
                        self.refresh_chests()
                    return handler

                def make_subtract_handler(chest, input_field):
                    def handler(widget):
                        val = input_field.value or 0
                        chest["saved"] = max(chest["saved"] - val, 0)
                        self.refresh_chests()
                    return handler

                add_button = toga.Button("Add", on_press=make_add_handler(chest, amount_input))
                subtract_button = toga.Button("Subtract", on_press=make_subtract_handler(chest, amount_input))

                action_box = toga.Box(style=Pack(direction=ROW, padding_top=5))
                action_box.add(amount_input, add_button, subtract_button)

                box = toga.Box(style=Pack(direction=COLUMN, padding_top=5))
                box.add(progress_bar, saved_label, action_box)

                chest_box.add(toga.Box(style=Pack(flex=1)), color_icon, chest_name, box, toga.Box(style=Pack(flex=1)))
                self.insert(len(self.children) - 1, chest_box)

    def open_create_chest(self, widget):
        self.app.show_create_chest()

    def open_menu(self, widget):
        self.app.show_menu()
