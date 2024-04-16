import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def getAnni(self):
        opzioni = []
        opzioni.append(ft.dropdown.Option(key=None, text="Nessun filtro"))
        for anno in self._model.get_anni():
            opzioni.append(ft.dropdown.Option(anno))
        return opzioni

    def getBrand(self):
        opzioni = []
        opzioni.append(ft.dropdown.Option(key=None, text="Nessun filtro"))
        for brand in self._model.get_brands():
            opzioni.append(ft.dropdown.Option(brand))
        return opzioni

    def getRetailer(self):
        opzioni = []
        opzioni.append(ft.dropdown.Option(key=None, text="Nessun filtro"))
        for retailer in self._model.get_retailers():
            opzioni.append(ft.dropdown.Option(key=retailer.codice, text=retailer.nome, data=retailer, on_click=self.read_retailer))
        return opzioni

    def handleTopVendite(self, e):
        top = self._model.top_vendite(self._view.ddAnno.value, self._view.ddBrand.value, self._view.ddRetailer.value)
        self._view.txt_result.controls.clear()
        for vendita in top:
            data = vendita["Date"]
            ricavo = vendita["Unit_sale_price"]*vendita["Quantity"]
            codRet = vendita["Retailer_code"]
            prod = vendita["Product_number"]
            self._view.txt_result.controls.append(ft.Text(f"Data: {data}; ricavo: {ricavo}; Retailer: {codRet}; Prodotto: {prod}"))
        self._view.update_page()

    def handleAnalizzaVendite(self, e):
        pass

    def read_retailer(self, e):
        retailer = e.control.data