macedonia = ["Anna", "Luca", "Marco", "Beatrice", "Otto"]


def conta_nomi_lunghi(macedonia):
    conteggio = 0

    for nome in macedonia:
        print(f"Nome: {nome}")

        if len(nome) > 5:
            print("Nome lungo")
            conteggio += 1

    return conteggio


print(f"Nomi lunghi: {conta_nomi_lunghi(macedonia)}")
