---
Deadline: 2025-05-31
Status: done
tags:
  - project
Links: "[[Projects]]"
Areas:
  - "[[Programming]]"
  - "[[University]]"
Resources: My knowledge, Python crash course 2nd edition - Eric Matthes, Python Documentation, other websites
---


# Related Resources
```dataview
list
from #resource 
where contains(file.inlinks, this.file.link)
OR contains(file.outlinks, this.file.link)
AND file.name != this.file.name
sort file.name asc
```
- [[OReilly.Head.First.Python.A.Brain-Friendly.Guide.2nd.Edition.www.EBooksWorld.ir_compressed.pdf]]
# Cosa fare prima
- Spegnere luci sul proiettore
- cambiare colori terminale per avere sfondo bianco `ctrl + shift + P -> colori`
- scrivere comandi per mac e per windows alla lavagna:
	- installare cose
	- aprire visual studio code nella cartella corrente

# Materiale

- https://docs.python.org/3/tutorial/index.html

Cosa fare con quelli del corso precedente:
- Strutturare il corso in moduli:
	- non consigliato
	- consigliato
	- obbligatorio

## Reti Neurali
[[Reti Neurali]]
# Lezioni

### Programma x Argomenti:

Setup e Intro (2 Lez):
- Installazione WSL per chi ha windows
- Perchè Linux
- Visual Studio
- Introduzione a Python
- Venv

Python (3 Lez):
- Python Basics
- Data Types
- PEP 8
- Operazioni Logiche
- If/else
- Cicli
	- Matrici fatte con le liste
- Funzioni
- Classi
- Error Handling

Librerie (2 Lez):
- Numpy
- MatplotLib
- Pandas
- Pytorch

Progetto (2 Lez):
- Pytorch

Extra:
- Presetnazione Librerie Biomediche
- Esterno/i che parla di come ha usato python nel suo lavoro biomedico

### Programma x Lezioni
Sarò un po' come Amadeus, se sforiamo di 15/20 min chissene ma si tenta di stare nei tempi.

Problemi:
- preparo il testo
- preparo la soluzione GIA pronta
- Durante lo svolgimento si va in giro a rispondere alle domande
- 

**Lezione 1 +1h Extra (19/03)**
[[Lezione 1 - Python Course]]
- Installazione WSL per chi ha windows (1h)
- **INZIO**
- Spiegazione Struttura Corso+ Progetto finale pytorch
- Perchè Linux
- Installazione e Aggiornamento Terminali (Ubuntu e MAC)
	- Installare e Aggiornare Pacchetti
- Comandi Terminali
	- Comandi Semplici
	- Nano Editor
	- Editare un file, estensioni, aprire una cartella
- *Problema: Creare un file, navigare in una directory, eseguire un file*
- Visual Studio
- Introduzione a Python
- Python da Terminale
- Guest?
- Culture Pill/esterni
	- Zen of Python

**Lezione 2 (26/03)**
[[Lezione 2 - Python Course]]
- Data Types 1 e relativi metodi (Test su Python da Terminale):
	- Booleans
	- Integers
	- Floats
	- Stringhe 
- If/else/elif
	- Esempi e Programmi Semplici con if else e stringhe
- *Problema: Variabili Booleane, Intere, Float, Stringhe ed If/Else*
- Data Types 2 e relativi metodi:
	- Liste
- For Loops
- *Problema: Liste e Cicli For*
- Culture Pill/esterni

**Lezione 3 (2/04)**
- Data Types 3
	- Matrici fatte con le liste
- Funzioni 1
	- Intro Funzioni
	- Esempio di creazione di una funzione che stampa una matrice fatta bene
- *Problema: Matrici e Funzioni*
- While loops
- *Problema: Cicli While*
- Data Types 4:
	- Dizionari
	- Tuple
	- Set
	- Altri
	- Esempi
- *Problema: Dizionari e Tuple*
- Culture Pill/esterni

**GitHub Forse (16/04)**
- ...

**Lezione 4 (23/04)**
- Funzioni 2
	- Argomenti avanzati sulle funzioni
- *Problema: Funzioni Avanzate*
- Classi 1
- Ambienti Virtuali
	- Venv
- numpy
	- altro
	- esempi di come usare numpy e di come questo si collega alle Classi
- *Problema: Numpy (con uso classi numpy)*
- Culture Pill/esterni

**Lezione 5 (30/04)**
- Classi 2
	- Costruire una propria classe
	- Argomenti avanzati sulle classi
- *Problema: Classi*
- Error Handling
- File esterni
	- Leggere un file
	- Scrivere un file
- *Problema: Error Handling e File Esterni*
- Creare una Libreria
- *Problema: Programma Completo con Funzioni, Classi, Error Handling e Libreria*
- Culture Pill/esterni


**DECIDERE PROGETTO COSA FARE E MODIFICARE PROSSIME LEZIONI DI CONSEGUENZA**

**Lezione 6 (7/05) (data Analysis 101)** 
- Pandas
	- ...
	- Esempi
- Matplotlib
	- ...
	- Esempi
- *Problema: Visualizzare i Dati con Pandas e Matplotlib*
- Numpy 2
- *Problema: Visualizzare ed Elaborare Dati con Numpy Pandas e MatplotlIb*
- Culture Pill/esterni

**Lezione 7 (14/05)**
- Jupyter Notebook
- PyTorch
- Culture Pill/esterni

**Lezione 8 (21/05)**
- Progetto
- Culture Pill/esterni

**Lezione 9 (28/05)**
- Progetto
- Culture Pill/esterni
- Saluti

**Extra:**
- Presetnazione Librerie Biomediche
- Esterno/i che parla di come ha usato python nel suo lavoro biomedico

**Clutlutre Pill Ideas**
- Lezione sui meme dei python
### Lezioni Vecchie:

- [[Programming Tools and Python Installation Guide]]
- [[Python Course - Lezione 1]]
- [[Python Course - Lezione 2]]
- [[Python Course - Lezione 3]]
- [[Python Course - Lezione 4]]
- [[Python Course - Lezione 5]]

# Migliorare

https://beaproposals.notion.site/Errors-and-Future-improvements-1406b991937580dea3c6c34e903f5b03?pvs=4
## Possibili soluzioni

- Le domande aperte sono state poste troppo spesso, creando silenzi imbarazzanti. Per mantenere l’attenzione, sarebbe meglio:
    - alternarle con *domande chiuse* (es. "Chi di voi ha già usato Python prima? Alzate la mano o scrivete 'sì' in chat").
    - alternare *istruzioni chiare pratiche (creare micro-attività interattive)*
        
        *→ Creare momenti di verifica collettiva e test delle cose viste*
        
    - *domande aperte strutturate* che guidino la discussione (es. "Quali problemi avete riscontrato durante l’installazione di WSL?").
    - *Utilizzare sondaggi rapidi o quiz*
    - *Usare pause attive* (inserire pause di 1-2 minuti con un’attività semplice, come: "Prendetevi un minuto per scrivere una riga di codice con ciò che abbiamo appena appreso".)
    - *Stimolare la curiosità con esempi pratici*
## Problemi