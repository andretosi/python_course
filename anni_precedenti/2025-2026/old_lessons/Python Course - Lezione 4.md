# Lezione 4

Questa versione unisce i due materiali di Lezione 4 che erano finiti in punti diversi del repository. Tengo insieme le parti utili di entrambe: chiusura sui cicli, matrici fatte con liste, un richiamo sulle funzioni, dizionari, classi, esercizi e un recap veloce su `venv`.

## Argomenti
- Fine cicli: `while`, `break`, `continue`
- Matrici costruite con liste annidate
- Funzioni: richiamo rapido
- Dizionari
- Classi
- Esercizi su dizionari e classi
- Richiamo su `venv`

---

## Cicli Pt 2

Quando usare `while` rispetto a `for`:
- `for` esegue un blocco di codice su ogni elemento di un iterabile;
- `while` va avanti finché una certa condizione rimane vera.

`while` è utile quando non sai in anticipo quante iterazioni ti serviranno, ma sai qual è la condizione che deve rimanere vera.

### While

```python
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1
```

### Using flags

Un pattern molto comune è usare una variabile booleana per controllare quando fermarsi.

```python
active = True

while active:
    message = input("Scrivi qualcosa (quit per uscire): ")
    if message == "quit":
        active = False
    else:
        print(message)
```

### Break & Continue

`break` serve per uscire immediatamente dal loop:

```python
while True:
    message = input("Scrivi qualcosa (quit per uscire): ")
    if message == "quit":
        break
    else:
        print(message)
```

`continue` invece salta il resto del blocco corrente e torna all'inizio del loop.

```python
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
```

In questo esempio stampiamo solo i numeri dispari. `%` restituisce il resto della divisione intera.

> Sia `break` che `continue` funzionano sia nei `for` sia nei `while`.

---

## Matrici

Qui parliamo di matrici rappresentate con **liste annidate**. Non sono il modo più comodo o potente per fare algebra lineare seria, ma sono ottime per capire la struttura dei dati prima di passare a NumPy.

### Costruzione

```python
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(mat)
```

Output:
```python
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Selezionare un elemento

```python
print(mat[1][1])
```

Output:
```python
5
```

### Selezionare una riga

```python
print(mat[1])
```

Output:
```python
[4, 5, 6]
```

### Parte di una riga

```python
print(mat[1][0:2])
```

Output:
```python
[4, 5]
```

### Selezionare più righe

```python
print(mat[1:3])
```

Output:
```python
[[4, 5, 6], [7, 8, 9]]
```

### Selezionare una colonna

Con liste annidate normali, una colonna si estrae tipicamente con una list comprehension:

```python
column = [row[1] for row in mat]
print(column)
```

Output:
```python
[2, 5, 8]
```

> Nota importante: la sintassi `mat[:, 1]` **non** funziona con le liste Python normali. Quella è sintassi da NumPy.

### Parte di una colonna

```python
column = [row[1] for row in mat][1:3]
print(column)
```

Output:
```python
[5, 8]
```

### Selezionare più colonne

```python
columns = [row[1:3] for row in mat]
print(columns)
```

Output:
```python
[[2, 3], [5, 6], [8, 9]]
```

### Selezionare una sottomatrice

```python
submatrix = [row[1:3] for row in mat][1:3]
print(submatrix)
```

Output:
```python
[[5, 6], [8, 9]]
```

### Stampare una matrice in modo decente

```python
def print_matrix(matrix):
    """Stampa una matrice riga per riga."""
    for row in matrix:
        print(row)

print_matrix(mat)
```

Quando inizieremo a fare operazioni più serie tra matrici o array, useremo **NumPy**, che è molto più adatto.

---

## Funzioni

Questa è una sezione di richiamo rapido.

### Positional arguments

```python
def foo(arg1, arg2):
    print(arg1, arg2)
```

### Default positional arguments

```python
def foo(arg1, arg2="default_arg2"):
    print(arg1, arg2)
```

I parametri con valore di default vanno dopo quelli obbligatori.

### Keyword arguments

```python
def foo(arg1, arg2="default_arg2"):
    return f"{arg1} - {arg2}"

value = foo(arg2="ciao", arg1="mario")
print(value)
```

### Return values

```python
def area_rettangolo(base, altezza):
    return base * altezza
```

### Passare un numero arbitrario di argomenti: `*args`

```python
def make_pizza(tomato_sauce=True, mozzarella=True, *toppings):
    """Restituisce una lista con tutti gli ingredienti della pizza."""
    pizza = ["Pasta (farina, lievito, acqua, sale, olio)"]

    if tomato_sauce:
        pizza.append("sugo di pomodoro")
    if mozzarella:
        pizza.append("mozzarella")

    for topping in toppings:
        pizza.append(topping)

    return pizza

print(make_pizza(True, True, "peperoni", "olive"))
```

### Passare un numero arbitrario di coppie chiave-valore: `**kwargs`

```python
def build_profile(first_name, last_name, **user_info):
    user_info["first_name"] = first_name
    user_info["last_name"] = last_name
    return user_info

print(build_profile("Mario", "Rossi", ruolo="studente", eta=23))
```

### Store functions in modules

Un modulo è semplicemente un file `.py` con dentro funzioni, classi o costanti riutilizzabili.

```python
import pizza_utilities
import pizza_utilities as pz

pz.make_pizza()
```

Oppure:

```python
from pizza_utilities import make_pizza

make_pizza("peperoni", "olive", "melanzane")
```

`as` può essere usato sia per moduli sia per funzioni importate.

---

## Dizionari

In Python, i dizionari sono strutture dati che permettono di memorizzare coppie chiave-valore. Sono estremamente utili per rappresentare dati eterogenei, come record, configurazioni o risultati di misurazioni.

Caratteristiche principali:
- accesso rapido tramite chiave, non tramite indice;
- chiavi univoche;
- chiavi immutabili (stringhe, numeri, tuple);
- valori di qualsiasi tipo;
- struttura dinamica: puoi aggiungere, modificare o rimuovere elementi in ogni momento.

### Sintassi di base

```python
dizionario = {
    "chiave1": "valore1",
    "chiave2": "valore2",
}
```

### Accesso a un valore

```python
valore = dizionario["chiave1"]
```

### Esempio

```python
studente = {
    "nome": "Mario",
    "cognome": "Rossi",
    "esami_mancanti": ["Analisi 1", "Storia Medievale"],
}

print(type(studente))
print(studente["esami_mancanti"])
```

Output:
```python
<class 'dict'>
['Analisi 1', 'Storia Medievale']
```

### Aggiunta e modifica

```python
studente["codice_persona"] = 10890000
print(studente)
```

### Rimozione

```python
del studente["codice_persona"]
print(studente)
```

Oppure:

```python
valore_rimosso = studente.pop("codice_persona", None)
```

### Metodi utili

- `keys()` restituisce una vista delle chiavi
- `values()` restituisce una vista dei valori
- `items()` restituisce una vista delle coppie chiave-valore

```python
print(studente.keys())
print(studente.values())
print(studente.items())
```

Attenzione: `studente.keys()` non è una lista, ma si può convertire:

```python
chiavi = list(studente.keys())
print(type(chiavi))
```

---

## Classi

In Python, le **classi** sono il cuore della programmazione orientata agli oggetti (OOP), un approccio che consente di strutturare il codice in modo modulare, riutilizzabile e facilmente estendibile.

Una classe può essere vista come un **modello** per creare oggetti. Ogni oggetto creato da una classe è un'**istanza** e possiede:
- **attributi**: dati associati all'oggetto
- **metodi**: azioni che l'oggetto può compiere

### Dichiarazione di una classe

```python
class NomeClasse:
    def __init__(self, parametro1, parametro2):
        self.attributo1 = parametro1
        self.attributo2 = parametro2
```

### Esempio: una classe `Animal`

```python
class Animal:
    def __init__(self, sex, age, owner):
        self.sex = sex
        self.age = age
        self.owner = owner
```

Con `self.attributo = valore` stai dicendo che quell'attributo apparterrà all'istanza specifica che stai creando.

### Creazione di un oggetto

```python
tobia = Animal("male", 2, "Mario")
print(f"Tobia is a {tobia.age} years old pet whose owner is {tobia.owner}")
```

Output:
```python
Tobia is a 2 years old pet whose owner is Mario
```

### Creazione di un metodo

```python
class Animal:
    def __init__(self, sex, age, owner):
        self.sex = sex
        self.age = age
        self.owner = owner

    def eat(self, food):
        print(f"Mmm that was a nice {food}, do you want to try {self.owner}?")

tobia = Animal("male", 2, "Mario")
tobia.eat("chicken bone")
```

Output:
```python
Mmm that was a nice chicken bone, do you want to try Mario?
```

### Ereditarietà

L’ereditarietà consente di creare una nuova classe (**figlia**) che eredita attributi e metodi da una classe esistente (**genitore**).

```python
class Cat(Animal):
    def __init__(self, sex, age, owner, fur_color):
        super().__init__(sex, age, owner)
        self.fur_color = fur_color
```

Esempio completo:

```python
from time import sleep

class Animal:
    def __init__(self, sex, age, owner):
        self.sex = sex
        self.age = age
        self.owner = owner

    def eat(self, food):
        print(f"Mmm that was a nice {food}, do you want to try {self.owner}?")

class Cat(Animal):
    def __init__(self, sex, age, owner, fur_color):
        super().__init__(sex, age, owner)
        self.fur_color = fur_color

    def cat_sleep(self, duration):
        print("I'm falling asleep")
        sleep(duration)

duchessa = Cat("female", 4, "Adelaide Bonfamille", "white")
duchessa.cat_sleep(3)
duchessa.eat("fish")
```

### Overriding

Una sottoclasse può ridefinire un metodo ereditato:

```python
class Cat(Animal):
    def __init__(self, sex, age, owner, fur_color):
        super().__init__(sex, age, owner)
        self.fur_color = fur_color

    def eat(self, food):
        print(f"Mmm that was a nice {food}, so good there is no more to try {self.owner}!")
```

Questo si chiama **overriding**. È utile, ma va usato con criterio.

### Esempio di classe che non eredita tutto

```python
class Lion(Animal):
    def __init__(self, sex, age, fur_color):
        self.sex = sex
        self.age = age
        self.fur_color = fur_color

    def eat(self, food):
        print(f"Mmm that was a nice {food}")

mufasa = Lion("male", 6, "yellow")
mufasa.eat("gazelle")
```

Se poi provi a fare:

```python
print(mufasa.owner)
```

ottieni:

```python
AttributeError: 'Lion' object has no attribute 'owner'
```

Perché `owner` non è mai stato definito in quella classe.

---

## Esercizi su Dizionari e Classi

### Esercizio 1: Gestione Pazienti

Scrivi una funzione che crei un dizionario per rappresentare un paziente con i seguenti dati:
- `nome` (stringa)
- `eta` (intero)
- `parametri_vitali` (dizionario con chiavi: `"frequenza_cardiaca"`, `"pressione"`, `"saturazione"`)

Poi scrivi una funzione che stampi i parametri vitali del paziente.

### Soluzione 1

```python
def crea_paziente(nome, eta, parametri_vitali):
    paziente = {
        "nome": nome,
        "eta": eta,
        "parametri_vitali": parametri_vitali,
    }
    return paziente

def stampa_parametri(paziente):
    print(f"Parametri vitali di {paziente['nome']}:")
    for chiave, valore in paziente["parametri_vitali"].items():
        print(f"{chiave}: {valore}")

parametri1 = {
    "frequenza_cardiaca": 72,
    "pressione": "120/80",
    "saturazione": 98,
}

paziente1 = crea_paziente("Mario Rossi", 45, parametri1)
stampa_parametri(paziente1)
```

### Esercizio 2: Analisi Segnali ECG

Scrivi una funzione che crei un dizionario per rappresentare un segnale ECG con i seguenti dati:
- `id_paziente` (stringa)
- `durata` (float, in secondi)
- `valori` (dizionario con chiavi: `"tempo"`, `"ampiezza"`)

Poi scrivi una funzione che calcoli la frequenza cardiaca media in bpm del segnale, assumendo che ogni picco corrisponda a un battito.

```python
ecg_data = {
    "tempo": [0.1, 0.5, 0.9, 1.3, 1.7],
    "ampiezza": [1.2, 1.5, 1.3, 1.4, 1.6],
}
```

### Soluzione 2

```python
def crea_segnale_ecg(id_paziente, durata, valori):
    segnale = {
        "id_paziente": id_paziente,
        "durata": durata,
        "valori": valori,
    }
    return segnale

def calcola_frequenza_media(segnale):
    num_picchi = len(segnale["valori"]["ampiezza"])
    frequenza_bpm = (num_picchi / segnale["durata"]) * 60
    return round(frequenza_bpm, 2)

ecg_data = {
    "tempo": [0.1, 0.5, 0.9, 1.3, 1.7],
    "ampiezza": [1.2, 1.5, 1.3, 1.4, 1.6],
}

ecg = crea_segnale_ecg("PZ123", 2.0, ecg_data)
print(f"Frequenza media: {calcola_frequenza_media(ecg)} bpm")
```

Output:
```python
Frequenza media: 150.0 bpm
```

### Esercizio 3: Gestione Database Strumenti

Scrivi una classe `DatabaseStrumenti` che gestisca un inventario di strumenti biomedici. La classe deve avere:
- un attributo `strumenti` (dizionario con chiavi: `id_strumento`, valori: dizionario con `"nome"`, `"tipo"`, `"disponibile"`)
- un metodo `aggiungi_strumento(id, nome, tipo)`
- un metodo `presta_strumento(id)` che imposta `disponibile = False`
- un metodo `restituisci_strumento(id)` che imposta `disponibile = True`

Poi aggiungi i seguenti strumenti:
- `("S001", "Elettrocardiografo", "Diagnostico")`
- `("S002", "Sfigmomanometro", "Monitoraggio")`

Presta l'elettrocardiografo e stampa il database.

### Soluzione 3

```python
class DatabaseStrumenti:
    def __init__(self):
        self.strumenti = {}

    def aggiungi_strumento(self, id_strumento, nome, tipo):
        self.strumenti[id_strumento] = {
            "nome": nome,
            "tipo": tipo,
            "disponibile": True,
        }

    def presta_strumento(self, id_strumento):
        if id_strumento in self.strumenti:
            self.strumenti[id_strumento]["disponibile"] = False

    def restituisci_strumento(self, id_strumento):
        if id_strumento in self.strumenti:
            self.strumenti[id_strumento]["disponibile"] = True

db = DatabaseStrumenti()
db.aggiungi_strumento("S001", "Elettrocardiografo", "Diagnostico")
db.aggiungi_strumento("S002", "Sfigmomanometro", "Monitoraggio")
db.presta_strumento("S001")

print(db.strumenti)
```

Output:
```python
{
    'S001': {
        'nome': 'Elettrocardiografo',
        'tipo': 'Diagnostico',
        'disponibile': False
    },
    'S002': {
        'nome': 'Sfigmomanometro',
        'tipo': 'Monitoraggio',
        'disponibile': True
    }
}
```

---

## Richiamo su `venv`

`venv` lo abbiamo già visto meglio altrove, ma il succo è questo: serve a isolare i pacchetti di un progetto da quelli di un altro.

### Come si usa

1. Creare l'ambiente virtuale:
   ```bash
   python3 -m venv .venv
   ```
2. Attivarlo:
   ```bash
   source .venv/bin/activate
   ```
3. Disattivarlo:
   ```bash
   deactivate
   ```

In generale:
- la cartella del venv non va versionata;
- l'ambiente si può ricreare;
- conviene usare un venv per ogni progetto.
