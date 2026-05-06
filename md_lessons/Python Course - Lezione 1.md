# Lezione 1 - Introduzione a Python, strumenti di lavoro e ambiente

## Indice
- [Lezione 1 - Introduzione a Python, strumenti di lavoro e ambiente](#lezione-1---introduzione-a-python-strumenti-di-lavoro-e-ambiente)
  - [Indice](#indice)
  - [Obiettivi della lezione](#obiettivi-della-lezione)
  - [Cos'e Python](#cose-python)
  - [Sistema operativo, file e cartelle](#sistema-operativo-file-e-cartelle)
    - [Percorsi assoluti e relativi](#percorsi-assoluti-e-relativi)
    - [Comandi essenziali](#comandi-essenziali)
  - [IDE](#ide)
  - [Jupyter Notebook](#jupyter-notebook)
  - [Ambienti virtuali](#ambienti-virtuali)
  - [Installazione e verifica degli strumenti](#installazione-e-verifica-degli-strumenti)
  - [Esercizi](#esercizi)
  - [Culture Pill / Esterni](#culture-pill--esterni)

---

## Obiettivi della lezione

Al termine della lezione:
- conoscere il ruolo di Python nel corso
- distinguere file, cartelle e percorsi
- sapere che cos'e un IDE
- avviare e usare Jupyter Notebook a livello base
- capire a cosa servono gli ambienti virtuali

---

## Cos'e Python

Python e un linguaggio di programmazione molto usato in:
- automazione
- analisi dati
- machine learning
- ricerca scientifica

Caratteristiche utili in questo corso:
- sintassi leggibile
- grande disponibilita di librerie
- buon supporto sia da terminale sia in notebook

Nel corso Python verra usato in tre modi principali:
- file `.py`
- terminale
- Jupyter Notebook

---

## Sistema operativo, file e cartelle

Un sistema operativo gestisce:
- programmi
- memoria
- file
- cartelle
- dispositivi

Quando si lavora con Python e importante capire dove si trovano i file e come raggiungerli.

Esempi di elementi comuni:
- file: `scatola.py`, `macedonia.txt`, `appunti.txt`
- cartelle: `python_course`, `md_lessons`, `lezione1_lab`

### Percorsi assoluti e relativi

Un percorso assoluto indica la posizione completa di un file o cartella.

Esempio:
```bash
/home/nome_utente/python_course
```

Un percorso relativo dipende dalla cartella corrente.

Esempi:
```bash
.          # cartella corrente
..         # cartella superiore
./file.py  # file nella cartella corrente
```

### Comandi essenziali

```bash
pwd
ls
cd nome_cartella
mkdir nuova_cartella
touch file.py
```

Significato:
- `pwd` mostra dove ci si trova
- `ls` mostra file e cartelle
- `cd` cambia cartella
- `mkdir` crea una cartella
- `touch` crea un file vuoto

---

## IDE

IDE significa `Integrated Development Environment`.

Un IDE aiuta a:
- scrivere codice
- eseguirlo
- organizzare i file
- usare strumenti aggiuntivi come terminale, estensioni e notebook

Nel corso viene usato **Visual Studio Code**.

Vantaggi pratici:
- supporto per Python
- integrazione con il terminale
- supporto per notebook Jupyter
- estensioni facili da installare

Per aprire una cartella in VS Code:
```bash
code .
```

---

## Jupyter Notebook

Jupyter Notebook permette di lavorare con:
- celle di codice
- celle di testo
- output immediato

E utile per:
- fare prove rapide
- spiegare passaggi con testo e codice insieme
- costruire piccoli esperimenti

Flusso tipico:
1. creare o aprire un notebook
2. scrivere codice in una cella
3. eseguire la cella
4. leggere l'output sotto la cella

Comando di avvio:
```bash
jupyter notebook
```

---

## Ambienti virtuali

Un ambiente virtuale isola i pacchetti Python di un progetto da quelli di altri progetti.

Questo evita conflitti tra versioni diverse delle librerie.

Creazione di un ambiente virtuale:
```bash
python3 -m venv .venv
```

Attivazione su Linux / macOS:
```bash
source .venv/bin/activate
```

Installazione di un pacchetto dentro l'ambiente attivo:
```bash
pip install notebook
```

Disattivazione:
```bash
deactivate
```

---

## Installazione e verifica degli strumenti

Guida di supporto:
- [Python Installation Guide.pdf](Python%20Installation%20Guide.pdf)

Comandi utili di verifica:
```bash
python3 -V
pip -V
jupyter notebook
```

Controlli pratici svolti:
- apertura di VS Code
- test del terminale
- attivazione di un ambiente virtuale
- installazione e avvio di Jupyter Notebook

---

## Esercizi

Gli esercizi della lezione 1 sono raccolti in:
- [Python Course - Lezione 1 - Esercizi.md](Python%20Course%20-%20Lezione%201%20-%20Esercizi.md)

Le soluzioni eseguibili sono raccolte in:
- `lesson_code/lezione_1/soluzioni/`

---

## Culture Pill / Esterni

Strumenti utili:
- documentazione ufficiale Python
- documentazione di VS Code
- guida Jupyter

Comando utile:
```bash
python3
```

Apre l'interprete interattivo di Python.
