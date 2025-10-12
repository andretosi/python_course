
# Lezione 2

## Prima di iniziare...
- Localizzare la cartella
- Cancellare i file nella cartella
- aprire visual studio code
- ri-creare i file con i nomi giusti SENZA SPAZI!!!
- print(f"...") NON printf()
- ri-testare python

## Comandi (spostare nella lezione 1)

### Percorsi
Nei nomi della cartelle e dei file è caldamente consigliato usare solo lettere, numeri e trattini alti e bassi. Altri caratteri sono spesso supportati ma richiederebbe avvolgere tra virgolette i nomi ogni volta e ci impazzite dietro.

I seguenti indirizzi possono essere usati come argomento di altri comandi come `cd`, `touch`, `mkdir` e molti altri che abbiamo visto o vedremo.

Immaginiamo la seguente struttura:

undefined
Vediamo quali sono i percorsi per arrivare alle diverse cartelle, supponendo di trovarci dentro la cartella *this_folder*.

This folder:
```bash
.
```
Next folder:
```bash
./next_folder_name
```
Parent folder:
```bash
..
```
Parent of parent folder:
```bash
../..
```
Sibling folder:
```bash
../sibling_folder
```
File di testo nella cartella *sibling*:
```bash
../sibling_folder/text_file.txt
```
è importante sottolineare come l'estensione sia NECESSARIA quando si fa fa riferimento ad un file.

Cartella home:
```bash
~
```
che è un modo più rapido per scrivere:
```bash
/home/user_name
```

Root directory (è la radice del file-system):
```bash
/
```

### Comandi
- - -
Manage open source pakages:

| **apt-get Command**              | **Description**                                                                                    | **Homebrew Equivalent**         |
| -------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- |
| `apt-get update`                 | Fetch and update the package lists from repositories                                               | `brew update`                   |
| `apt-get install <package-name>` | Install a specific package                                                                         | `brew install <package-name>`   |
| `apt-get remove <package-name>`  | Remove a specific package without removing its configuration files                                 | `brew uninstall <package-name>` |
| `apt-get purge <package-name>`   | Remove a specific package and its configuration files                                              | `brew uninstall <package-name>` |
| `apt-get upgrade`                | Upgrade all packages to the newest available version                                               | `brew upgrade`                  |
| `apt-get autoremove`             | Remove packages that were automatically installed to satisfy dependencies and are no longer needed | `brew cleanup`                  |
| `apt-get clean`                  | Clear downloaded archive files                                                                     | `brew cleanup`                  |
| `dpkg -l`                        | List all installed packages                                                                        | `brew list`                     |
| `apt-cache search <term>`        | Search for a package by its name or description                                                    | `brew search <term>`            |

- - -
Aprire la cartella `path_to_folder/folder_name` nell'app predefinita:
- Windows WSL:
```bash
wslview path_to_folder/folder_name
```
o alternativamente:
```bash
explorer.exe path_to_folder/folder_name
```

- Mac OS:
```bash
open path_to_folder/folder_name
```
- - -
Aprire visual studio code nella cartella corrente:
```bash
code .
```
*Nota:* per mac bisogna averlo aggiunto al path per farlo funzionare.
- - -
Navigare in una cartella
```bash
cd path_to_folder
```
- - -
Creare una cartella
```bash
mkdir path_to_folder/name_of_folder
```
- - -
Sapere il percorso completo alla cartella corrente:
```bash
pwd
```
- - -
Creare un file
```bash
touch path_to_file/file_name.extension
```
- - -


## Recap Lezione 1 (10 min)

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


## Venv (15 min)
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

## Python basics (60 min)

Come python usa l'indentazion al posto delle parentesi e dei punti e virgola:
### Comments

```python
# This is a normal comment

# It's a good practice to leave a blank space between the hashtag
# and the rest of the comment.

""" This is a multiline comment.
This is made for long paragraphs of text,
otherwise it will be messy to have it only on one line!
This kind of formatting that you see here is the standard
Usually on the first line there is the "title" of the comment
and below the explanation.
"""
```

Ma cosa dovrei scrivere nei commenti?

è importantissimo commentare tutte le funzioni o i passaggi delicati, che possono non essere chiari a prima vista a noi stessi o a qualcun'altro a prima lettura.

### Variables
Can contain:
- letters
- numbers
- underscore
They can NOT start with a number.

Best practice
I nomi delle variabili devono essere lowercase
... trattini davanti (trattini in mezzo?)

### Leggere gli errori
...
Name errors


## Data Types



### Boolean

### Strings
Si possono  usare
""
o
''


Metodi (cos'è un metodo)
.title()
.upper()
.lower()
.rstrip() Toglie gli spazi a destra che non si vedono di solito
.lstrip()
.strip()
come salvare una stringa dopo averla modificata

errori comuni
```python
message = 'Ti piace l'odore dei funghi?'
```



#### Variuabili nelle stringhe

Da python 3.6
```python
text = f"{var_1}{var_2}"
```

#### Simboli speciali
\t
\n
escape chars


### Numbers

#### Integers
```python
+ - * / **
```
provarli nella sessione dell'interprete


#### Floats
```python
+ - * / ** 
```
#### Mischiare Interi e Floats

....

```python
//
```


#### multiple assignament

#### Conventions
Costanti:
```python
MAX_SPEED = 300
```

Trattini bassi

```python
speed_of_lights = 299_792_458 # m/s
```

### The zen of python
```python
import this
```

### Liste

indice inizia a 0


### Tuple

List of items that can not change. 
```python
dimensions = (100, 200)
```

definite dalla virgola!

posso assegnare un nuovo valore a dimensions ma non posso modificare la toupla che gia esiste.


### Sets
A Set in [Python programming](https://www.geeksforgeeks.org/getting-started-with-python-programming/) is an **unordered** collection data type that is **iterable** and has **no duplicate elements**. While sets are **mutable**, meaning you can add or remove elements after their creation, the *individual elements within the set must be immutable and cannot be changed directly*.

> Set are represented by { } (values enclosed in curly braces)

The major advantage of using a set, as opposed to a [list](https://www.geeksforgeeks.org/python-lists/), is that it has a highly optimized method for checking whether a specific element is contained in the set. This is based on a data structure known as a [hash table](https://www.geeksforgeeks.org/hashing-set-1-introduction/). Since sets are unordered, we cannot access items using indexes as we do in lists.

```python
var = {"Geeks", "for", "Geeks"}
type(var)
```

#### Frozen Sets
...


FINIRE DI APPROFONDIRE DA SOLI

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

### Dizionari




- Comments
- Best practices in comments
- Variables
	- names
	- how do they differ from other programming languages
	- data types
		- strings
			- strings functions
			- variables in strings
			- special chars in strings
			- common errors? (ex related to the " ... ' ..." or others)
		- Numbers
			- Integers
			- Floats
			- Combining both and what happens
			- underscore in numbers (Cool!)
			- constants (convention)
		- Lists
			
		- Tuples
			- 
		- Dictionaries
			- 
		- Comments
			- 
		- The zen of python (principles)
			- `import this`
		- Loops