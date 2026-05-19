class Gatto:
    def __init__(self, nome, anni, colori):
        self.nome = nome
        self.anni = anni
        self.colori = colori

    def miagola(self):
        return f"{self.nome} dice: Meow"

    def compie_anni(self):
        self.anni += 1


felix = Gatto("Felix", 13, ["bianco", "nero"])
sky = Gatto("Sky", 10, ["nero"])

print(felix.miagola())
print(sky.anni)

sky.compie_anni()

print(sky.anni)
