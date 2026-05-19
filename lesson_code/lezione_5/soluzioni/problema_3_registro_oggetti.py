class Gatto:
    def __init__(self, nome, anni, colore):
        self.nome = nome
        self.anni = anni
        self.colore = colore

    def descrizione(self):
        return f"{self.nome}, anni {self.anni}, {self.colore}"

    def adulto(self):
        return self.anni >= 2


gatti = [
    Gatto("Felix", 13, "bianco e nero"),
    Gatto("Sky", 10, "nero"),
    Gatto("Nina", 1, "grigio"),
]

for gatto in gatti:
    print(gatto.descrizione())

adulti = 0
totale_anni = 0

for gatto in gatti:
    totale_anni += gatto.anni

    if gatto.adulto():
        adulti += 1

media = totale_anni / len(gatti)

print(f"Gatti adulti: {adulti}")
print(f"Media anni: {media}")
