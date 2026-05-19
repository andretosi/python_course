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

    def verso(self):
        return "meow"

    def scheda(self):
        return f"{self.nome}: {', '.join(self.colori)}"


class Cane(Animale):
    def verso(self):
        return "bau"


animali = [
    Gatto("Felix", 13, ["bianco", "nero"]),
    Cane("Bruno", 3),
]

for animale in animali:
    print(animale.descrizione())
    print(f"{animale.nome}: {animale.verso()}")

felix = animali[0]
print(felix.scheda())
