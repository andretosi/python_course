# Lezione 2 – Python di base: tipi di dato, strutture di controllo, liste e funzioni

## Indice
- [Lezione 2 – Python di base: tipi di dato, strutture di controllo, liste e funzioni](#lezione-2--python-di-base-tipi-di-dato-strutture-di-controllo-liste-e-funzioni)
  - [Indice](#indice)
  - [Prima di iniziare](#prima-di-iniziare)
    - [Regole sui percorsi](#regole-sui-percorsi)
  - [Recap Lezione 1](#recap-lezione-1)
    - [Cosa abbiamo fatto](#cosa-abbiamo-fatto)
    - [Quando usare altri linguaggi](#quando-usare-altri-linguaggi)
  - [Python Basics](#python-basics)
    - [Commenti](#commenti)
    - [Variabili](#variabili)
    - [Leggere gli errori](#leggere-gli-errori)
    - [Input da tastiera (input())](#input-da-tastiera-input)
  - [Data Types](#data-types)
    - [Boolean](#boolean)
    - [Stringhe](#stringhe)
    - [Numeri](#numeri)
      - [Interi](#interi)
      - [Float](#float)
      - [Operazioni miste](#operazioni-miste)
    - [Liste](#liste)
  - [If / Else / Elif](#if--else--elif)
  - [Cicli For](#cicli-for)
  - [Funzioni](#funzioni)
  - [PEP 8 e buone pratiche](#pep-8-e-buone-pratiche)
  - [Esercizi Pratici](#esercizi-pratici)
    - [Problema 1 – Valutazione Rischio Paziente](#problema-1--valutazione-rischio-paziente)
    - [Problema 2 – Frequenze Cardiache](#problema-2--frequenze-cardiache)
    - [Problema 3 – BMI con funzione](#problema-3--bmi-con-funzione)
  - [Culture Pill / Esterni](#culture-pill--esterni)
  - [Soluzioni](#soluzioni)
    - [Soluzione Problema 1](#soluzione-problema-1)
    - [Soluzione Problema 2](#soluzione-problema-2)
    - [Soluzione Problema 3](#soluzione-problema-3)

---

## Prima di iniziare

- Localizzare la cartella di lavoro.  
- Cancellare i file inutili.  
- Aprire **Visual Studio Code**.  
- Se hai creato un ambiente virtuale nella lezione 1, attivalo.  
- Ricreare i file con **nomi senza spazi**.  
- Usare `print(f"...")` e non `printf()`.  
- Testare che Python funzioni correttamente.

### Regole sui percorsi
Usare solo lettere, numeri, trattini bassi `_` o trattini medi `-` nei nomi di file e cartelle.  
Evitare spazi o simboli speciali.

Esempi di percorsi:
```bash
.                # cartella corrente
..               # cartella superiore
../sibling       # cartella "fratello"
~/Desktop        # cartella Desktop
```

Aprire una cartella in VS Code:
```bash
code .
```

Creare una cartella o un file:
```bash
mkdir nome_cartella
touch file.py
```

---

## Recap Lezione 1

### Cosa abbiamo fatto
- Perché Python:
  - Facile da imparare, molto diffuso, ottimo per prototipare e per il Machine Learning.
- Perché Linux (WSL o nativo):
  - Leggero, efficiente, standard per sistemi embedded e server, open-source.
- Perché Visual Studio Code:
  - IDE moderno, estensioni per tutti i linguaggi, funziona con venv e Jupyter senza attriti.
- Ambienti virtuali (`venv`):
  - Isolano le dipendenze di ogni progetto. Ricorda: **attivare** prima di installare con `pip`.
- Jupyter Notebook:
  - Celle di codice + Markdown, ottimo per esplorare dati e documentare ragionamenti.

- Perché non usare solo Google Colab/compilatori online:
  - Sono ottimi per la ricerca e prototipi, ma nel lavoro reale spesso si lavora su macchine/server senza interfaccia grafica.
  - Abituarsi al terminale e all'ambiente locale aiuta a essere produttivi in contesti professionali.

### Quando usare altri linguaggi
- C/C++ → alte prestazioni, sistemi embedded.  
- MATLAB → analisi numerica o scientifica.  
- JavaScript → sviluppo web.  
- Java / Rust → software strutturato o ad alte prestazioni.  
- R → analisi statistica e data science.

---

## Python Basics

### Commenti
```python
# Questo è un commento singolo

"""
Questa è una stringa multilinea.
Se la metti all'inizio di un file o di una funzione
diventa una docstring, cioè documentazione leggibile da Python.
"""
```

Per commentare davvero si usa `#`. Le triple virgolette tornano molto utili soprattutto per le **docstring**, che rivedremo meglio nella sezione sulle funzioni.
Scrivere sempre commenti chiari per spiegare **perché** si fa qualcosa, non solo **cosa** si fa.

---

### Variabili

Le variabili possono contenere:
- lettere  
- numeri  
- trattini bassi `_`  

Non possono iniziare con un numero.

Esempi rapidi:
```python
eta_paziente = 25   # ok
eta2 = 25           # ok
# 2eta = 25         # no: inizia con un numero
# eta-paziente = 25 # no: '-' viene letto come sottrazione
```

Esempio:
```python
nome = "Mario"
eta = 25
```

Buona pratica:
- usare nomi in **minuscolo**
- separare parole con `_`  

Evita nomi poco descrittivi come `a`, `x1` quando possibile. Preferisci `eta_paziente`, `frequenze_bpm`.

Le variabili non hanno un tipo dichiarato staticamente: il tipo dipende dal valore assegnato.

---

### Leggere gli errori

Quando Python stampa un errore (traceback), leggi dall’ultima riga verso l’alto: lì trovi il tipo e il messaggio.

Esempio di NameError:
```python
print(nome)
# NameError: name 'nome' is not defined
```
Significa che la variabile `nome` non è stata definita prima dell’uso. Definisci o correggi il nome della variabile.

Errori comuni:
- NameError → variabile non definita o scritta male.  
- TypeError → operazione non valida per quel tipo (es. sommare stringa e numero).  
- ValueError → conversione fallita (es. `int("ciao")`).

---

### Input da tastiera (input())

La funzione `input()` legge una riga di testo dalla tastiera e restituisce sempre una stringa (`str`). Puoi passare una stringa come prompt.

Esempi base:
```python
nome = input("Come ti chiami? ")           # restituisce una stringa
eta = int(input("Quanti anni hai? "))      # converte la stringa in int
peso = float(input("Peso (kg): "))         # converte la stringa in float
```

Note importanti:
- `input()` → sempre stringa: usa `int(...)` o `float(...)` per numeri.  
- Se la conversione fallisce (es. testo non numerico), Python solleva un `ValueError` (vedi "Leggere gli errori").

Curiosità, non da memorizzare adesso: `input()` è una funzione **built-in**, cioè è già disponibile senza bisogno di `import`.

---

## Data Types

### Boolean
```python
vero = True
falso = False
```

I boolean compaiono spesso come risultato di confronti o espressioni logiche:
```python
eta >= 18           # True o False
pressione > 140     # True o False
fumatore and eta > 65
not febbre
```

### Stringhe
Le stringhe si scrivono tra virgolette singole o doppie:
```python
messaggio = "Ciao mondo!"
```

Metodi utili:
```python
messaggio.upper()
messaggio.lower()
messaggio.strip()
messaggio.title()   # Prima lettera maiuscola per ogni parola
messaggio.rstrip()  # Rimuove spazi a destra
messaggio.lstrip()  # Rimuove spazi a sinistra
```

Formattazione:
```python
nome = "Anna"
eta = 22
testo = f"{nome} ha {eta} anni"
```

Caratteri speciali:
- `\n` → nuova riga  
- `\t` → tabulazione  

Attenzione alle virgolette dentro le stringhe:
```python
# Sbagliato → interrompe la stringa
messaggio = 'Ti piace l'odore dei funghi?'

# Giusto → usa virgolette diverse o l'escape
messaggio = "Ti piace l'odore dei funghi?"
messaggio = 'Ti piace l\'odore dei funghi?'
```

---

### Numeri

#### Interi
```python
x = 5
y = 2
somma = x + y
diff = x - y
prodotto = x * y
quoziente_float = x / y   # 2.5
quoziente_intero = x // y # 2 divisione intera
resto = x % y             # 1 modulo
potenza = x ** y          # 25
```

#### Float
```python
z = 5.3
```

#### Operazioni miste
```python
risultato = 5 / 2     # float
intero = 5 // 2        # divisione intera
resto = 5 % 2          # 1
potenza = 2 ** 10      # 1024
```

Costanti:
```python
MAX_SPEED = 300
```

Numeri leggibili:
```python
velocita_luce = 299_792_458
```

Assegnazioni multiple e scambio rapido di variabili:
```python
a, b = 1, 2
b, a = a, b  # scambia i valori
```

---

### Liste
Le **liste** sono collezioni ordinate e modificabili.

```python
frutti = ["mela", "banana", "ciliegia"]
print(frutti[0])  # mela
frutti.append("pera")
```

L’indice parte da 0. Le liste supportano slicing e molte operazioni:
```python
frutti[1]        # "banana"
frutti[-1]       # ultimo elemento
frutti[0:2]      # ["mela", "banana"]
len(frutti)      # lunghezza
"mela" in frutti  # True
```


## If / Else / Elif

Istruzioni condizionali:
```python
pressione = 145

if pressione >= 140:
    print("Grave rischio ipertensione!")
elif pressione >= 120:
    print("Rischio ipertensione.")
else:
    print("Pressione nella norma")
```

Python controlla le condizioni **dall'alto verso il basso** e si ferma al primo ramo vero. Quindi l'ordine conta.

---

## Cicli For
Il ciclo `for` serve a ripetere un blocco di codice per ogni elemento di una sequenza.
```python
for numero in [1, 2, 3]:
    print(numero)
```

Altri esempi comuni:
```python
# range(start, stop, step) genera sequenze di interi
for i in range(5):         # 0,1,2,3,4
    print(i)

for i in range(1, 6):      # 1..5
    print(i)

for i in range(0, 10, 2):  # 0,2,4,6,8
    print(i)

# enumerate per ottenere indice e valore
frutti = ["mela", "banana", "pera"]
for i, frutto in enumerate(frutti, start=1):
    print(f"{i}: {frutto}")
```

---

## Funzioni

Una **funzione** è un blocco di codice riutilizzabile: si definisce una volta, si chiama quante volte serve. Aiuta a evitare duplicazione e a dare un nome chiaro a un'operazione.
Puoi pensarla come a una mini-macchina: riceve input, fa un'elaborazione e opzionalmente restituisce un output.

Si definisce con `def`:
```python
def saluta(nome):
    print(f"Ciao {nome}!")

saluta("Anna")   # Ciao Anna!
saluta("Marco")  # Ciao Marco!
```

### `return`
Se la funzione deve restituire un valore al chiamante si usa `return`:
```python
def area_rettangolo(base, altezza):
    return base * altezza

a = area_rettangolo(3, 4)   # 12
```

Una funzione senza `return` restituisce implicitamente `None`.

> **Differenza importante**: `print()` stampa a schermo, `return` **restituisce** un valore al chiamante. Sono cose diverse.

### Parametri di default
Un parametro può avere un valore predefinito, usato se il chiamante non ne fornisce uno:
```python
def saluta(nome, saluto="Ciao"):
    print(f"{saluto} {nome}!")

saluta("Anna")              # Ciao Anna!
saluta("Marco", "Salve")    # Salve Marco!
```

### Argomenti keyword
Gli argomenti si possono passare anche specificandone il nome. Rende la chiamata più leggibile, utile quando i parametri sono molti:
```python
area_rettangolo(base=3, altezza=4)
```

### Restituire più valori
Python permette di restituire più valori separandoli con la virgola (tecnicamente è una tupla):
```python
def min_max(valori):
    return min(valori), max(valori)

m, M = min_max([3, 7, 1, 9, 4])   # m=1, M=9
```

### Scope delle variabili
Le variabili definite **dentro** una funzione sono locali: non esistono fuori da lì.
```python
def f():
    x = 10
    print(x)

f()
print(x)   # NameError: x non esiste qui
```

### Docstring
Buona pratica: documentare cosa fa la funzione con una stringa subito sotto `def`. La si legge con `help(nome_funzione)`.
```python
def area_cerchio(raggio):
    """Restituisce l'area di un cerchio dato il raggio."""
    return 3.14159 * raggio ** 2
```

### Esempio in ambito biomedico
```python
def bmi(peso_kg, altezza_m):
    """Calcola il Body Mass Index."""
    return peso_kg / altezza_m ** 2

def classifica_bmi(valore):
    if valore < 18.5:
        return "Sottopeso"
    elif valore < 25:
        return "Normopeso"
    elif valore < 30:
        return "Sovrappeso"
    else:
        return "Obesità"

indice = bmi(70, 1.75)
print(f"BMI: {indice:.1f} → {classifica_bmi(indice)}")
```

---

## PEP 8 e buone pratiche

- Indentazione: **4 spazi** per livello.  
- Massimo **79 caratteri** per riga.  
- Commenti max **72 caratteri**.  
- Lasciare righe vuote per separare le sezioni.  

Per consultare lo standard:
👉 [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

---

## Esercizi Pratici

### Problema 1 – Valutazione Rischio Paziente

Scrivi un programma in Python che simuli una semplice **valutazione di rischio** per un paziente.

Nota sulle risorse disponibili in questa lezione:
- Usa solo variabili, numeri, boolean, stringhe, `if/elif/else`, liste e `for` (se serve).
- Non è necessario usare `input()`: per questa prima versione imposta i valori direttamente in variabili.

Opzionale
- Se preferisci leggere i dati da tastiera, puoi usare `input()` (vedi sezione: "Input da tastiera (input())").

Consegna
- Dati i valori del paziente definiti come variabili:
  - `nome` (stringa), `eta` (intero), `pressione` (float, sistolica), `fumatore` (boolean: `True`/`False`).
- Stampa un messaggio di rischio in base a queste regole (semplificate):
  - Se `pressione >= 140` → "Grave rischio ipertensione!"
  - Altrimenti se `pressione >= 120` → "Rischio ipertensione."
  - Altrimenti se `eta >= 65` e `fumatore` è `True` → "Attenzione: fattori di rischio presenti."
  - Altrimenti → "Livello di rischio normale."
- Stampa un breve riepilogo finale con i valori del paziente in 4 righe (nome, età, pressione, fumatore).

Cosa puoi usare
- Operatori di confronto (`>`, `>=`, `<`, `<=`, `==`), operatori logici (`and`, `or`).
- `print()` e f-string per formattare l'output.

Scheletro di partenza
```python
# Dati del paziente (modifica i valori per provare casi diversi)
nome = "Anna"
eta = 68
pressione = 118.0
fumatore = True  # usa True/False

# TODO: scrivi qui la logica condizionale descritta in consegna
# Suggerimento: usa if / elif / else in questo ordine di priorità

# TODO: stampa il riepilogo in 4 righe
```

Variante con input() (opzionale)
```python
nome = input("Nome del paziente: ")
eta = int(input("Età del paziente: "))
pressione = float(input("Pressione sistolica: "))
fumatore = input("Il paziente è fumatore? (s/n): ").strip().lower() == "s"
```

Esempio di output atteso (per valori: eta=70, pressione=145.0, fumatore=True)
```
Grave rischio ipertensione!

Riepilogo:
Nome: Anna
Età: 70
Pressione: 145.0
Fumatore: True
```

---

### Problema 2 – Frequenze Cardiache

Calcola statistiche semplici sulle frequenze cardiache misurate ogni minuto.

Nota sulle risorse disponibili in questa lezione:
- Usa solo liste, cicli `for`, `if/elif/else`, `enumerate` (già visto), `len()`.
- Per esercizio, calcola la somma manualmente con un accumulatore; in soluzione è lecito usare anche `sum()`.
- Puoi provare anche una variante con `input()`; evita, per ora, le liste comprensione (versione compatta come extra).

Consegna
- Dato l'elenco `frequenze` qui sotto, per ciascun valore:
  - Stampa "Frequenza minuto X: Y bpm" (usa `enumerate` con `start=1`).
  - Se `bpm < 60` stampa "→ Frequenza troppo bassa" e incrementa `anomale`.
  - Se `bpm > 100` stampa "→ Frequenza eccessiva" e incrementa `anomale`.
  - Altrimenti stampa "→ Frequenza nella norma" e incrementa `normali`.
- Calcola la media manualmente: usa una variabile `somma = 0` e aggiungi `bpm` ad ogni iterazione, poi `media = somma / len(frequenze)` (gestisci anche il caso lista vuota: media 0).
- Alla fine stampa la media con 2 decimali e il conteggio di valori normali/anomali.

Scheletro di partenza
```python
# Frequenze cardiache acquisite ogni minuto
frequenze = [72, 78, 90, 65, 100, 88, 76, 80, 110, 95]

normali = 0
anomale = 0
somma = 0

for i, bpm in enumerate(frequenze, start=1):
    # TODO: stampa frequenza del minuto i
    # TODO: aggiorna normali/anomale in base alle regole
    # TODO: aggiorna la somma
    pass

media = somma / len(frequenze) if frequenze else 0
# In soluzione/alternativa: puoi usare anche sum(frequenze) al posto dell'accumulatore
# media = sum(frequenze) / len(frequenze) if frequenze else 0
print(f"\nMedia: {media:.2f} bpm")
print(f"Valori normali: {normali}, anomali: {anomale}")
```

Esempio di output finale (ultime 2 righe)
```
Media: 85.40 bpm
Valori normali: 8, anomali: 2
```

Variante con input() (senza liste comprensione)
```python
valori_input = input("Inserisci frequenze separate da virgola: ")

# Costruisci la lista di interi senza liste comprensione
frequenze = []
for tok in valori_input.split(','):
    t = tok.strip()
    if t:  # ignora vuoti
        frequenze.append(int(t))

normali = 0
anomale = 0
somma = 0

for i, bpm in enumerate(frequenze, start=1):
    print(f"Frequenza minuto {i}: {bpm} bpm")
    if bpm < 60:
        print("→ Frequenza troppo bassa")
        anomale += 1
    elif bpm > 100:
        print("→ Frequenza eccessiva")
        anomale += 1
    else:
        print("→ Frequenza nella norma")
        normali += 1
    somma += bpm

media = somma / len(frequenze) if frequenze else 0
print(f"\nMedia: {media:.2f} bpm")
print(f"Valori normali: {normali}, anomali: {anomale}")
```

Extra (facoltativo)
- Versione compatta con liste comprensione e `sum()` (verrà approfondita nelle prossime lezioni):
```python
frequenze = [int(x.strip()) for x in input("Inserisci frequenze separate da virgola: ").split(',') if x.strip()]
media = sum(frequenze) / len(frequenze) if frequenze else 0
```

---

### Problema 3 – BMI con funzione

Scrivi due funzioni per calcolare e classificare il BMI di un paziente.

Nota sulle risorse disponibili in questa lezione:
- Usa funzioni, `return`, `if/elif/else`, numeri e `print()`.
- Tieni separate le responsabilità: una funzione calcola il valore, l'altra lo interpreta.

Consegna
- Definisci `bmi(peso_kg, altezza_m)` che restituisce `peso_kg / altezza_m ** 2`.
- Definisci `classifica_bmi(valore)` che restituisce:
  - `"Sottopeso"` se `valore < 18.5`
  - `"Normopeso"` se `valore < 25`
  - `"Sovrappeso"` se `valore < 30`
  - `"Obesità"` altrimenti
- Usa poi le due funzioni con i valori `peso_kg = 70` e `altezza_m = 1.75`.
- Stampa il risultato con una cifra decimale e la classe finale.

Scheletro di partenza
```python
def bmi(peso_kg, altezza_m):
    # TODO: restituisci il BMI
    pass

def classifica_bmi(valore):
    # TODO: restituisci la classe corretta
    pass

peso_kg = 70
altezza_m = 1.75

indice = bmi(peso_kg, altezza_m)
print(f"BMI: {indice:.1f} → {classifica_bmi(indice)}")
```

Variante con input() (opzionale)
```python
peso_kg = float(input("Peso (kg): "))
altezza_m = float(input("Altezza (m): "))
```

Esempio di output atteso
```
BMI: 22.9 → Normopeso
```

---

## Culture Pill / Esterni
Piccoli approfondimenti:
- Esplora la **Zen of Python** con:
  ```python
  import this
  ```
- Comprendere la filosofia “chiara, leggibile, esplicita”.

---

## Soluzioni

Le soluzioni sono presentate separatamente dalle consegne. Dove indicato, includiamo varianti opzionali che usano `input()` o funzioni come `sum()`.

### Soluzione Problema 1

Versione con variabili impostate nel codice
```python
nome = "Anna"
eta = 68
pressione = 118.0
fumatore = True

if pressione >= 140:
    print("Grave rischio ipertensione!")
elif pressione >= 120:
    print("Rischio ipertensione.")
elif eta >= 65 and fumatore:
    print("Attenzione: fattori di rischio presenti.")
else:
    print("Livello di rischio normale.")

print("\nRiepilogo:")
print(f"Nome: {nome}")
print(f"Età: {eta}")
print(f"Pressione: {pressione}")
print(f"Fumatore: {fumatore}")
```

Variante con input() (opzionale)
```python
nome = input("Nome del paziente: ")
eta = int(input("Età del paziente: "))
pressione = float(input("Pressione sistolica: "))
fumatore = input("Il paziente è fumatore? (s/n): ").strip().lower() == "s"

if pressione >= 140:
    print("Grave rischio ipertensione!")
elif pressione >= 120:
    print("Rischio ipertensione.")
elif eta >= 65 and fumatore:
    print("Attenzione: fattori di rischio presenti.")
else:
    print("Livello di rischio normale.")

print("\nRiepilogo:")
print(f"Nome: {nome}")
print(f"Età: {eta}")
print(f"Pressione: {pressione}")
print(f"Fumatore: {fumatore}")
```

---

### Soluzione Problema 2

Versione con accumulatore (coerente con la consegna)
```python
frequenze = [72, 78, 90, 65, 100, 88, 76, 80, 110, 95]

normali = 0
anomale = 0
somma = 0

for i, bpm in enumerate(frequenze, start=1):
    print(f"Frequenza minuto {i}: {bpm} bpm")
    if bpm < 60:
        print("→ Frequenza troppo bassa")
        anomale += 1
    elif bpm > 100:
        print("→ Frequenza eccessiva")
        anomale += 1
    else:
        print("→ Frequenza nella norma")
        normali += 1
    somma += bpm

media = somma / len(frequenze) if frequenze else 0
print(f"\nMedia: {media:.2f} bpm")
print(f"Valori normali: {normali}, anomali: {anomale}")
```

Alternativa con sum()
```python
frequenze = [72, 78, 90, 65, 100, 88, 76, 80, 110, 95]

normali = 0
anomale = 0

for i, bpm in enumerate(frequenze, start=1):
    print(f"Frequenza minuto {i}: {bpm} bpm")
    if bpm < 60:
        print("→ Frequenza troppo bassa")
        anomale += 1
    elif bpm > 100:
        print("→ Frequenza eccessiva")
        anomale += 1
    else:
        print("→ Frequenza nella norma")
        normali += 1

media = sum(frequenze) / len(frequenze) if frequenze else 0
print(f"\nMedia: {media:.2f} bpm")
print(f"Valori normali: {normali}, anomali: {anomale}")
```

Variante con input() (senza liste comprensione)
```python
valori_input = input("Inserisci frequenze separate da virgola: ")

frequenze = []
for tok in valori_input.split(','):
    t = tok.strip()
    if t:
        frequenze.append(int(t))

normali = 0
anomale = 0
somma = 0

for i, bpm in enumerate(frequenze, start=1):
    print(f"Frequenza minuto {i}: {bpm} bpm")
    if bpm < 60:
        print("→ Frequenza troppo bassa")
        anomale += 1
    elif bpm > 100:
        print("→ Frequenza eccessiva")
        anomale += 1
    else:
        print("→ Frequenza nella norma")
        normali += 1
    somma += bpm

media = somma / len(frequenze) if frequenze else 0
print(f"\nMedia: {media:.2f} bpm")
print(f"Valori normali: {normali}, anomali: {anomale}")
```

---

### Soluzione Problema 3

Versione base
```python
def bmi(peso_kg, altezza_m):
    return peso_kg / altezza_m ** 2

def classifica_bmi(valore):
    if valore < 18.5:
        return "Sottopeso"
    elif valore < 25:
        return "Normopeso"
    elif valore < 30:
        return "Sovrappeso"
    else:
        return "Obesità"

peso_kg = 70
altezza_m = 1.75

indice = bmi(peso_kg, altezza_m)
print(f"BMI: {indice:.1f} → {classifica_bmi(indice)}")
```

Variante con input() (opzionale)
```python
def bmi(peso_kg, altezza_m):
    return peso_kg / altezza_m ** 2

def classifica_bmi(valore):
    if valore < 18.5:
        return "Sottopeso"
    elif valore < 25:
        return "Normopeso"
    elif valore < 30:
        return "Sovrappeso"
    else:
        return "Obesità"

peso_kg = float(input("Peso (kg): "))
altezza_m = float(input("Altezza (m): "))

indice = bmi(peso_kg, altezza_m)
print(f"BMI: {indice:.1f} → {classifica_bmi(indice)}")
```
