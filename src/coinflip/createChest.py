import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER

def spacer(height=10):
    return toga.Box(style=Pack(height=height))

class CreateChestScreen(toga.Box):
    def __init__(self, app, **style):
        super().__init__(style=Pack(direction=COLUMN, padding=20, **style))
        self.app = app
        label_width = 100

        # Title
        title = toga.Label(
            "Create a New Chest", 
            style=Pack(font_size=20, font_weight='bold', padding_bottom=15, font_family="WorkSansSemiBold", color="orange")
        )
        self.add(title)

        # Chest Name
        chestNameLabel = toga.Label(
            "Chest Name:", 
            style=Pack(width=label_width, padding=(0, 5), font_family="WorkSansSemiBold")
        )

        self.chestNameInput = toga.TextInput(
            placeholder="What are you saving for?", 
            style=Pack(flex=1)
        )

        chestNameBox = toga.Box(style=Pack(direction=ROW, padding=5))
        chestNameBox.add(chestNameLabel, self.chestNameInput)

        # Chest Amount
        chestAmountLabel = toga.Label(
            "Amount:", 
            style=Pack(width=label_width, padding=(0, 5), font_family="WorkSansSemiBold")
        )

        self.chestAmountInput = toga.NumberInput(style=Pack(flex=1))

        chestAmountBox = toga.Box(style=Pack(direction=ROW, padding=5))
        chestAmountBox.add(chestAmountLabel, self.chestAmountInput)

        # Deadline
        deadlineLabel = toga.Label(
            "Deadline:", 
            style=Pack(width=label_width, padding=(0, 5), font_family="WorkSansSemiBold")
        )

        self.deadlineInput = toga.DateInput(style=Pack(flex=1))

        deadlineBox = toga.Box(style=Pack(direction=ROW, padding=5))
        deadlineBox.add(deadlineLabel, self.deadlineInput)

        # Color Icons
        colors = []
        for i in range(7):
            icon = toga.Icon(f"resources/Colors/Color{i}.png")
            button = toga.Button(
                icon=icon, 
                style=Pack(alignment=CENTER, width=40, height=40, padding=5)
            )
            colors.append(button)

        chestColorOptionLabel = toga.Label(
            "Chest Color:", 
            style=Pack(padding=(0, 5), font_family="WorkSansSemiBold")
        )

        colorsBox = toga.Box(style=Pack(direction=ROW, flex=1))
        for btn in colors:
            colorsBox.add(btn)

        chestColorOptionBox = toga.Box(style=Pack(direction=COLUMN, padding=5, alignment=CENTER))
        chestColorOptionBox.add(chestColorOptionLabel, colorsBox)

        # Buttons
        createButton = toga.Button(
            "Submit", 
            on_press=self.submit, 
            style=Pack(padding_top=20, alignment=CENTER, font_family="WorkSansSemiBold")
        )
        backButton = toga.Button(
            "Back", 
            on_press=self.go_back, 
            style=Pack(padding_top=10, alignment=CENTER, font_family="WorkSansSemiBold")
        )

        # Add all to main box
        self.add(
            chestNameBox,
            spacer(),
            chestAmountBox,
            spacer(),
            deadlineBox,
            spacer(),
            chestColorOptionBox,
            spacer(15),
            createButton,
            backButton
        )

    def submit(self, widget):
        print(f"Chest '{self.chestNameInput.value}' created with amount ${self.chestAmountInput.value}.")
        self.app.show_home()

    def go_back(self, widget):
        self.app.show_home()
