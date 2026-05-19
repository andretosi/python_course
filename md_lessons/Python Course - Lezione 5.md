# Lezione 5 - Ereditarieta e classi

## Indice
- [Lezione 5 - Ereditarieta e classi](#lezione-5---ereditarieta-e-classi)
  - [Prima di iniziare](#prima-di-iniziare)
  - [Obiettivi della lezione](#obiettivi-della-lezione)
  - [Struttura della lezione](#struttura-della-lezione)
  - [Ereditarieta](#ereditarieta)
    - [Classe generale e classe specifica](#classe-generale-e-classe-specifica)
    - [super()](#super)
    - [Metodi ereditati e metodi specializzati](#metodi-ereditati-e-metodi-specializzati)
  - [Felix come oggetto](#felix-come-oggetto)
  - [Oggetti in una lista](#oggetti-in-una-lista)
  - [Esercizi](#esercizi)
  - [Collegamento con la prossima lezione](#collegamento-con-la-prossima-lezione)

---

## Prima di iniziare

- Aprire la cartella di lavoro corretta in VS Code.
- Attivare l'ambiente virtuale se presente.
- Creare una cartella per la lezione, per esempio `lezione_5`.
- Tenere aperti un file `.py` e il terminale integrato.

Comandi utili:
```bash
pwd
ls
python3 nome_file.py
```

---

## Obiettivi della lezione

Al termine della lezione:
- riconoscere una classe generale e una classe specializzata
- usare l'ereditarieta con `class Figlia(ClasseBase)`
- usare `super().__init__(...)`
- distinguere metodi ereditati, metodi aggiunti e metodi ridefiniti
- rappresentare oggetti gia visti in aula, come Felix, con attributi e metodi
- lavorare con piu oggetti dentro una lista

---

## Struttura della lezione

1. Richiamo su classi, attributi, metodi e stato
2. Ereditarieta e `super()`
3. Metodi ereditati e metodi specializzati
4. Oggetti gia visti in aula: Felix, altri gatti e animali
5. Esercizi guidati

Argomenti della lezione:
- classi
- oggetti
- stato
- ereditarieta
- `super()`
- liste di oggetti

---

## Ereditarieta

L'ereditarieta permette di definire una classe generale e poi creare classi piu specifiche che riusano quella struttura.

Esempio:
- `Animale` contiene quello che vale per molti animali
- `Gatto` aggiunge quello che riguarda un gatto
- `Cane` aggiunge quello che riguarda un cane

Non serve usare ereditarieta sempre. Diventa utile quando piu classi condividono una parte comune.

### Classe generale e classe specifica

```python
class Animale:
    def __init__(self, nome, anni):
        self.nome = nome
        self.anni = anni

    def descrizione(self):
        return f"{self.nome}, {self.anni} anni"


class Gatto(Animale):
    def miagola(self):
        return f"{self.nome} dice: Meow"


felix = Gatto("Felix", 13)

print(felix.descrizione())
print(felix.miagola())
```

`Gatto` non definisce `descrizione()`, ma puo usarla perche la eredita da `Animale`.

### super()

Quando una classe specifica deve aggiungere attributi, puo chiamare il costruttore della classe base con `super()`.

```python
class Animale:
    def __init__(self, nome, anni):
        self.nome = nome
        self.anni = anni

    def descrizione(self):
        return f"{self.nome}, {self.anni} anni"


class Gatto(Animale):
    def __init__(self, nome, anni, colori):
        super().__init__(nome, anni)
        self.colori = colori

    def scheda(self):
        return f"{self.nome}: {', '.join(self.colori)}"


felix = Gatto("Felix", 13, ["bianco", "nero"])

print(felix.descrizione())
print(felix.scheda())
```

`super().__init__(nome, anni)` evita di riscrivere la parte comune.

### Metodi ereditati e metodi specializzati

Una classe figlia puo:
- usare metodi della classe base
- aggiungere nuovi metodi
- ridefinire un metodo con lo stesso nome

```python
class Animale:
    def __init__(self, nome, anni):
        self.nome = nome
        self.anni = anni

    def verso(self):
        return "verso generico"


class Gatto(Animale):
    def verso(self):
        return "meow"


class Cane(Animale):
    def verso(self):
        return "bau"


animali = [
    Gatto("Felix", 13),
    Cane("Bruno", 3),
]

for animale in animali:
    print(f"{animale.nome}: {animale.verso()}")
```

Qui `verso()` ha lo stesso nome, ma comportamento diverso in base all'oggetto.

---

## Felix come oggetto

In aula Felix e stato rappresentato prima con un dizionario:

```python
gatto = {
    "nome": "Felix",
    "anni": 13,
    "colore": ["Bianco", "Nero"],
}

print(gatto["nome"])
print(gatto["anni"])
```

La stessa informazione puo essere rappresentata con una classe:

```python
class Gatto:
    def __init__(self, nome, anni, colori):
        self.nome = nome
        self.anni = anni
        self.colori = colori

    def miagola(self):
        return f"{self.nome} dice: Meow"

    def compie_anni(self):
        self.anni += 1


felix = Gatto("Felix", 13, ["bianco", "nero"])
sky = Gatto("Sky", 10, ["nero"])

print(felix.miagola())
print(sky.anni)

sky.compie_anni()
print(sky.anni)
```

Il dizionario tiene insieme dati. La classe tiene insieme dati e comportamenti.

---

## Oggetti in una lista

Una lista puo contenere oggetti. Questo permette di ripetere la stessa operazione su elementi diversi.

```python
class Animale:
    def __init__(self, nome, anni):
        self.nome = nome
        self.anni = anni

    def descrizione(self):
        return f"{self.nome}, {self.anni} anni"


class Gatto(Animale):
    def __init__(self, nome, anni, colori):
        super().__init__(nome, anni)
        self.colori = colori

    def verso(self):
        return "meow"

    def scheda(self):
        return f"{self.nome}: {', '.join(self.colori)}"


class Cane(Animale):
    def verso(self):
        return "bau"


animali = [
    Gatto("Felix", 13, ["bianco", "nero"]),
    Cane("Bruno", 3),
]

for animale in animali:
    print(animale.descrizione())
    print(f"{animale.nome}: {animale.verso()}")

felix = animali[0]
print(felix.scheda())
```

Questo modo di scrivere prepara anche alla lettura di librerie come PyTorch, dove molti componenti sono oggetti con attributi e metodi.

---

## Esercizi

Gli esercizi della lezione 5 sono raccolti in:
- [Python Course - Lezione 5 - Esercizi.md](Python%20Course%20-%20Lezione%205%20-%20Esercizi.md)

Le soluzioni eseguibili sono raccolte in:
- `lesson_code/lezione_5/soluzioni/`

Gli esempi eseguibili sono raccolti in:
- `lesson_code/lezione_5/esempi/`

---

## Collegamento con la prossima lezione

La prossima lezione introduce NumPy e Matplotlib usando immagini.

Una foto digitale puo essere letta come una tabella di numeri. Questo collega direttamente:
- liste e indici
- tabelle e matrici
- immagini
- dati usati nei primi esempi di machine learning
