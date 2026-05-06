def saluta(nome):
    print(f"Ciao {nome}")


def area_tappeto(base, altezza):
    return base * altezza


def saluta_default(nome, saluto="Ciao"):
    print(f"{saluto} {nome}")


saluta("Milo")
print(area_tappeto(5, 2))
saluta_default("Nina")
