# Lezione 2 - Variabili, numeri, booleani, condizioni e liste

## Indice
- [Lezione 2 - Variabili, numeri, booleani, condizioni e liste](#lezione-2---variabili-numeri-booleani-condizioni-e-liste)
  - [Indice](#indice)
  - [Prima di iniziare](#prima-di-iniziare)
    - [Regole sui percorsi](#regole-sui-percorsi)
  - [Recap lezione 1](#recap-lezione-1)
  - [Obiettivi della lezione](#obiettivi-della-lezione)
  - [Variabili](#variabili)
  - [Numeri](#numeri)
    - [Interi e float](#interi-e-float)
    - [Operazioni utili](#operazioni-utili)
  - [Booleani](#booleani)
  - [If / Else](#if--else)
  - [Liste](#liste)
    - [Creazione e accesso](#creazione-e-accesso)
    - [Operazioni di base](#operazioni-di-base)
  - [Esercizi](#esercizi)
  - [Culture Pill / Esterni](#culture-pill--esterni)

---

## Prima di iniziare

- Aprire la cartella di lavoro corretta.
- Aprire **Visual Studio Code**.
- Attivare l'ambiente virtuale se presente.
- Verificare che `python3` funzioni da terminale.

### Regole sui percorsi

Usare solo lettere, numeri, `_` e `-` nei nomi di file e cartelle quando possibile.

Esempi utili:
```bash
pwd
ls
code .
```

---

## Recap lezione 1

Nella lezione precedente sono stati introdotti:
- Python e il suo ruolo nel corso
- sistema operativo, file e cartelle
- IDE
- Jupyter Notebook
- ambienti virtuali

Questa lezione passa ai primi elementi del linguaggio.

---

## Obiettivi della lezione

Al termine della lezione:
- creare e aggiornare variabili
- usare numeri interi e decimali
- capire espressioni booleane semplici
- scrivere condizioni con `if / else`
- creare e manipolare liste a livello base

---

## Variabili

Una variabile e un nome associato a un valore.

```python
nome = "Milo"
anni = 4
colore = "grigio"
```

Regole pratiche:
- i nomi possono contenere lettere, numeri e `_`
- non possono iniziare con un numero
- e meglio usare nomi chiari

Esempi:
```python
nome_gatto = "Milo"
numero_limoni = 5
```

---

## Numeri

### Interi e float

```python
numero_limoni = 5      # int
altezza_sedia = 0.8   # float
```

### Operazioni utili

```python
x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)
```

Significato:
- `/` divisione normale
- `//` divisione intera
- `%` resto
- `**` potenza

---

## Booleani

I booleani hanno solo due valori:

```python
vero = True
falso = False
```

Nascono spesso da confronti:

```python
anni_gatto = 4

print(anni_gatto >= 2)
print(anni_gatto < 2)
```

Altri esempi:
```python
numero_limoni = 5
print(numero_limoni > 3)
print(numero_limoni == 5)
```

---

## If / Else

Le condizioni permettono di eseguire codice diverso a seconda del caso.

```python
numero_limoni = 5

if numero_limoni >= 4:
    print("Abbastanza limoni")
else:
    print("Pochi limoni")
```

Esempio con booleano:

```python
sedia_verde = True

if sedia_verde:
    print("Sedia verde")
else:
    print("Sedia non verde")
```

---

## Liste

Le liste sono collezioni ordinate e modificabili.

```python
macedonia = ["Anna", "Luca", "Marco"]
print(macedonia)
```

### Creazione e accesso

```python
macedonia = ["Anna", "Luca", "Marco"]

print(macedonia[0])
print(macedonia[1])
print(macedonia[-1])
```

### Operazioni di base

```python
macedonia = ["Anna", "Luca", "Marco"]

macedonia.append("Nina")
print(macedonia)

print(len(macedonia))
print("Luca" in macedonia)
```

Operazioni usate:
- `append()` aggiunge un elemento
- `len()` restituisce il numero di elementi
- `in` verifica la presenza di un valore

---

## Esercizi

Gli esercizi della lezione 2 sono raccolti in:
- [Python Course - Lezione 2 - Esercizi.md](Python%20Course%20-%20Lezione%202%20-%20Esercizi.md)

Le soluzioni eseguibili sono raccolte in:
- `lesson_code/lezione_2/soluzioni/`

---

## Culture Pill / Esterni

Comandi utili gia da ora:

```python
print(type(10))
print(type(0.8))
print(type(True))
print(type(["Anna", "Luca", "Marco"]))
```
