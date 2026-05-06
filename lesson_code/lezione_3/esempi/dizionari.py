scatola = {
    "nome": "scatola_1",
    "colore": "verde",
    "contenuto": "limone",
}

print(scatola["nome"])
print(scatola["contenuto"])

scatola["contenuto"] = "gatto"
scatola["stanza"] = "cucina"

for chiave, valore in scatola.items():
    print(f"{chiave}: {valore}")
