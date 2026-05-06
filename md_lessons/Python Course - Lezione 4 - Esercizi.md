# Lezione 4 - Esercizi

Gli esercizi di questa lezione consolidano:
- dizionari
- file di testo
- lettura di errori semplici
- classi
- attributi
- metodi
- liste di oggetti
- ereditarieta di base

Le soluzioni eseguibili sono raccolte in:
- `lesson_code/lezione_4/soluzioni/`

---

## Problema 1 - Dizionario scatola

Creare un dizionario `scatola` con queste chiavi:
- `nome`
- `colore`
- `contenuto`

La chiave `contenuto` deve contenere un altro dizionario con:
- `primo`
- `secondo`
- `terzo`

Poi:
- stampare nome e secondo contenuto
- aggiungere la chiave `stanza`
- stampare tutte le coppie chiave-valore del dizionario principale

Scheletro:
```python
scatola = {
    "nome": "scatola_1",
    "colore": "verde",
    "contenuto": {
        "primo": "gatto",
        "secondo": "limone",
        "terzo": "sedia",
    },
}

# TODO: stampa nome e secondo contenuto

# TODO: aggiungi stanza

for chiave, valore in scatola.items():
    # TODO: stampa chiave e valore
    pass
```

---

## Problema 2 - Macedonia su file

Partendo da una lista chiamata `macedonia`, salvare ogni elemento nel file `macedonia.txt`.

Poi leggere il file e stampare il contenuto.

Scheletro:
```python
macedonia = ["Anna", "Luca", "Marco"]

with open("macedonia.txt", "w", encoding="utf-8") as file:
    # TODO: scrivi ogni nome su una riga
    pass

with open("macedonia.txt", "r", encoding="utf-8") as file:
    contenuto = file.read()

print(contenuto)
```

---

## Problema 3 - Classe Gatto

Creare una classe `Gatto` con:
- attributi `nome`, `anni`, `colore`
- metodo `descrizione()` che restituisce una stringa riassuntiva
- metodo `adulto()` che restituisce `True` se `anni` e maggiore o uguale a `2`
- metodo `compie_anni()` che aumenta `anni` di `1`

Poi:
- creare un gatto di `1` anno
- stampare la descrizione
- stampare se e adulto
- chiamare `compie_anni()`
- stampare di nuovo se e adulto

Scheletro:
```python
class Gatto:
    def __init__(self, nome, anni, colore):
        # TODO: salva gli attributi
        pass

    def descrizione(self):
        # TODO: restituisci una stringa riassuntiva
        pass

    def adulto(self):
        # TODO: restituisci True o False
        pass

    def compie_anni(self):
        # TODO: aggiorna anni
        pass


gatto = Gatto("Nina", 1, "nero")
print(gatto.descrizione())
print(gatto.adulto())

gatto.compie_anni()
print(gatto.adulto())
```

---

## Problema 4 - Registro gatti

Creare due classi:

`Gatto`
- attributi `nome`, `anni`, `colore`
- metodo `adulto()`
- metodo `descrizione()`

`RegistroGatti`
- attributo `gatti`, inizialmente lista vuota
- metodo `aggiungi(gatto)`
- metodo `conta_adulti()`
- metodo `media_anni()`
- metodo `cerca_per_nome(nome)`

Poi creare un registro con tre gatti:
- Milo, 4 anni, grigio
- Nina, 1 anno, nero
- Otto, 4 anni, bianco

Stampare:
- numero di gatti adulti
- media degli anni
- descrizione di Otto

---

## Problema 5 - Animali con ereditarieta

Creare una classe generale `Animale` con:
- attributi `nome`, `anni`
- metodo `descrizione()`

Creare una classe `Cane` che eredita da `Animale` e aggiunge:
- attributo `colore`
- metodo `scheda()`

Poi creare un cane e stampare:
- descrizione dell'animale
- scheda del cane

Questo esercizio serve solo come prima esposizione all'ereditarieta.
