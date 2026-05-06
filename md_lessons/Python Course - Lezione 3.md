# Lezione 3 - Stringhe, cicli, funzioni, dizionari e primi moduli

## Indice
- [Lezione 3 - Stringhe, cicli, funzioni, dizionari e primi moduli](#lezione-3---stringhe-cicli-funzioni-dizionari-e-primi-moduli)
  - [Indice](#indice)
  - [Prima di iniziare](#prima-di-iniziare)
    - [Regole sui percorsi](#regole-sui-percorsi)
  - [Recap lezioni precedenti](#recap-lezioni-precedenti)
  - [Obiettivi della lezione](#obiettivi-della-lezione)
  - [Struttura della lezione \(3 ore\)](#struttura-della-lezione-3-ore)
  - [Stringhe](#stringhe)
    - [Creazione e concatenazione](#creazione-e-concatenazione)
    - [f-string](#f-string)
    - [Metodi utili](#metodi-utili)
  - [Liste: ripasso e operazioni utili](#liste-ripasso-e-operazioni-utili)
    - [Indicizzazione e slicing](#indicizzazione-e-slicing)
    - [Metodi base](#metodi-base)
  - [Cicli for](#cicli-for)
    - [for su una lista](#for-su-una-lista)
    - [range](#range)
  - [While e input utente](#while-e-input-utente)
    - [While base](#while-base)
    - [While con break](#while-con-break)
  - [Funzioni](#funzioni)
    - [Definizione e chiamata](#definizione-e-chiamata)
    - [return](#return)
  - [Dizionari](#dizionari)
    - [Creazione e accesso](#creazione-e-accesso)
    - [Aggiornare un dizionario](#aggiornare-un-dizionario)
    - [Iterare su un dizionario](#iterare-su-un-dizionario)
  - [Import, errori e file di testo](#import-errori-e-file-di-testo)
    - [Importare una libreria standard](#importare-una-libreria-standard)
    - [Importare un modulo scritto da noi](#importare-un-modulo-scritto-da-noi)
    - [try / except](#try--except)
    - [Scrivere e leggere un file di testo](#scrivere-e-leggere-un-file-di-testo)
  - [Leggere gli errori](#leggere-gli-errori)
  - [Esercizi](#esercizi)
  - [Culture Pill / Esterni](#culture-pill--esterni)

---

## Prima di iniziare

- Aprire la cartella di lavoro corretta in VS Code.
- Attivare l'ambiente virtuale se gia presente.
- Verificare che `python3` funzioni da terminale.
- Tenere aperto sia il file `.py` sia il terminale integrato.

### Regole sui percorsi

Usare solo lettere, numeri, `_` e `-` nei nomi di file e cartelle quando possibile.

Esempi utili:
```bash
pwd
ls
cd nome_cartella
code .
```

---

## Recap lezioni precedenti

Nelle prime due lezioni sono stati introdotti:
- cos'e Python
- il ruolo del sistema operativo e l'organizzazione di file e cartelle
- il concetto di IDE
- Jupyter Notebook
- ambienti virtuali
- variabili, numeri e booleani
- `if / else`
- prime liste

Questa lezione introduce stringhe e cicli, e prosegue con funzioni, primi dizionari e uso base dei moduli.

---

## Obiettivi della lezione

Al termine della lezione:
- usare stringhe e formattazione di base
- manipolare liste con le operazioni piu comuni
- scrivere cicli `for`
- usare `while` per leggere input ripetuti
- definire funzioni semplici
- organizzare dati in un dizionario
- usare `import` in casi semplici
- leggere e scrivere un file di testo molto semplice
- vedere un primo uso di `try / except`
- leggere e interpretare gli errori piu comuni

---

## Struttura della lezione (3 ore)

1. Recap rapido e strumenti di lavoro - 10 min
2. Stringhe - 25 min
3. Liste e cicli `for` - 35 min
4. `while` e `input()` - 20 min
5. Funzioni - 35 min
6. Dizionari - 20 min
7. `import`, errori e file di testo - 20 min
8. Esercizi guidati e soluzioni - 30 min

Argomenti della lezione:
- stringhe
- liste
- cicli `for`
- cicli `while`
- input utente
- funzioni
- dizionari
- `import`
- `try / except`
- file di testo
- lettura degli errori

---

## Stringhe

Una stringa e una sequenza di caratteri racchiusa tra virgolette.

```python
nome = "Milo"
messaggio = "gatto verde"
```

### Creazione e concatenazione

```python
nome = "Milo"
colore = "grigio"

nome_colore = nome + " " + colore
print(nome_colore)
```

Le stringhe possono essere combinate con `+`, ma quando servono valori diversi nello stesso messaggio spesso conviene usare le `f-string`.

### f-string

```python
nome = "Milo"
anni = 4

print(f"{nome} ha {anni} anni")
```

Le `f-string` permettono di inserire variabili direttamente dentro il testo.

### Metodi utili

```python
messaggio = "  Gatto Verde  "

print(messaggio.lower())
print(messaggio.upper())
print(messaggio.strip())
```

Metodi molto usati:
- `.lower()` -> minuscolo
- `.upper()` -> maiuscolo
- `.strip()` -> rimuove spazi iniziali e finali

---

## Liste: ripasso e operazioni utili

Le liste sono collezioni ordinate e modificabili.

```python
macedonia = ["Anna", "Luca", "Marco", "Nina"]
print(macedonia)
```

### Indicizzazione e slicing

Ogni elemento ha un indice che parte da `0`.

```python
macedonia = ["Anna", "Luca", "Marco", "Nina"]

print(macedonia[0])
print(macedonia[-1])
print(macedonia[1:3])
```

Osservazioni:
- `lista[a:b]` prende da `a` incluso a `b` escluso
- l'indice `-1` indica l'ultimo elemento

### Metodi base

```python
macedonia = ["Anna", "Luca", "Marco"]

macedonia.append("Nina")
print(macedonia)

ultimo = macedonia.pop()
print(ultimo)
print(macedonia)

print(len(macedonia))
print("Luca" in macedonia)
```

Operazioni molto comuni:
- `append()` aggiunge un elemento in fondo
- `pop()` rimuove e restituisce un elemento
- `len()` restituisce il numero di elementi
- `in` verifica se un valore e presente

---

## Cicli for

Il ciclo `for` serve a ripetere un blocco di codice su ogni elemento di una sequenza.

### for su una lista

```python
macedonia = ["Anna", "Luca", "Marco", "Nina"]

for nome in macedonia:
    print(f"Nome: {nome}")
```

In questo caso la variabile `nome` assume uno alla volta tutti i valori presenti nella lista.

### range

`range()` genera una sequenza di numeri interi.

```python
for i in range(5):
    print(i)
```

Output:
```python
0
1
2
3
4
```

Altri esempi:

```python
for i in range(1, 6):
    print(i)

for i in range(0, 10, 2):
    print(i)
```

---

## While e input utente

Il ciclo `while` continua finche una condizione rimane vera.

### While base

```python
numero = 1

while numero <= 5:
    print(numero)
    numero += 1
```

Se la variabile di controllo non viene aggiornata, il ciclo puo diventare infinito.

### While con break

Un uso molto comune consiste nel leggere input finche non viene inserita una condizione di uscita.

```python
while True:
    testo = input("Scrivi qualcosa (stop per uscire): ").strip().lower()

    if testo == "stop":
        break

    print(f"Hai scritto: {testo}")
```

Esempio con una lista:

```python
numeri = []

while True:
    valore = float(input("Numero (-1 per terminare): "))

    if valore < 0:
        break

    numeri.append(valore)

print(numeri)
```

---

## Funzioni

Le funzioni permettono di riutilizzare codice e dare un nome chiaro a un'operazione.

### Definizione e chiamata

```python
def saluta(nome):
    print(f"Ciao {nome}")

saluta("Milo")
```

Una funzione si definisce con `def` e si esegue chiamandola per nome.

### return

`return` restituisce un valore al punto da cui la funzione e stata chiamata.

```python
def area_tappeto(base, altezza):
    return base * altezza

area = area_tappeto(5, 2)
print(area)
```

Esempio con parametro di default:

```python
def saluta(nome, saluto="Ciao"):
    print(f"{saluto} {nome}")
```

---

## Dizionari

Un dizionario salva coppie `chiave: valore`.

### Creazione e accesso

```python
scatola = {
    "nome": "scatola_1",
    "colore": "verde",
    "contenuto": "limone",
}

print(scatola["nome"])
print(scatola["contenuto"])
```

### Aggiornare un dizionario

```python
scatola["contenuto"] = "gatto"
scatola["stanza"] = "cucina"

print(scatola)
```

I dizionari sono utili quando un singolo elemento deve contenere piu informazioni diverse.

### Iterare su un dizionario

```python
for chiave, valore in scatola.items():
    print(f"{chiave}: {valore}")
```

---

## Import, errori e file di testo

Per usare codice definito in altri moduli o librerie si usa `import`.

### Importare una libreria standard

```python
import math

print(math.sqrt(16))
```

Si puo anche importare solo un nome specifico:

```python
from math import sqrt

print(sqrt(25))
```

### Importare un modulo scritto da noi

Esempio con due file:

```python
# utils.py
def saluta(nome):
    return f"Ciao {nome}"
```

```python
# main.py
import utils

print(utils.saluta("Milo"))
```

### try / except

Un primo esempio di gestione degli errori:

```python
try:
    numero = int(input("Numero: "))
except ValueError:
    print("Inserire un numero intero")
```

Il blocco `try / except` permette di intercettare alcuni errori comuni invece di interrompere subito il programma.

### Scrivere e leggere un file di testo

Esempio di scrittura:

```python
with open("note.txt", "w") as file:
    file.write("gatto\n")
```

Il blocco `with` gestisce apertura e chiusura del file.

Esempio di lettura:

```python
with open("note.txt", "r") as file:
    contenuto = file.read()

print(contenuto)
```

---

## Leggere gli errori

Quando Python mostra un errore, la parte piu importante e di solito l'ultima riga del messaggio.

Esempio:

```python
numero = int(input("Numero: "))
```

Se viene scritto `venti`, Python produce un errore simile a questo:

```python
ValueError: invalid literal for int() with base 10: 'venti'
```

Errori comuni in questa fase:
- `NameError` -> nome non definito
- `IndexError` -> indice fuori dalla lista
- `ValueError` -> conversione non valida

---

## Esercizi

Gli esercizi della lezione 3 sono raccolti in:
- [Python Course - Lezione 3 - Esercizi.md](Python%20Course%20-%20Lezione%203%20-%20Esercizi.md)

Le soluzioni eseguibili sono raccolte in:
- `lesson_code/lezione_3/soluzioni/`

---

## Culture Pill / Esterni

### Il nome Python

Il nome `Python` non deriva dal serpente, ma dal gruppo comico inglese **Monty Python**.
Guido van Rossum, il creatore del linguaggio, aveva scelto un nome breve, riconoscibile e con un tono leggero.

Per questo nella cultura Python compaiono spesso riferimenti ironici a sketch e battute dei Monty Python, compresi esempi con parole come `spam`, `eggs` e `ham`.

### The Zen of Python

Nel terminale Python si puo eseguire:

```python
import this
```

Questo comando mostra lo **Zen of Python**, una raccolta di principi brevi e memorabili sullo stile del codice.

Tra le idee piu note:
- la leggibilita conta
- semplice e meglio di complesso
- esplicito e meglio di implicito

### Un piccolo Easter Egg

Un altro comando storico della cultura Python e:

```python
import antigravity
```

Apre una striscia a fumetti di XKCD ed e uno degli Easter Egg piu noti del linguaggio.

### PEP e PEP 8

`PEP` significa **Python Enhancement Proposal**.
I PEP sono documenti che descrivono proposte, convenzioni e decisioni importanti per l'evoluzione del linguaggio.

Uno dei piu noti e `PEP 8`, la guida di stile piu citata in Python:
- indentazione di 4 spazi
- nomi chiari
- codice leggibile e coerente
