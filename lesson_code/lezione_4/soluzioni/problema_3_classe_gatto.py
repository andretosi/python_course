class Gatto:
    def __init__(self, nome, anni, colore):
        self.nome = nome
        self.anni = anni
        self.colore = colore

    def descrizione(self):
        return f"{self.nome}, anni {self.anni}, {self.colore}"

    def adulto(self):
        return self.anni >= 2

    def compie_anni(self):
        self.anni += 1


gatto = Gatto("Nina", 1, "nero")

print(gatto.descrizione())
print(gatto.adulto())

gatto.compie_anni()

print(gatto.descrizione())
print(gatto.adulto())
