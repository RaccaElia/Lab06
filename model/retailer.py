from dataclasses import dataclass

@dataclass
class Retailer:
    codice: int
    nome: str
    tipo: str
    nazione: str

    def __eq__(self, other):
        self.codice = other.codice
    def __str__(self):
        return f"{self.nome} ({self.codice})"
    def __hash__(self):
        return hash(self.codice)
