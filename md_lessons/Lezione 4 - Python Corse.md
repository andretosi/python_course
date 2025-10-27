1. Dizionari (fine)
2. Classi
3. Esercizi su Dizionari e CLassi

---
# Dizionari (fine)
In Python, i dizionari sono strutture dati che permettono di memorizzare coppie chiave-valore. Sono estremamente utili per rappresentare dati eterogenei, come record, configurazioni, o risultati di misurazioni.

Caratteristiche principali:

- Accesso rapido: I valori sono accessibili tramite chiave, non tramite indice.
- Chiavi univoche: Ogni chiave deve essere univoca all’interno di un dizionario.
- Tipi di dato flessibili: Le chiavi devono essere immutabili (stringhe, numeri, tuple), mentre i valori possono essere di qualsiasi tipo (anche altri dizionari o liste).
- Dinamici: È possibile aggiungere, modificare o rimuovere coppie chiave-valore in qualsiasi momento.

Sintassi di base
```python 
Dizionario = {
    "chiave1": valore1,
    "chiave2": valore2,
}
```
### Accesso a un valore
valore = dizionario["chiave1"]

### Esempio
```python
studente = {
   "nome": "Mario",
   "cognome" : "Rossi",
   "esami_mancanti" : ["Analisi 1", "Storia Medievale"]
}
print(type(studente))                                                                                                                                                                                  
print( studente["esami_mancanti"])
```
output
```
<class 'dict'>
['Analisi 1', 'Storia Medievale']
```
### Aggiunta/modifica
dizionario["nuova_chiave"] = nuovo_valore
### Rimozione
del dizionario["chiave1"]
#### oppure
valore_rimosso = dizionario.pop("chiave1", valore_di_default)
```python
studente["Codice Persona"] = 10890000
print(studente)
del studente["Codice Persona"]
print(studente)
```
output
```
{'nome': 'Mario', 'cognome': 'Rossi', 'esami_mancanti': ['Analisi 1', 'Storia Medievale'], 'Codice Persona': 10890000}
{'nome': 'Mario', 'cognome': 'Rossi', 'esami_mancanti': ['Analisi 1', 'Storia Medievale']}
```

### Metodi utili

- keys(): restituisce una vista delle chiavi.
- values(): restituisce una vista dei valori.
- items(): restituisce una vista delle coppie (chiave, valore).
```python
print(f"{studente.keys()}, {studente.values()}")
```
output
```
dict_keys(['nome', 'cognome', 'esami_mancanti']), dict_values(['Mario', 'Rossi', ['Analisi 1', 'Storia Medievale']])
```
Attenzione: studente.keys, non è una lista ma la si può convertire
```python
print(type(studente.keys()))
chiavi = list(studente.keys())
print(type(chiavi))
```
output
```
<class 'dict_keys'>
<class 'list'>
```

# Classi

In Python, le **classi** sono il cuore della programmazione orientata agli oggetti (OOP), un approccio che consente di strutturare il codice in modo modulare, riutilizzabile e facilmente estendibile. 
Una classe può essere vista come un **modello** per la creazione di un insieme di **oggetti**. Ogni oggetto creato da una classe è detto **istanza** e possiede **attributi** (variabili che memorizzano dati) e **metodi** (funzioni che definiscono le azioni che l’oggetto può compiere).
La gerarchia è quindi la seguente:
1. Classe genitore
2. Sottoclasse
3. Istanza (Oggetto)
### Dichiarazione di una Classe
Per definire una classe in Python si utilizza la parola chiave `class`, seguita dal nome della classe (per convenzione, in **CamelCase**) e dai due punti. Il corpo della classe è indentato e può contenere attributi e metodi.
La prima cosa da fare quando si crea una nuova classe è definirne gli attributi.
```python
class NomeClasse: # costruttore della classe
    def __init__(self, parametro1, parametro2): #Definisco gli attributi dell'oggetto con __init__
        # Attributi di istanza (specifici per ogni oggetto)
        self.attributo1 = parametro1
        self.attributo2 = parametro2
```
Vediamo un esempio:
Voglio ricreare in python degli oggetti che abbiano le caratteristiche (attributi), e che svolgano le medesime azioni (metodi), di alcuni animali domestici. 
Potrei creare un dizionario per ciascun animale e una funzione per ciascuna azione svolta ma sarebbe dispendioso, poco scalabile e non estendibile.
Noto quindi che ci sono azioni e caratteristiche comuni a tutti gli animali (*classe genitore*).
Ciascun animale domestico ha un sesso, un età e un padrone.
```python
class Animal: # costruttore della classe
    def __init__(self, sex, age, owner): #Definisco gli attributi dell'oggetto con __init__
        self.sex = sex
        self.age = age
        self.owner = owner
```
Con queste righe di codice specifico che quando una nuova istanza di animale verrà creata, gli saranno passati degli argomenti posizionali (sex, age, owner) caratteristici dell'animale.
Con self.attributo = attributo intendo che dopo la creazione dell'istanza mi riferirò al suo attributo con istanza.attributo
### Creazione di un’Oggetto
Per creare un’istanza di una classe, si chiama la classe come se fosse una funzione, passando gli argomenti richiesti dal metodo `__init__`:

```python
tobia = Animal("male", 2, "Mario")
print(f"Tobia is a {tobia.age} years old pet whose owner is {tobia.owner}")
```
L'output sarà
```
 Tobia is a 2 years old pet whose owner is Mario
```
### Creazione di un metodo
Creiamo ora un nuovo metodo per la classe animale. Tutti gli animali mangiano, quindi possiamo aggiungere un metodo alla classe genitore. 
Aggiorniamo il costruttore in questo modo
```python
class Animal:
    def __init__(self, sex, age, owner):
        self.sex = sex
        self.age = age
        self.owner = owner
    def eat(self, food):
        print(f"Mmm that was a nice {food}, do you want to try {self.owner}?")
```
il metodo sarà analogo ad una funzione propria di ciascun animale, che riceverà come attributo posizionale *food*
```python
tobia.eat("chicken bone")
```
Output
```
Mmm that was a nice chicken bone, do you want to try Mario?
```

### Ereditarietà
L’ereditarietà consente di creare una nuova classe (**classe figlia**) che eredita attributi e metodi da una classe esistente (**classe genitore**). Si utilizza la sintassi `class Figlia(Genitore)`.

```python
class Figlia(Genitore):
    def __init__(self, attributi_genitore, attributi_figlio):
        super().__init__(attributi_genitore)# Eredito metodi e attributi della classe genitore
        self.attributo_figlio = attributo_figlio #Attributo specifico della sottoclasse
    def nuovo_metodo(self):
        return "Metodo della classe figlia"
```
Si tratta del primo grande vantaggio dell'utilizzo delle classi. 
Continuando con l'esempio precedente mi piacerebbe aggiungere attributi e metodi specifici dei gatti ereditando però metodi e attributi comuni a tutti gli animali.
```python
from time import sleep # importo la funzione sleep dalla libreria time
class Cat(Animal):
    def __init__(self,sex, age, owner, fur_color):
        super().__init__(sex, age, owner)#quando creo un'istanza di gatto eredito subito l'init della classe padre
        self.fur_color = fur_color 
    def cat_sleep(self, duration):
        print("I'm falling asleep")
        sleep(duration)
duchessa = Cat("female", 4, "Adelaide Bonfamille", "white")
duchessa.cat_sleep(3)
duchessa.eat("fish")
```
*N.B.* Sleep *è una funzione della libreria* time *che riceve un tempo in secondi e mette in pausa per quel tempo.*

Output
```
I'm falling asleep
[pausa di 3 secondi]
Mmm that was a nice fish, do you want to try Adelaide Bonfamille?
```

### Cenni su Polimorfismo e Overriding
Il polimorfismo permette di ridefinire un metodo ereditato nella classe figlia, sovrascrivendone il comportamento:
```python
class Figlia(Genitore):
    def metodo_istanza(self):
        return "Comportamento modificato"
```
Con questo codice chiamando il metodo istanza otterrò il comportamento specificato nel costruttore della classe figlia, non quello della classe genitore
```python
class Animal: # costruttore della classe
    def __init__(self, sex, age, owner): #Definisco gli attributi dell'oggetto con __init__
        self.sex = sex
        self.age = age
        self.owner = owner
    def eat(self, food):
        print(f"Mmm that was a nice {food}, do you want to try {self.owner}?")
class Cat(Animal):
    def __init__(self,sex, age, owner, fur_color):
        super().__init__(sex, age, owner)#quando creo un'istanza di gatto eredito subito l'init della classe padre, se non lo metto faccio "l'overide", in generale non è bene farlo mma a volte è utile
        self.fur_color = fur_color #non è necessario chiamarli allo stesso modo
    def eat(self, food):
        print(f"Mmm that was a nice {food}, so good there is no more to try {self.owner}!")
    def cat_sleep(self, duration):
        print("I'm falling asleep")
        sleep(duration)
duchessa = Cat("female", 4, "Adelaide Bonfamille", "white")
duchessa.eat("fish")
```
Output
```
Mmm that was a nice fish, so good there is no more to try Adelaide Bonfamille!
```

Talvolta può essere utile effettuare l'overriding, ovvero non ereditare alcuni metodi della classe genitore. Per farlo bisogna tralasciare la riga 'super().__init__(attributi)'
```python
class Lion(Animal):
    def __init__(self,sex, age, fur_color):
        self.sex = sex
        self.age = age
        self.fur_color = fur_color #non è necessario chiamarli allo stesso modo
    def eat(self, food):
        print(f"Mmm that was a nice {food}")
mufasa = Lion("male", 6, "Yellow")
mufasa.eat("gazelle")
```
Output
```
Mmm that was a nice gazelle
```
Se provo ad eseguire la seguente riga
```python
print(mufasa.owner)
```
Ottengo
```
AttributeError: 'Lion' object has no attribute 'owner'
```
Mufasa è il re, non ha padrone!!!
*N.B. L'override, in generale, è da evitare.*

# Esercizi su Dizionari e CLassi
### Esercizio 1: Gestione Pazienti
Scrivi una funzione che crei un dizionario per rappresentare un paziente con i seguenti dati:

- nome (stringa)
- età (intero)
- parametri_vitali (dizionario con chiavi: "frequenza_cardiaca", "pressione", "saturazione")

Poi scrivi una funzione che stampi i parametri vitali del paziente.
### Soluzione 1
```python
def crea_paziente(nome, età, parametri_vitali):
    paziente = {
        "nome": nome,
        "età": età,
        "parametri_vitali": parametri_vitali
    }
    return paziente

def stampa_parametri(paziente):
    print(f"Parametri vitali di {paziente['nome']}:")
    for chiave, valore in paziente["parametri_vitali"].items():
        print(f"{chiave}: {valore}")
```
#### Esempio di utilizzo

```python
parametri1 = {
    "frequenza_cardiaca": 72,
    "pressione": "120/80",
    "saturazione": 98
}
paziente1 = crea_paziente("Mario Rossi", 45, parametri1)
stampa_parametri(paziente1)
```
### Esercizio 2: Analisi Segnali ECG
Scrivi una funzione che crei un dizionario per rappresentare un segnale ECG con i seguenti dati:

- id_paziente (stringa)
- durata (float, in secondi)
- valori (dizionario con chiavi: "tempo", "ampiezza")

Poi scrivi una funzione che calcoli la frequenza cardiaca media (bpm) del segnale

ecg_data = {
    "tempo": [0.1, 0.5, 0.9, 1.3, 1.7],
    "ampiezza": [1.2, 1.5, 1.3, 1.4, 1.6]
}

assumendo che ogni picco corrisponda a un battito.
### Soluzione:
```python 
def crea_segnale_ecg(id_paziente, durata, valori):
    segnale = {
        "id_paziente": id_paziente,
        "durata": durata,
        "valori": valori
    }
    return segnale

def calcola_frequenza_media(segnale):
    num_picchi = len(segnale["valori"]["ampiezza"])
    frequenza_bpm = (num_picchi / segnale["durata"]) * 60
    return round(frequenza_bpm, 2)

ecg_data = {
    "tempo": [0.1, 0.5, 0.9, 1.3, 1.7],
    "ampiezza": [1.2, 1.5, 1.3, 1.4, 1.6]
}
ecg = crea_segnale_ecg("PZ123", 2.0, ecg_data)
print(f"Frequenza media: {calcola_frequenza_media(ecg)} bpm")
```
Output
```
Frequenza media: 150.0 bpm
```
### Esercizio 3: Gestione Database Strumenti
Scrivi una classe DatabaseStrumenti che gestisca un inventario di strumenti biomedici. La classe deve avere:

- Un attributo strumenti (dizionario con chiavi: id_strumento, valori: dizionario con "nome", "tipo", "disponibile")
- Un metodo aggiungi_strumento(id, nome, tipo)
- Un metodo presta_strumento(id) che imposta disponibile=False
- Un metodo restituisci_strumento(id) che imposta disponibile=True

A questo punto aggiungi i seguenti strumenti

- ("S001", "Elettrocardiografo", "Diagnostico")
- ("S002", "Sfigmomanometro", "Monitoraggio")

Presta  l'elettrocardiografo e stampa il database
### Soluzione
```python
class DatabaseStrumenti:
    def __init__(self):
        self.strumenti = {}

    def aggiungi_strumento(self, id, nome, tipo):
        self.strumenti[id] = {
            "nome": nome,
            "tipo": tipo,
            "disponibile": True
        }

    def presta_strumento(self, id):
        if id in self.strumenti:
            self.strumenti[id]["disponibile"] = False

    def restituisci_strumento(self, id):
        if id in self.strumenti:
            self.strumenti[id]["disponibile"] = True

db = DatabaseStrumenti()
db.aggiungi_strumento("S001", "Elettrocardiografo", "Diagnostico")
db.aggiungi_strumento("S002", "Sfigmomanometro", "Monitoraggio")
db.presta_strumento("S001")
print(db.strumenti)
```
Output
```
{'S001': {'nome': 'Elettrocardiografo', 'tipo': 'Diagnostico', 'disponibile': False}, 'S002': {'nome': 'Sfigmomanometro', 'tipo': 'Monitoraggio', 'disponibile': True}}
```
