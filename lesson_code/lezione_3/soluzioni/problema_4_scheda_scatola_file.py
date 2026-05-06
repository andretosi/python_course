scatola = {
    "nome": "scatola_1",
    "colore": "verde",
    "contenuto": "limone",
    "stanza": "cucina",
}

for chiave, valore in scatola.items():
    print(f"{chiave}: {valore}")

riepilogo = (
    f"Nome: {scatola['nome']}\n"
    f"Colore: {scatola['colore']}\n"
    f"Contenuto: {scatola['contenuto']}\n"
    f"Stanza: {scatola['stanza']}\n"
)

with open("scheda_scatola.txt", "w", encoding="utf-8") as file:
    file.write(riepilogo)
