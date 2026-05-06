class Gatto:
    def __init__(self, nome, anni, colore):
        self.nome = nome
        self.anni = anni
        self.colore = colore

    def adulto(self):
        return self.anni >= 2

    def descrizione(self):
        return f"{self.nome}, anni {self.anni}, {self.colore}"


class RegistroGatti:
    def __init__(self):
        self.gatti = []

    def aggiungi(self, gatto):
        self.gatti.append(gatto)

    def conta_adulti(self):
        totale = 0

        for gatto in self.gatti:
            if gatto.adulto():
                totale += 1

        return totale

    def media_anni(self):
        if len(self.gatti) == 0:
            return 0

        totale = 0

        for gatto in self.gatti:
            totale += gatto.anni

        return totale / len(self.gatti)

    def cerca_per_nome(self, nome):
        for gatto in self.gatti:
            if gatto.nome == nome:
                return gatto

        return None


registro = RegistroGatti()
registro.aggiungi(Gatto("Milo", 4, "grigio"))
registro.aggiungi(Gatto("Nina", 1, "nero"))
registro.aggiungi(Gatto("Otto", 4, "bianco"))

print(f"Gatti adulti: {registro.conta_adulti()}")
print(f"Media anni: {registro.media_anni()}")

trovato = registro.cerca_per_nome("Otto")

if trovato is not None:
    print(trovato.descrizione())
