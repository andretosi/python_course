class Animale:
    def __init__(self, nome, anni):
        self.nome = nome
        self.anni = anni

    def descrizione(self):
        return f"{self.nome}, {self.anni} anni"

    def verso(self):
        return "verso generico"


class Gatto(Animale):
    def verso(self):
        return "meow"


class Cane(Animale):
    def verso(self):
        return "bau"


animali = [
    Gatto("Felix", 13),
    Cane("Bruno", 3),
    Gatto("Nina", 1),
]

for animale in animali:
    print(animale.descrizione())
    print(f"{animale.nome}: {animale.verso()}")
