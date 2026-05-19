# Lezione 5 - Esercizi

Gli esercizi di questa lezione consolidano:
- ereditarieta
- `super()`
- classi e oggetti
- liste di oggetti

Le soluzioni eseguibili sono raccolte in:
- `lesson_code/lezione_5/soluzioni/`

---

## Problema 1 - Animali con ereditarieta

Creare una classe `Animale` con:
- attributi `nome`, `anni`
- metodo `descrizione()`

Creare una classe `Gatto` che eredita da `Animale` e aggiunge:
- attributo `colori`
- metodo `miagola()`
- metodo `scheda()`

Poi creare `Felix`, 13 anni, colori `bianco` e `nero`, e stampare:
- descrizione
- verso
- scheda

Scheletro:
```python
class Animale:
    def __init__(self, nome, anni):
        # TODO: salva gli attributi
        pass

    def descrizione(self):
        # TODO: restituisci una descrizione
        pass


class Gatto(Animale):
    def __init__(self, nome, anni, colori):
        # TODO: richiama super() e salva colori
        pass

    def miagola(self):
        # TODO: restituisci il verso
        pass

    def scheda(self):
        # TODO: restituisci una scheda breve
        pass


felix = Gatto("Felix", 13, ["bianco", "nero"])

print(felix.descrizione())
print(felix.miagola())
print(felix.scheda())
```

---

## Problema 2 - Lista di animali

Creare una classe `Animale` con:
- attributi `nome`, `anni`
- metodo `descrizione()`
- metodo `verso()`, che nella classe base restituisce `"verso generico"`

Creare due classi figlie:
- `Gatto`, con `verso()` che restituisce `"meow"`
- `Cane`, con `verso()` che restituisce `"bau"`

Creare una lista con:
- `Gatto("Felix", 13)`
- `Cane("Bruno", 3)`
- `Gatto("Nina", 1)`

Stampare per ogni animale:
- descrizione
- verso

---

## Problema 3 - Registro di oggetti

Creare una classe `Gatto` con:
- attributi `nome`, `anni`, `colore`
- metodo `descrizione()`
- metodo `adulto()`, che restituisce `True` se il gatto ha almeno 2 anni

Creare una lista con:
- Felix, 13 anni, bianco e nero
- Sky, 10 anni, nero
- Nina, 1 anno, grigio

Stampare:
- la descrizione di tutti i gatti
- quanti gatti sono adulti
- la media degli anni
