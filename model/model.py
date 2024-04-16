from database.DAO import DAO
from model.retailer import Retailer

class Model:
    def __init__(self):
        self._anni = []
        self._brands = []
        self._retailers = []

    def get_anni(self):
        if self._anni == []:
            for anno in DAO.get_anni():
                self._anni.append(anno[0])
        return self._anni

    def get_brands(self):
        if self._brands == []:
            for brand in DAO.get_brands():
                self._brands.append(brand[0])
        return self._brands

    def get_retailers(self):
        if self._retailers == []:
            for retailer in DAO.get_retailers():
                self._retailers.append(Retailer(retailer["Retailer_code"], retailer["Retailer_name"], retailer["Type"], retailer["Country"]))
        return self._retailers

    def top_vendite(self, anno, brand, retailer):
        if anno=="Nessun filtro" or anno=="":
            anno = None
        if brand=="Nessun filtro" or brand=="":
            brand = None
        if retailer=="Nessun filtro" or retailer=="" or retailer==None:
            return DAO.top_vendite(anno, brand, None)
        return DAO.top_vendite(anno, brand, int(retailer))