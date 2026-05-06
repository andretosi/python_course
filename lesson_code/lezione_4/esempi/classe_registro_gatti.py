class Gatto:
    def __init__(self, nome, anni, colore):
        self.nome = nome
        self.anni = anni
        self.colore = colore

    def adulto(self):
        return self.anni >= 2


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


registro = RegistroGatti()
registro.aggiungi(Gatto("Milo", 4, "grigio"))
registro.aggiungi(Gatto("Nina", 1, "nero"))
registro.aggiungi(Gatto("Otto", 4, "bianco"))

print(registro.conta_adulti())
