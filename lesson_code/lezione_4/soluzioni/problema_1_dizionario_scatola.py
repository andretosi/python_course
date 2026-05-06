scatola = {
    "nome": "scatola_1",
    "colore": "verde",
    "contenuto": {
        "primo": "gatto",
        "secondo": "limone",
        "terzo": "sedia",
    },
}

print(scatola["nome"])
print(scatola["contenuto"]["secondo"])

scatola["stanza"] = "cucina"

for chiave, valore in scatola.items():
    print(f"{chiave}: {valore}")
