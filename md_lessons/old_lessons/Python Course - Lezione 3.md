BENVENUTO
- PEP 8
- Dizionari
- Sets
- Slicing
- boolean, if, else
BREAK e RECAP
- for
- while (accenno)
- matrici
- stampiamo le matrici con una funzione
- venv
- numpy matrix ()
## Recap Lezione 1 e 2 (10 min)

- Cosa abbiamo fatto?
	- Vogliamo dare i perchè delle cose, non calarle dall'alto.
- perchè python?
	- Facile da usare, veloce da prototipare, diffusissimo, usato molto nel ML.
- perchè linux?
	- Perchè è portable
	- perchè consuma poche risorse e poca batteria (niente interfacce!)
	- perchè è lo standard per tutti i dispositivi avanzati dove l'interfaccia utente non è quella di Windows o Mac OS. (Esistono anche altri standard industriali, ma non permettono applicazioni complesse e non sono così veratili)
- perchè visual studio?
	- è un IDE molto usato, quindi con molte risorse online
- Perchè non google colab o un compilatore online?
	- Perchè a meno che di lavorare solo nella ricerca, quando si parla di implementazione non sarà possibile usare solo google colab o un compilatore online. Lavorando sin da subito con la shell (terminale) ci si abitua a quello che poi potrebbe essere lo standard sul posto di lavoro.
- Quando usare python e quando:
	- C/C++
	- matlab
	- javascript
	- java
	- R
	- Rust?


## Varie
#### multiple assignament

### PEP 8
PEP: Python Enhancement Proposal
PEP 8: parla di come dare stile al codice
- Indentazione:
	- 4 spazi per livello (gli editor ma non tutti convertono il tab in 4 spazi)
	- se no ci sono problemi!!+
- 79 char per linea
- i commenti massimo di 72 char per linea, per documentazione automatica
- Linee vuote per dividere il file ma non troppo, man mano vi dirò le linee guida migliori
- aprire PEP 8 presso https://python.org/dev/peps/pep-0008


# Fine Tipi Base
## Dizionari

Cosa sono?
Sono coppie di chiavi-valore (key value pairs)

I dizionari e le liste condividono le seguenti caratteristiche:

- Entrambi sono mutabili.
- Entrambi sono dinamici. Possono crescere e ridursi secondo necessità.
- Entrambi possono essere annidati. Una lista può contenere un'altra lista. Un dizionario può contenere un altro dizionario. Un dizionario può anche contenere una lista, e viceversa.

I dizionari si differenziano dalle liste principalmente nel modo in cui si accede agli elementi:

- Gli elementi di una lista sono accessibili tramite la loro posizione nella lista, mediante indicizzazione.
- Gli elementi di un dizionario sono accessibili tramite chiavi.

Nonostante questo, da python 3.6 i dizionari preservano l'ordine degli elementi in cui sono stati creati, quindi quando si itera su un dizionario ciò viene fatto nell'ordine in cui ci si aspetterebbe. Di fatto sono ordinati, ma non viene garantito l'accesso a questo ordine perchè in tal caso è preferibile l'uso delle liste!


Regole sulle chiavi:
Every Immutable Type can be a key. (Strings, Touples, Ints )
First, a given key can appear in a dictionary only once. Duplicate keys are not allowed. A dictionary maps each key to a corresponding value, so it doesn’t make sense to map a particular key more than once.
Regole sui Valori:
Non ci sono regole:

### Built-in functions:
#### in
#### not in

#### len()

### Built-in methods:
#### `d.clear()`



#### `d.get(<key>[, <default>])`

> Returns the value for a key if it exists in the dictionary.

The Python dictionary `.get()` method provides a convenient way of getting the value of a key from a dictionary without checking ahead of time whether the key exists, and without raising an error.

`d.get(<key>)` searches dictionary `d` for `<key>` and returns the associated value if it is found. If `<key>` is not found, it returns `None`:

``` python
>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> print(d.get('b'))
>>> 20
>>> print(d.get('z'))
>>> None
```

If `<key>` is not found and the optional `<default>` argument is specified, that value is returned instead of `None`:

```python
>>> print(d.get('z', -1))
>>> -1
```


#### `d.items()`

> Returns a list of key-value pairs in a dictionary.

`d.items()` returns a list of tuples containing the key-value pairs in `d`. The first item in each tuple is the key, and the second item is the key’s value:

`>>> d = {'a': 10, 'b': 20, 'c': 30} >>> d {'a': 10, 'b': 20, 'c': 30}  >>> list(d.items()) [('a', 10), ('b', 20), ('c', 30)] >>> list(d.items())[1][0] 'b' >>> list(d.items())[1][1] 20`

#### `d.keys()`

> Returns a list of keys in a dictionary.

`d.keys()` returns a list of all keys in `d`:

```python
>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> d
{'a': 10, 'b': 20, 'c': 30}
>>> list(d.keys())
>>> ['a', 'b', 'c']
```


#### `d.values()`

> Returns a list of values in a dictionary.

`d.values()` returns a list of all values in `d`:

Python

`>>> d = {'a': 10, 'b': 20, 'c': 30} >>> d {'a': 10, 'b': 20, 'c': 30}  >>> list(d.values()) [10, 20, 30]`

Any duplicate values in `d` will be returned as many times as they occur:

Python

`>>> d = {'a': 10, 'b': 10, 'c': 10} >>> d {'a': 10, 'b': 10, 'c': 10}  >>> list(d.values()) [10, 10, 10]`

**Technical Note:** The `.items()`, `.keys()`, and `.values()` methods actually return something called a **view object**. A dictionary view object is more or less like a window on the keys and values. For practical purposes, you can think of these methods as returning lists of the dictionary’s keys and values.

#### `d.pop(<key>[, <default>])`

> Removes a key from a dictionary, if it is present, and returns its value.

If `<key>` is present in `d`, `d.pop(<key>)` removes `<key>` and returns its associated value:

```python
>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> d.pop('b')
20
>>> d
{'a': 10, 'c': 30}
```

`d.pop(<key>)` raises a `KeyError` exception if `<key>` is not in `d`:

Python

`>>> d = {'a': 10, 'b': 20, 'c': 30}  >>> d.pop('z') Traceback (most recent call last):   File "<pyshell#4>", line 1, in <module>     d.pop('z') KeyError: 'z'`

If `<key>` is not in `d`, and the optional `<default>` argument is specified, then that value is returned, and no exception is raised:

Python

`>>> d = {'a': 10, 'b': 20, 'c': 30} >>> d.pop('z', -1) -1 >>> d {'a': 10, 'b': 20, 'c': 30}`

#### `d.popitem()`

> Removes a key-value pair from a dictionary.

`d.popitem()` removes the last key-value pair added from `d` and returns it as a tuple:

Python

`>>> d = {'a': 10, 'b': 20, 'c': 30}  >>> d.popitem() ('c', 30) >>> d {'a': 10, 'b': 20}  >>> d.popitem() ('b', 20) >>> d {'a': 10}`

If `d` is empty, `d.popitem()` raises a `KeyError` exception:

Python

`>>> d = {} >>> d.popitem() Traceback (most recent call last):   File "<pyshell#11>", line 1, in <module>     d.popitem() KeyError: 'popitem(): dictionary is empty'`

**Note:** In Python versions less than 3.6, `popitem()` would return an arbitrary (random) key-value pair since [Python dictionaries were unordered](https://realpython.com/iterate-through-dictionary-python/) before version 3.6.

#### `d.update(<obj>)`

> Unisce un dizionario con un altro dizionario o con un iterabile di coppie chiave-valore (key-value pair).

Se `<obj>` è un dizionario, `d.update(<obj>)` unisce le voci di `<obj>` in `d`. Per ogni chiave in `<obj>`:
- Se la chiave non è presente in `d`, la coppia chiave-valore da `<obj>` viene aggiunta a `d`.
- Se la chiave è già presente in `d`, il valore corrispondente in `d` per quella chiave viene aggiornato al valore da `<obj>`.

Ecco un esempio che mostra due dizionari uniti insieme:

```python
>>> d1 = {'a': 1, 'b': 2, 'c': 3}
>>> d2 = {'b': 99, 'd': 4}
>>> d1.update(d2)
>>> d1
{'a': 1, 'b': 99, 'c': 3, 'd': 4}
```

In questo esempio, la chiave `'b'` è già esistente in `d1`, quindi il suo valore viene aggiornato a `99`, il valore per quella chiave da `d2`. Tuttavia, non c'è la chiave `'d'` in `d1`, quindi quella coppia chiave-valore viene aggiunta da `d2`.

`<obj>` può anche essere una sequenza di coppie chiave-valore, simile a quando si utilizza la funzione `dict()` per definire un dizionario. Ad esempio, `<obj>` può essere specificato come una lista di tuple:

```python
>>> d1 = {'a': 10, 'b': 20, 'c': 30}
>>> d1.update([('b', 200), ('d', 400)])
>>> d1
{'a': 10, 'b': 200, 'c': 30, 'd': 400}
```

Oppure i valori da unire possono essere specificati come una lista di argomenti con parole chiave (key-words arguments):

```python
>>> d1 = {'a': 10, 'b': 20, 'c': 30}
>>> d1.update(b=200, d=400)
>>> d1
{'a': 10, 'b': 200, 'c': 30, 'd': 400}
```


## Sets
Un Set in [programmazione Python](https://www.geeksforgeeks.org/getting-started-with-python-programming/) è un tipo di dati collezione **non ordinato** che è **iterabile** e non ha **elementi duplicati**. Mentre i set sono **mutabili**, il che significa che puoi aggiungere o rimuovere elementi dopo la loro creazione, gli *elementi individuali all'interno del set devono essere immutabili e non possono essere modificati direttamente*.

> I Set sono rappresentati da { } (valori racchiusi tra parentesi graffe)

Il principale vantaggio nell'uso di un set, rispetto a una [lista](https://www.geeksforgeeks.org/python-lists/), è che dispone di un metodo altamente ottimizzato per verificare se un elemento specifico è contenuto nel set. Questo si basa su una struttura di dati nota come [tabella hash](https://www.geeksforgeeks.org/hashing-set-1-introduction/). Poiché i set sono non ordinati, non possiamo accedere agli elementi usando gli indici come facciamo nelle liste.

```python
var = {"Geeks", "for", "Geeks"}
type(var)
```

### Frozen Sets

FINIRE DI APPROFONDIRE DA SOLI


## Liste

### Slicing
undefined

```python
>>> word = ["G","a","g","l","i","o","f","f","o"]
>>> # o semplicemente word = list("Gaglioffo")
>>> word[1:6]
['a', 'g', 'l', 'i', 'o']
```

#### Dall'inizio
```python
>>> word[:6]
['G', 'a', 'g', 'l', 'i', 'o']
```
#### Fino alla fine
```python
>>> word[1:]
['a', 'g', 'l', 'i', 'o', 'f', 'f', 'o']
```

#### Tutta la stringa
```python
>>> word[:]
['G', 'a', 'g', 'l', 'i', 'o', 'f', 'f', 'o']
```

#### Dalla fine
```python
>>> word[1:-3]
['a', 'g', 'l', 'i', 'o']
```


# Operazioni logiche
(servono per if/ else)

I tipi booleani sono considerati tipi numerici
```python
>>> True == 1
True
```


### Comparare i valori
Tipi di operatori:
```python
== # equality
!= # inequality
> # greater than
>=
<
<=
```

## Operatori Logici
### not
### and
### or
### The `is` Operator[](https://realpython.com/python-boolean/#the-is-operator "Permanent link")

The [`is` operator](https://realpython.com/lessons/is-operator/) checks for **object identity**. In other words, `x is y` evaluates to `True` only when `x` and `y` evaluate to the same object. The `is` operator has an opposite, the `is not` operator.

A typical usage of `is` and `is not` is to compare lists for identity:

Python

`>>> x = [] >>> y = [] >>> x is x True >>> x is not x False >>> x is y False >>> x is not y True`

Even though `x == y`, they are not the same object. The `is not` operator always returns the opposite of `is`. There’s no difference between the expression `x is not y` and the expression `not (x is y)` except for readability.

Keep in mind that the above examples show the `is` operator used only with lists. The behavior of the `is` operator on [immutable](https://realpython.com/courses/immutability-python/) objects like numbers and strings is [more complicated](https://realpython.com/python-is-identity-vs-equality/#when-only-some-integers-are-interned).
### The `in` Operator[](https://realpython.com/python-boolean/#the-in-operator "Permanent link")

The [`in` operator](https://realpython.com/python-in-operator/) checks for **membership**. An object can define what it considers members. Most sequences, such as lists, consider their elements to be members:

```python
>>> small_even = [2, 4]
>>> 1 in small_even
False
>>> 2 in small_even
True
>>> 10 in small_even
False
```


Since `2` is an element of the list, `2 in small_even` returns `True`. Since `1` and `10` aren’t in the list, the other expressions return `False`. In all cases, the `in` operator returns a Boolean value.

Since strings are sequences of characters, you might expect them to also check for membership. In other words, characters that are members of the string will return `True` for `in`, while those that don’t will return `False`:

```python
>>> "e" in "hello beautiful world"
True
>>> "x" in "hello beautiful world"
False
```


Since `"e"` is the second element of the string, the first example returns `True`. Since `x` doesn’t appear in the string, the second example returns `False`. However, along with individual characters, substrings are also considered to be members of a string:

Python

`>>> "beautiful" in "hello beautiful world" True >>> "belle" in "hello beautiful world" False`

Since `"beautiful"` is a substring, the `in` operator returns `True`. Since `"belle"` is not a substring, the `in` operator returns `False`. This is despite the fact that every individual letter in `"belle"` is a member of the string.

Like the operators `is` and `==`, the `in` operator also has an opposite, [`not in`](https://realpython.com/python-in-operator/#pythons-not-in-operator). You can use `not in` to confirm that an element is not a member of an object.
in


# If/else

```python
# IFELSE ELIF
print('What is age?')
age = int(input('number:')) # user gives number as input
if age > 18:
	print('go ahead drive')
elif age == 18:
	print('come personaly for test')
else:
	print('still underage')
```

# Cicli

## For
### For Loops with "in"
```python
thislist = ["apple", "banana", "cherry"]  
for x in thislist:  
  print(x)
```
### For Loops with "index"
```python
thislist = ["apple", "banana", "cherry"]  
for i in range(len(thislist)):  
  print(thislist[i])
```

### While
```python
thislist = ["apple", "banana", "cherry"]  
i = 0  
while i < len(thislist):  
  print(thislist[i])  
  i = i + 1
```

### List comprehension
```python
thislist = ["apple", "banana", "cherry"]  
[print(x) for x in thislist]
```

