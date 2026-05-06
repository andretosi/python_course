# Lezione 4 - Dizionari, errori, file di testo e classi

## Indice
- [Lezione 4 - Dizionari, errori, file di testo e classi](#lezione-4---dizionari-errori-file-di-testo-e-classi)
  - [Indice](#indice)
  - [Prima di iniziare](#prima-di-iniziare)
  - [Recap](#recap)
  - [Obiettivi della lezione](#obiettivi-della-lezione)
  - [Struttura della lezione \(2 ore\)](#struttura-della-lezione-2-ore)
  - [Dizionari: il minimo indispensabile](#dizionari-il-minimo-indispensabile)
    - [Creazione, accesso e modifica](#creazione-accesso-e-modifica)
    - [Dizionari annidati](#dizionari-annidati)
  - [Leggere gli errori](#leggere-gli-errori)
    - [try / except](#try--except)
  - [File di testo](#file-di-testo)
  - [Perche usare una classe](#perche-usare-una-classe)
  - [Prima classe](#prima-classe)
    - [Classe, istanza, attributo](#classe-istanza-attributo)
    - [self](#self)
  - [Metodi](#metodi)
    - [Metodi che restituiscono valori](#metodi-che-restituiscono-valori)
    - [Metodi che modificano lo stato](#metodi-che-modificano-lo-stato)
    - [__str__](#__str__)
  - [Liste di oggetti](#liste-di-oggetti)
  - [Una classe che contiene altri oggetti](#una-classe-che-contiene-altri-oggetti)
  - [Ereditarieta: una prima idea](#ereditarieta-una-prima-idea)
  - [Errori comuni con le classi](#errori-comuni-con-le-classi)
  - [Esercizi](#esercizi)
  - [Collegamento con le prossime lezioni](#collegamento-con-le-prossime-lezioni)

---

## Prima di iniziare

- Aprire la cartella di lavoro corretta in VS Code.
- Attivare l'ambiente virtuale se presente.
- Creare una cartella per la lezione, per esempio `lezione_4`.
- Tenere aperti un file `.py` e il terminale integrato.

Comandi utili:
```bash
pwd
ls
python3 nome_file.py
```

---

## Recap

Nelle lezioni precedenti sono stati introdotti:
- variabili, numeri e booleani
- `if / else`
- liste
- stringhe
- cicli `for` e `while`
- `input()`
- funzioni
- `import` di base

Questa lezione completa rapidamente tre strumenti rimasti aperti, cioe dizionari, lettura degli errori e file di testo. La parte principale della lezione e dedicata alle classi.

---

## Obiettivi della lezione

Al termine della lezione:
- creare e leggere dizionari semplici
- usare dizionari annidati per rappresentare dati strutturati
- interpretare gli errori Python piu comuni
- scrivere e leggere un file di testo semplice
- definire una classe con `__init__`
- creare istanze di una classe
- distinguere attributi e metodi
- usare `self`
- scrivere metodi che restituiscono valori e metodi che modificano lo stato
- usare liste di oggetti
- riconoscere una prima forma di ereditarieta

---

## Struttura della lezione (2 ore)

1. Recap e setup - 5 min
2. Dizionari - 15 min
3. Errori e `try / except` - 10 min
4. File di testo - 10 min
5. Classi: idea, sintassi, istanze - 30 min
6. Metodi e stato dell'oggetto - 20 min
7. Liste di oggetti e registri - 15 min
8. Ereditarieta essenziale - 10 min
9. Esercizi guidati - 5 min

Argomenti della lezione:
- dizionari
- errori
- file di testo
- classi
- attributi
- metodi
- oggetti
- ereditarieta di base

---

## Dizionari: il minimo indispensabile

Un dizionario memorizza coppie `chiave: valore`.

Rispetto a una lista:
- una lista usa indici numerici: `macedonia[0]`
- un dizionario usa chiavi descrittive: `gatto["nome"]`

### Creazione, accesso e modifica

```python
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
```

`items()` permette di attraversare insieme chiavi e valori.

Per leggere una chiave che potrebbe non esistere si puo usare `.get()`:

```python
stanza = gatto.get("stanza", "non assegnata")
print(stanza)
```

### Dizionari annidati

Un valore puo essere un altro dizionario.

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

print(scatola["contenuto"]["secondo"])
```

I dizionari sono utili quando un elemento deve tenere insieme piu informazioni diverse.

---

## Leggere gli errori

Quando Python mostra un errore, la parte piu importante e spesso l'ultima riga.

Esempio:

```python
numero = int("venti")
```

Errore:
```python
ValueError: invalid literal for int() with base 10: 'venti'
```

Significa che Python non riesce a convertire la stringa `"venti"` in un numero intero.

Errori comuni:
- `NameError`: nome non definito
- `TypeError`: operazione usata con un tipo sbagliato
- `ValueError`: valore non convertibile o non valido
- `IndexError`: indice fuori da una lista
- `KeyError`: chiave non presente in un dizionario
- `FileNotFoundError`: file non trovato
- `AttributeError`: attributo o metodo non presente in un oggetto

### try / except

`try / except` permette di gestire un errore previsto.

```python
testo = "venti"

try:
    numero = int(testo)
    print(f"Numero: {numero}")
except ValueError:
    print("Numero non valido")
```

Usare `try / except` non significa nascondere tutti gli errori. Conviene intercettare errori specifici, come `ValueError` o `FileNotFoundError`.

---

## File di testo

Un file di testo puo essere scritto e letto con `open()`.

```python
macedonia = ["Anna", "Luca", "Marco"]

with open("macedonia.txt", "w", encoding="utf-8") as file:
    for nome in macedonia:
        file.write(nome + "\n")

with open("macedonia.txt", "r", encoding="utf-8") as file:
    contenuto = file.read()

print(contenuto)
```

Modalita comuni:
- `"w"` scrive e sovrascrive il file
- `"a"` aggiunge in fondo al file
- `"r"` legge il file

Il blocco `with` chiude il file automaticamente anche se il codice incontra un errore.

---

## Perche usare una classe

Finora abbiamo rappresentato dati con variabili, liste e dizionari.

Esempio con dizionario:

```python
gatto = {
    "nome": "Milo",
    "anni": 4,
    "colore": "grigio",
}

def descrizione_gatto(gatto):
    return f"{gatto['nome']}, anni {gatto['anni']}, {gatto['colore']}"
```

Funziona. Pero, quando il programma cresce, dati e funzioni collegate tendono a sparpagliarsi.

Una classe permette di mettere insieme:
- i dati di una cosa
- le operazioni che hanno senso su quella cosa

Una classe non e obbligatoria per ogni problema. Diventa utile quando una struttura dati ha comportamento, regole e molte istanze simili.

---

## Prima classe

Una classe e un modello. Un oggetto e un elemento concreto creato da quel modello.

```python
class Gatto:
    def __init__(self, nome, anni, colore):
        self.nome = nome
        self.anni = anni
        self.colore = colore


gatto_1 = Gatto("Milo", 4, "grigio")
gatto_2 = Gatto("Nina", 1, "nero")

print(gatto_1.nome)
print(gatto_2.colore)
```

### Classe, istanza, attributo

In questo esempio:
- `Gatto` e la classe
- `gatto_1` e `gatto_2` sono istanze
- `nome`, `anni` e `colore` sono attributi

Ogni istanza ha i propri valori.

```python
print(gatto_1.nome)
print(gatto_2.nome)
```

### self

`self` rappresenta l'oggetto specifico su cui stiamo lavorando.

```python
self.nome = nome
```

Significa: salva il valore del parametro `nome` dentro l'attributo `nome` di questo oggetto.

Quando chiamiamo:

```python
gatto_1 = Gatto("Milo", 4, "grigio")
```

Python passa automaticamente l'oggetto in costruzione come `self`.

---

## Metodi

Un metodo e una funzione definita dentro una classe.

```python
class Gatto:
    def __init__(self, nome, anni, colore):
        self.nome = nome
        self.anni = anni
        self.colore = colore

    def descrizione(self):
        return f"{self.nome}, anni {self.anni}, {self.colore}"


gatto = Gatto("Milo", 4, "grigio")
print(gatto.descrizione())
```

Il metodo usa `self` per leggere gli attributi dell'oggetto.

### Metodi che restituiscono valori

```python
class Gatto:
    def __init__(self, nome, anni, colore):
        self.nome = nome
        self.anni = anni
        self.colore = colore

    def adulto(self):
        return self.anni >= 2


gatto = Gatto("Nina", 1, "nero")
print(gatto.adulto())
```

Un metodo puo restituire un booleano, un numero, una stringa, una lista o qualsiasi altro tipo.

### Metodi che modificano lo stato

Lo stato di un oggetto e l'insieme dei valori dei suoi attributi.

```python
class Gatto:
    def __init__(self, nome, anni, colore):
        self.nome = nome
        self.anni = anni
        self.colore = colore

    def compie_anni(self):
        self.anni += 1

    def adulto(self):
        return self.anni >= 2


gatto = Gatto("Nina", 1, "nero")
print(gatto.adulto())

gatto.compie_anni()
print(gatto.adulto())
```

Prima `adulto()` restituisce `False`, poi l'oggetto cambia stato.

### __str__

`__str__` definisce come rappresentare un oggetto quando viene stampato.

```python
class Gatto:
    def __init__(self, nome, anni, colore):
        self.nome = nome
        self.anni = anni
        self.colore = colore

    def __str__(self):
        return f"{self.nome} ({self.colore})"


gatto = Gatto("Milo", 4, "grigio")
print(gatto)
```

Senza `__str__`, Python stampa una rappresentazione tecnica dell'oggetto.

---

## Liste di oggetti

Gli oggetti possono stare dentro una lista.

```python
class Gatto:
    def __init__(self, nome, anni, colore):
        self.nome = nome
        self.anni = anni
        self.colore = colore

    def adulto(self):
        return self.anni >= 2


gatti = [
    Gatto("Milo", 4, "grigio"),
    Gatto("Nina", 1, "nero"),
    Gatto("Otto", 4, "bianco"),
]

for gatto in gatti:
    if gatto.adulto():
        print(f"{gatto.nome}: adulto")
```

Questa struttura e utile quando si hanno molti elementi dello stesso tipo.

---

## Una classe che contiene altri oggetti

Una classe puo contenere una lista di oggetti.

```python
class Gatto:
    def __init__(self, nome, anni, colore):
        self.nome = nome
        self.anni = anni
        self.colore = colore

    def adulto(self):
        return self.anni >= 2


class RegistroGatti:
    def __init__(self):
        self.gatti = []

    def aggiungi(self, gatto):
        self.gatti.append(gatto)

    def conta_adulti(self):
        totale = 0

        for gatto in self.gatti:
            if gatto.adulto():
                totale += 1

        return totale


registro = RegistroGatti()
registro.aggiungi(Gatto("Milo", 4, "grigio"))
registro.aggiungi(Gatto("Nina", 1, "nero"))

print(registro.conta_adulti())
```

Qui `RegistroGatti` non sostituisce `Gatto`: li organizza.

---

## Ereditarieta: una prima idea

L'ereditarieta permette di creare una classe specializzata a partire da una classe piu generale.

```python
class Animale:
    def __init__(self, nome, anni):
        self.nome = nome
        self.anni = anni

    def descrizione(self):
        return f"{self.nome}, {self.anni} anni"


class Cane(Animale):
    def __init__(self, nome, anni, colore):
        super().__init__(nome, anni)
        self.colore = colore

    def scheda(self):
        return f"{self.nome}: {self.colore}"


cane = Cane("Bruno", 3, "marrone")

print(cane.descrizione())
print(cane.scheda())
```

In questo esempio:
- `Animale` contiene la parte comune
- `Cane` riusa quella parte con `super()`
- `Cane` aggiunge un attributo e un metodo specifici

Per ora basta riconoscere la struttura. Nelle prossime lezioni questo schema tornera quando si useranno classi gia definite da librerie esterne.

---

## Errori comuni con le classi

### Dimenticare `self`

```python
class Gatto:
    def descrizione():
        return "gatto"
```

Il metodo dovrebbe ricevere `self`:

```python
class Gatto:
    def descrizione(self):
        return "gatto"
```

### Confondere classe e istanza

```python
Gatto.nome
```

`nome` appartiene a una istanza, quindi:

```python
gatto = Gatto("Milo", 4, "grigio")
print(gatto.nome)
```

### Scrivere un attributo con un nome diverso

```python
self.colore = colore
print(gatto.colori)
```

Questo produce un `AttributeError`, perche `colori` non esiste.

---

## Esercizi

Gli esercizi della lezione 4 sono raccolti in:
- [Python Course - Lezione 4 - Esercizi.md](Python%20Course%20-%20Lezione%204%20-%20Esercizi.md)

Le soluzioni eseguibili sono raccolte in:
- `lesson_code/lezione_4/soluzioni/`

Gli esempi eseguibili sono raccolti in:
- `lesson_code/lezione_4/esempi/`

---

## Collegamento con le prossime lezioni

Le classi sono importanti anche per le librerie scientifiche.

In PyTorch, per esempio, molti componenti sono oggetti:
- tensori
- dataset
- modelli
- funzioni di loss
- ottimizzatori

Quando verra definita una rete neurale, la sintassi delle classi rendera piu chiaro cosa succede dentro il modello.
