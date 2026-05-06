# Lezione 3 - Esercizi

Gli esercizi di questa lezione consolidano:
- stringhe
- cicli `for`
- cicli `while`
- funzioni
- dizionari
- `import`
- primi file di testo

Le soluzioni eseguibili sono raccolte in:
- `lesson_code/lezione_3/soluzioni/`

---

## Problema 1 - Frase con stringhe

Definire le variabili:
- `nome`
- `oggetto`
- `colore`

Stampare una frase finale con una `f-string`.

Esempio di output:
```python
Anna ha un limone verde.
```

Scheletro:
```python
nome = "Anna"
oggetto = "limone"
colore = "verde"

# TODO: stampa la frase finale
```

---

## Problema 2 - Macedonia con for e funzione

Data la lista:

```python
macedonia = ["Anna", "Luca", "Marco", "Beatrice", "Otto"]
```

Scrivere una funzione `conta_nomi_lunghi(macedonia)` che:
- stampi ogni nome
- stampi `"Nome lungo"` se il nome ha piu di `5` caratteri
- restituisca quanti nomi hanno piu di `5` caratteri

Scheletro:
```python
macedonia = ["Anna", "Luca", "Marco", "Beatrice", "Otto"]

def conta_nomi_lunghi(macedonia):
    conteggio = 0

    for nome in macedonia:
        # TODO: stampa nome
        # TODO: controlla se len(nome) > 5
        pass

    return conteggio

print(f"Nomi lunghi: {conta_nomi_lunghi(macedonia)}")
```

---

## Problema 3 - Registro numeri con while

Scrivere un programma che:
- chieda all'utente di inserire numeri
- si fermi quando viene inserito un valore negativo
- salvi i valori in una lista
- stampi il numero totale di valori inseriti

Scheletro:
```python
numeri = []

while True:
    valore = float(input("Numero (-1 per terminare): "))

    if valore < 0:
        break

    numeri.append(valore)

print(f"Valori inseriti: {len(numeri)}")
print(numeri)
```

---

## Problema 4 - Scatola con dizionario e file

Creare un dizionario `scatola` con queste chiavi:
- `nome`
- `colore`
- `contenuto`
- `stanza`

Poi:
- stampare i valori con un ciclo sul dizionario
- costruire una stringa riassuntiva
- salvare il riepilogo in un file chiamato `scheda_scatola.txt`

Scheletro:
```python
scatola = {
    "nome": "scatola_1",
    "colore": "verde",
    "contenuto": "limone",
    "stanza": "cucina",
}

for chiave, valore in scatola.items():
    # TODO: stampa chiave e valore
    pass

riepilogo = ""

with open("scheda_scatola.txt", "w") as file:
    # TODO: scrivi il riepilogo nel file
    pass
```
