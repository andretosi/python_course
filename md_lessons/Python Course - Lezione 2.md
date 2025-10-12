# Corso Python – Lezione 2: Ambiente, Data Types, If/Else, Liste e Cicli For

## Indice
- [Corso Python – Lezione 2: Ambiente, Data Types, If/Else, Liste e Cicli For](#corso-python--lezione-2-ambiente-data-types-ifelse-liste-e-cicli-for)
  - [Indice](#indice)
  - [Prima di iniziare](#prima-di-iniziare)
    - [Regole sui percorsi](#regole-sui-percorsi)
  - [Recap Lezione 1](#recap-lezione-1)
    - [Cosa abbiamo fatto](#cosa-abbiamo-fatto)
    - [Quando usare altri linguaggi](#quando-usare-altri-linguaggi)
  - [Ambienti Virtuali (venv)](#ambienti-virtuali-venv)
    - [Cos’è un ambiente virtuale](#cosè-un-ambiente-virtuale)
    - [Comandi principali](#comandi-principali)
  - [Python Basics](#python-basics)
    - [Commenti](#commenti)
    - [Variabili](#variabili)
    - [Leggere gli errori](#leggere-gli-errori)
  - [Data Types](#data-types)
    - [Boolean](#boolean)
    - [Stringhe](#stringhe)
    - [Numeri](#numeri)
      - [Interi](#interi)
      - [Float](#float)
      - [Operazioni miste](#operazioni-miste)
    - [Liste](#liste)
    - [Tuple](#tuple)
    - [Dizionari](#dizionari)
  - [If / Else / Elif](#if--else--elif)
  - [Cicli For](#cicli-for)
  - [PEP 8 e buone pratiche](#pep-8-e-buone-pratiche)
  - [Esercizi Pratici](#esercizi-pratici)
    - [Problema 1 – Valutazione Rischio Paziente](#problema-1--valutazione-rischio-paziente)
    - [Problema 2 – Frequenze Cardiache](#problema-2--frequenze-cardiache)
  - [Culture Pill / Esterni](#culture-pill--esterni)

---

## Prima di iniziare

- Localizzare la cartella di lavoro.  
- Cancellare i file inutili.  
- Aprire **Visual Studio Code**.  
- Ricreare i file con **nomi senza spazi**.  
- Usare `print(f"...")` e non `printf()`.  
- Testare che Python funzioni correttamente.

### Regole sui percorsi
Usare solo lettere, numeri e trattini bassi o alti nei nomi di file e cartelle.  
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
- Perché usare Python:
  - Facile da imparare e molto diffuso.  
  - Ottimo per prototipare e per il Machine Learning.  
- Perché usare Linux:
  - Più leggero, efficiente e standard per i sistemi embedded, open-source.  
- Perché Visual Studio Code:
  - IDE moderno, ricco di estensioni e ampiamente supportato. Più linguaggi da poter usare contemporaneamente. 

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

## Ambienti Virtuali (venv)

### Cos’è un ambiente virtuale
Un **ambiente virtuale** permette di isolare le dipendenze di un progetto Python, evitando conflitti tra pacchetti e versioni.

### Comandi principali
1. Creare un ambiente:
   ```bash
   python3 -m venv myenv
   ```
2. Attivarlo:
   ```bash
   . myenv/bin/activate
   ```
3. Disattivarlo:
   ```bash
   deactivate
   ```

---

## Python Basics

### Commenti
```python
# Questo è un commento singolo

""" Questo è un commento
su più righe, utile per spiegazioni
o documentazione interna. """
```

Scrivere sempre commenti chiari per spiegare **perché** si fa qualcosa, non solo **cosa** si fa.

---

### Variabili

Le variabili possono contenere:
- lettere  
- numeri  
- trattini bassi `_`  

Non possono iniziare con un numero.

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

## Data Types

### Boolean
```python
vero = True
falso = False
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

---

### Tuple
Le **tuple** sono simili alle liste ma **immutabili**.

```python
dimensioni = (100, 200)
```

Le tuple sono definite dalla virgola e non possono essere modificate dopo la creazione:
```python
dimensioni = (100, 200)
# dimensioni[0] = 50  # TypeError
```
```

---

### Set
I **set** sono collezioni **non ordinate** e **senza duplicati**.

```python
insieme = {"rosso", "verde", "blu"}
insieme.add("giallo")
"rosso" in insieme   # True
```

Un set non mantiene l’ordine e non consente elementi mutabili al suo interno. Variante immutabile:
```python
fisso = frozenset({"a", "b"})
```

---

### Dizionari
Associazione chiave → valore.

```python
paziente = {
    "nome": "Luca",
    "eta": 35,
    "fumatore": False
}
print(paziente["nome"])
```

Metodi utili e accesso sicuro:
```python
paziente.get("peso", None)   # Restituisce None se assente
paziente.update({"eta": 36})
list(paziente.keys())   # chiavi
list(paziente.values()) # valori
list(paziente.items())  # coppie (chiave, valore)
```

---

## If / Else / Elif

Istruzioni condizionali:
```python
eta = 70
if eta > 65:
    print("Senior")
elif eta > 18:
    print("Adulto")
else:
    print("Minorenne")
```

---

## Cicli For
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

## PEP 8 e buone pratiche

- Indentazione: **4 spazi** per livello.  
- Massimo **79 caratteri** per riga.  
- Commenti max **72 caratteri**.  
- Lasciare righe vuote per separare le sezioni.  

Per consultare lo standard:
👉 [PEP 8 – Style Guide for Python Code](https://python.org/dev/peps/pep-0008)

---

## Esercizi Pratici

### Problema 1 – Valutazione Rischio Paziente

Scrivi un programma in Python che simuli una semplice **valutazione di rischio** per un paziente.

```python
# Input dati utente
nome = input("Nome del paziente: ")
eta = int(input("Età del paziente: "))
pressione = float(input("Pressione sistolica: "))
fumatore = input("Il paziente è fumatore? (s/n): ")

# Logica condizionale
if eta > 65 and pressione < 120 and fumatore == "s":
    print("Attenzione: rischio ipertensione.")
elif pressione > 120 and eta > 65:
    print("Grave rischio ipertensione!")
elif pressione > 120:
    print("Rischio ipertensione.")
else:
    print("Livello di rischio normale.")

# Riepilogo finale
print(f"\nRiepilogo:")
print(f"Nome: {nome}")
print(f"Età: {eta}")
print(f"Pressione: {pressione}")
print(f"Fumatore: {fumatore}")
```

---

### Problema 2 – Frequenze Cardiache

```python
# Frequenze cardiache acquisite ogni minuto
frequenze = [72, 78, 90, 65, 100, 88, 76, 80, 110, 95]

normali = 0
anomale = 0

for i, bpm in enumerate(frequenze):
    print(f"Frequenza minuto {i+1}: {bpm} bpm")
    if bpm < 60:
        print("→ Frequenza troppo bassa")
        anomale += 1
    elif bpm > 100:
        print("→ Frequenza eccessiva")
        anomale += 1
    else:
        print("→ Frequenza nella norma")
        normali += 1

media = sum(frequenze) / len(frequenze)
print(f"\nMedia: {media:.2f} bpm")
print(f"Valori normali: {normali}, anomali: {anomale}")
```

Variante: leggi i valori dall’utente, converti in lista e ripeti il calcolo.
Esempio di input: 72, 78, 90, 65, 100, 88, 76, 80, 110, 95

```python
valori_input = input("Inserisci frequenze separate da virgola: ")
# Pulisci spazi e converti in interi
frequenze = [int(x.strip()) for x in valori_input.split(',') if x.strip()]

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

---

## Culture Pill / Esterni
Piccoli approfondimenti:
- Esplora la **Zen of Python** con:
  ```python
  import this
  ```
- Comprendere la filosofia “chiara, leggibile, esplicita”.
