class Animale:
    def __init__(self, nome, anni):
        self.nome = nome
        self.anni = anni

    def descrizione(self):
        return f"{self.nome}, {self.anni} anni"


class Cane(Animale):
    def __init__(self, nome, anni, colore):
        super().__init__(nome, anni)
        self.colore = colore

    def scheda(self):
        return f"{self.nome}: {self.colore}"


cane = Cane("Bruno", 3, "marrone")

print(cane.descrizione())
print(cane.scheda())
