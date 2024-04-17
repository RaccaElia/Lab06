import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Analisi vendite"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txt_name = ft.TextField(
            label="name",
            width=200,
            hint_text="Insert a your name"
        )

        # button for the "hello" reply
        self.btn_hello = ft.ElevatedButton(text="Hello", on_click=self._controller.handle_hello)

        self.ddAnno = ft.Dropdown(label="anno", options=self._controller.getAnni())
        self.ddBrand = ft.Dropdown(label="brand", options=self._controller.getBrand())
        self.ddRetailer = ft.Dropdown(label="retailer", options=self._controller.getRetailer())
        row1 = ft.Row([self.ddAnno, self.ddBrand, self.ddRetailer], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.btnTop = ft.ElevatedButton(text="Top vendite", on_click=self._controller.handleTopVendite)
        self.btnAnalizza = ft.ElevatedButton(text="Analizza vendite", on_click=self._controller.handleAnalizzaVendite)
        row2 = ft.Row([self.btnTop, self.btnAnalizza], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
