- Fine cicli
	- while
	- *break*
- Matrici
- Funzioni
- Classi
- venv


# Cicli Pt 2

Quando usare while rispetto al for:
Il for esegue un blocco di codice su ogni elemento di un iterabile. Il while va avanti finché una certa condizione rimane vera, questa differenza è ancora più importante in python che in altri linguaggi.


## While

```python
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1
```

### Using flags

```python
active = True

while active:
	message = input(prompt)
	if message == "quit":
		active = False
	else:
		print(message)
```

### Break & Continue

```python
active = True

while active:
	message = input(prompt)
	if message == "quit":
		break # <-- 
	else:
		print(message)
```

`break` può essere usato per uscire da un loop immediatamente senza eseguire il codice rimanente.

Al contrario di break, `continue` serve per ripartire dall'inizio del loop senza eseguire nient'altro.
Per esempio (e così ne approfittiamo per vedere l'operatore `%`):
```python
current_numeber = 0

while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue

	print(current_number)
```
dove `%` da il resto intero della divisione intera `/`.


>[!comment] Osservazione
> Sia `break` che `continue` funzionano sia nei for che nei while


## Matrici
... meglio con librerie...
#### Costruzione
```python
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print(mat)
```
Il risultato è `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
#### Selezionare un elemento
```python
print(mat[1][1])
```
Il risultato è `5`
#### Selezionare una riga
una riga
```python
print(mat[1])
```
il risultato è `[4, 5, 6]`

parte di una riga
```python
print(mat[1][0:2])
```
il risultato è `[4, 5]`
#### Selezionare più righe
```python
print(mat[1:3])
```
il risultato è:
#### Selezionare una colonna
una colonna
```python
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

# Select the second column (index 1)
column = [row[1] for row in mat]

column = mat[:,1]

print(column)
```


parte di una colonna
```python
column = [row[1] for row in mat][1:3]
```

#### Selezionare più colonne
```python
columns = [row[1:3] for row in mat]
```


#### Selezionare una sottomatrice qualunque
```python
cute_little_matrix = [row[1:3] for row in mat][1:3]
```

A questo punto definire una funzione per stampare in modo decente la matrice e capirci qualcosa.


# Funzioni
Nomi di funzioni

```python
def print_matrix(matrix):
    """Print the matrix with nice formatting"""
    for row in matrix:
        print(row)

print_matrix(mat)
```

### positional arguments
```python
def foo(arg1, arg2)
```

#### default positional arguments
```python
def foo(arg1, arg2="default_arg2")
```
Dovrebbero cmq essere in ordine, nel senso che lui interpreta il primo argomento
#### Keyword Arguments
```python
value = foo(arg2="default_arg2", arg1="default_arg1")
```


### Making an argument optional
### Return Values

### Preventing a function from modifying a list

### Passing an arbitrary number of arguments

#### As a Tuple
```python
def make_pizza(tomato_sauce=True, mozzarella=True, *toppings):
	"""Returns a list containing all the ingredients of the pizza"""
	pizza = ["Pasta (farina, lievito madre, acqua, sale, olio d'oliva)"]
	if tomato_sauce == True:
		pizza.append("sugo di pomodoro")
	if mozzarella == True:
		pizza.appemd("mozzarella")
	
	for topping in toppings
		pizza.append(topping)
	
	return pizza
	
make_pizza(("peperoni", "salsisiccia"))
```
*Trovare degli esempi di quando queste cose sono NECESSRAIE*

#### As a Dictionary
```python
def build_rofile(first_name, last_name, **user_info):
	user_info["first_name"]
	...
	return user_info
```

Solitamente si trova `**kwargs` per indicare un numero arbitrario di key value pairs

## Store functions in Modules
Un modulo è semplicemente un file `.py` con tutte le funzioni usate
```python
import pizza_utilities
import pizza_utilities as pz # alias

pz.make_pizza()
```

oppure:
```python
from pizza_utilities import make_pizza

make_pizza("peperoni", "olive", "melanzane")
```

#### Alias
`as`
può essere usato per pacchetti o funzioni

#### Importare tutto
```python
from make_pizza import *
```


# Classi

```python

```

- ogni variabile con prefisso self è disponibile ad ogni metodo della classe



# Venv (15 min)
- A cosa servono gli ambienti virtuali?
- python virtual environment
- python3 -m venv myenv
- . myenv/bin/activate
- deactivate

- Cos'è un ambiente virtuale e a cosa serve?
Un ambiente virtuale è un modo per isolare i pacchetti di python in modo da non avere conflitti con gli stessi pacchetti ma di altre versioni usati in altri progetti. 
- Cos'è venv?
Il modulo `venv` di Python permette di creare ambienti virtuali leggeri, ciascuno con il proprio set di pacchetti. Questi ambienti si basano su un'installazione Python esistente e possono essere isolati dai pacchetti dell'ambiente di sistema. Strumenti come `pip` installano automaticamente i pacchetti all'interno dell'ambiente virtuale, una volta attivato, senza bisogno di specificare altro.

In punti un ambiente virtuale:
- Include un interprete Python specifico e le librerie/binari necessari per un progetto.
- È memorizzato in una directory, solitamente chiamata `.venv` o `venv`.
- Non viene incluso nei sistemi di controllo versione come Git.
- È usa e getta e facile da ricreare.
- Non è progettato per essere spostato o copiato; dovrebbe essere ricreato nella nuova posizione ogni volta che si cambia la cartella del progetto.

Questa configurazione assicura che i progetti abbiano le proprie dipendenze e configurazioni, indipendenti da altri progetti e dall'installazione di sistema di Python. Serve per evitare contesti dove, per esempio, in un progetto uso una versione nuova di un pacchetto che veniva usato anche in un progetto vecchio. In tal caso sovrascrivere il vecchio pacchetto con quello nuovo potrebbe "rompere" il vecchio progetto. Grazie ad un ambiente virtuale, i pacchetti vengono usati con le corrette versioni in entrambi i progetti.

### Come si usa il comando venv
Il comando parte pre-installato con python, non bisogna installare nient'altro. 

Il processo di utilizzo si divide in 3 step:

1. Creare l'ambiente virtuale:
   ```bash
   python3 -m venv myenv
   ```
2. Attivare l'ambiente virtuale:
   ```bash
   . myenv/bin/activate
   ```
3. Disattivare l'ambiente virtuale:
   ```bash
   deactivate
   ```


### Operazioni tra matrici

Non le vediamo ma sono disponibili nella libreria numpy (aggiungere info)




# Funzioni (opz)


