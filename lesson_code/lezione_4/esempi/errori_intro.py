testi = ["23", "venti"]

for testo in testi:
    try:
        numero = int(testo)
        print(f"Numero valido: {numero}")
    except ValueError:
        print(f"Numero non valido: {testo}")
