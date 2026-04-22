# Lesson 1

## Intro (20 min)
- Why Python?
	- advantages
	- disadvantages
		- https://www.freecodecamp.org/news/python-vs-c-plus-plus-time-complexity-analysis/
	- use cases
		- based on motivation of participants
		- !!! Find good examples to **SEE**
		- https://inoxoft.com/blog/top-23-applications-made-with-python/
- What is python?
	- Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
	- [[Compiled and Interpreted Language]]
		- Its high-level built in data structures, combined with *dynamic typing* (This means that the type of a variable is determined at runtime) and *dynamic binding*, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance.
		- Python è un colla che delega certe funzioni a pacchetti in C
		- Python supports *modules and packages*, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.
	- How does it work (high level, formatting, class based ecc) the interpreter ecc
	- when to choose python
	- the open source community
	- ubuntu e linux
- How are we gonna learn python
- Tips about programming and troubleshooting
	- non sappiamo quante persone avranno difficoltà ecc...
	- Documentazione ufficiale
	- Stackoverflow
	- Siti vari
	- chatgpt (rischia di rendere frustrante e di creare problemi dopo, short term reward)
## Setup (60 min)

[[Programming Tools and Python Installation Guide]]
### Windows

**Installare wsl:**

Usa una versione leggermente diversa da quella che abbiamo visto noi. Provare a seguire il tutorial dall'inizio in caso di problemi. Prima di arrendersi al proprio destino provate a riavviare il computer, a molti ha risolto i problemi.
https://learn.microsoft.com/en-us/windows/wsl/install


**Installare python:**

```bash
sudo apt install python3
```

Controllare se l'installazione è avvenuta correttamente:
```bash
python3 -V
```
Si dovrebbe ottenere un output del tipo:
```
root@host:~# python3 -V
Python 3.12.3
```

In caso di problemi consultare il seguente link e seguire [procedure alternative](https://www.rosehosting.com/blog/how-to-install-python-on-ubuntu-24-04/).

### MAC OS
- Installare Homebrew
	(non fatto assieme ma consigliato, consente di installare pacchetti da terminale come in Linux. Potrebbe essere necessario farlo nelle lezioni finali)
	https://iboysoft.com/howto/install-homebrew-on-mac.html

- Installare python
	Seguire la sezione 5.1.1 di questo tutorial, non andare oltre.
	https://docs.python.org/3/using/mac.html#installation-steps

## Linux Commands 101

Questa sezione è una guida rapida ai comandi base di Linux. Gli esempi sono pensati per essere eseguiti in sequenza, utilizzando un file `prova.txt` che creeremo e modificheremo.

**`pwd` (Print Working Directory):** Mostra il percorso completo della cartella in cui ti trovi attualmente. È utile per orientarsi.
```bash
pwd
```

**`ls` (List):** Elenca tutti i file e le cartelle presenti nella directory corrente.
```bash
ls
```

**`mkdir` (Make Directory):** Crea una nuova cartella. Creiamone una per i nostri esperimenti.
```bash
mkdir appunti_python
```

**`cd` (Change Directory):** Ti permette di spostarti tra le cartelle. Entriamo nella cartella appena creata.
```bash
cd appunti_python
```

**`touch`:** Crea un file vuoto. Se il file esiste già, ne aggiorna la data di modifica.
```bash
touch prova.txt
```

**`echo`:** Scrive una stringa di testo. Usando `>` possiamo "redirezionare" l'output e scrivere il testo dentro un file (sovrascrivendolo).
```bash
echo "Questa è la prima riga." > prova.txt
```

**`cat` (Concatenate):** Mostra il contenuto di uno o più file. Verifichiamo cosa abbiamo scritto.
```bash
cat prova.txt
```

**`echo` con `>>`:** A differenza di `>`, il doppio `>>` aggiunge il testo alla fine del file, senza cancellare il contenuto esistente.
```bash
echo "Questa è la seconda riga." >> prova.txt
cat prova.txt
```

**`cp` (Copy):** Copia un file. Creiamo una copia di backup.
```bash
cp prova.txt backup_prova.txt
```

**`mv` (Move):** Sposta o rinomina un file. Rinominiamo il nostro file originale.
```bash
mv prova.txt note_importanti.txt
```

**`rm` (Remove):** Rimuove (cancella) un file. Facciamo attenzione, perché non c'è un cestino!
```bash
rm backup_prova.txt
```

**`cd ..`**: Comando speciale per tornare alla cartella "genitore" (quella che contiene la cartella attuale).
```bash
cd ..
```

**`rmdir` (Remove Directory):** Rimuove una cartella, ma solo se è vuota. Prima svuotiamola e poi cancelliamola.
```bash
rm appunti_python/note_importanti.txt
rmdir appunti_python
```

**`man` (Manual):** Mostra il manuale di un comando, spiegando come funziona e quali opzioni ha. Per uscire, premi `q`.
```bash
man ls
```

**`sudo` (Super User Do):** Esegue un comando con i privilegi di amministratore. È necessario per operazioni di sistema, come installare software.
```bash
sudo apt-get update
```
- check that python is working
- come installare pachetti e cos'è pip
	- I’ve finished renaming pyinstall to its new name: pip. The name pip is [an] acronym and declaration: pip installs packages.
	- 

## Visual studio code (20 min)
- install visual studio code
- https://code.visualstudio.com/
	- install extensions in visual studio code
- Create a simple python file in visual studio code
- Visual studio completion and documentation
- Run that file

### Windows Installation

1. Installa [Visual Studio Code](https://code.visualstudio.com/Download).
2. Cerca il terminale (`Windows + S`)
	![](attachment/99216af86ab123fa9fb2afaeeec4d448.png)
3. Scegli ubuntu 2024-4.1 LTS dal menù a tendina
	![](attachment/8746bdc7feaed470ab3f172228dfc575.png)
4. Vai nella cartella python course:
	`cd python_course`
5. Avvia visual studio code in quella cartella
	`code .`
	Dovrebbe partire un download di un server che connette visual studio code a wsl, in questo modo visual studio code gira su windows modificando i dati in Linux 

### MAC Installation

1. [Scarica Visual Studio Code](https://go.microsoft.com/fwlink/?LinkID=534106) per macOS.
2. Apri l'elenco dei download del browser e individua l'app o l'archivio scaricato.
3. Se è un archivio, estrai il contenuto. Usa il doppio clic per alcuni browser o seleziona l'icona della 'lente d'ingrandimento' con Safari.
4. Trascina `Visual Studio Code.app` nella cartella **Applicazioni**, rendendolo disponibile nel Launchpad di macOS.
5. Apri VS Code dalla cartella **Applicazioni**, facendo doppio clic sull'icona.

Puoi anche eseguire VS Code dal terminale digitando 'code' dopo averlo aggiunto al percorso:
- Avvia VS Code.
- Apri la **Command Palette** (Cmd+Shift+P) e digita 'shell command' per trovare il comando **Shell Command: Install 'code' command in PATH**.
undefined
- Riavvia il terminale affinché il nuovo valore `$PATH` abbia effetto. Potrai digitare 'code .' in qualsiasi cartella per iniziare a modificare i file in quella cartella.

> **Nota:** Se hai ancora il vecchio alias `code` nel tuo `.bash_profile` (o equivalente) da una versione precedente di VS Code, rimuovilo e sostituiscilo eseguendo il comando **Shell Command: Install 'code' command in PATH**.

[Se non funziona, provare a copiare ed incollare nel terminale questi comandi](https://code.visualstudio.com/docs/setup/mac#_alternative-manual-instructions).

### Install extensions
1. Aprire visual studio code dal terminale nella cartella che interessa (chi ha windows deve aprirlo dal terminale di wsl, vedi sopra come)
	`code .`
2. Cliccare nella barra a sinistra sull'icona estensioni 
![](attachment/29eefb4da27cd8021280634e57b146f5.png)
3. Cercare python nella barra di ricerca ed installare le seguenti estensioni
![](attachment/aef99a4d055e83109f0f00048b70334f.png)
