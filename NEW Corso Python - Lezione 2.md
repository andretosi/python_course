# Corso Python – Lezione 2: Ambiente, Data Types, If/Else, Liste e Cicli For

## Indice
- [Prima di iniziare](#prima-di-iniziare)
- [Recap Lezione 1](#recap-lezione-1)
- [Ambienti Virtuali (venv)](#ambienti-virtuali-venv)
- [Python Basics](#python-basics)
  - [Commenti](#commenti)
  - [Variabili](#variabili)
  - [Data Types](#data-types)
    - [Boolean](#boolean)
    - [Stringhe](#stringhe)
    - [Numeri](#numeri)
    - [Liste](#liste)
    - [Tuple](#tuple)
    - [Set](#set)
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

### Quando usare altri linguaggi
- C/C++ → alte prestazioni, sistemi embedded.  
- MATLAB → analisi numerica o scientifica.  
- JavaScript → sviluppo web.  
- Java / Rust → software strutturato o ad alte prestazioni.  

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

---

### Numeri

#### Interi
```python
x = 5
y = 2
somma = x + y
```

#### Float
```python
z = 5.3
```

#### Operazioni miste
```python
risultato = 5 / 2     # float
intero = 5 // 2        # divisione intera
```

Costanti:
```python
MAX_SPEED = 300
```

Numeri leggibili:
```python
velocita_luce = 299_792_458
```

---

### Liste
Le **liste** sono collezioni ordinate e modificabili.

```python
frutti = ["mela", "banana", "ciliegia"]
print(frutti[0])  # mela
frutti.append("pera")
```

---

### Tuple
Le **tuple** sono simili alle liste ma **immutabili**.

```python
dimensioni = (100, 200)
```

---

### Set
I **set** sono collezioni **non ordinate** e **senza duplicati**.

```python
insieme = {"rosso", "verde", "blu"}
insieme.add("giallo")
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

---

## Culture Pill / Esterni
Piccoli approfondimenti:
- Esplora la **Zen of Python** con:
  ```python
  import this
  ```
- Comprendere la filosofia “chiara, leggibile, esplicita”.
