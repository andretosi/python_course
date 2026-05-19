class Animale:
    def __init__(self, nome, anni):
        self.nome = nome
        self.anni = anni

    def descrizione(self):
        return f"{self.nome}, {self.anni} anni"


class Gatto(Animale):
    def __init__(self, nome, anni, colori):
        super().__init__(nome, anni)
        self.colori = colori

    def miagola(self):
        return f"{self.nome} dice: Meow"

    def scheda(self):
        return f"{self.nome}: {', '.join(self.colori)}"


felix = Gatto("Felix", 13, ["bianco", "nero"])

print(felix.descrizione())
print(felix.miagola())
print(felix.scheda())
