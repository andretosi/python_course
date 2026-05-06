gatto = {
    "nome": "Milo",
    "anni": 4,
    "colore": "grigio",
}

print(gatto["nome"])
print(gatto["colore"])

gatto["anni"] = 5
gatto["stanza"] = "cucina"

for chiave, valore in gatto.items():
    print(f"{chiave}: {valore}")

scatola = {
    "nome": "scatola_1",
    "colore": "verde",
    "contenuto": {
        "primo": "gatto",
        "secondo": "limone",
        "terzo": "sedia",
    },
}

print(scatola["contenuto"]["secondo"])
