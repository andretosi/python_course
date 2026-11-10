# Lezione 1 - Introduzione a Python, strumenti di lavoro e ambiente

**Martedì 10 novembre 2026, 17:30–19:30 · Passion in Action, Politecnico di Milano**

Prima di partire, apri la [guida di installazione (PDF)](Python%20Installation%20Guide.pdf). Per il laboratorio usa Ubuntu 26.04 LTS (con WSL 2 se hai Windows) o macOS, con l’ultima versione stabile di Python 3.13.

## Cosa facciamo oggi

Alla fine della lezione dovresti riuscire a orientarti tra file e cartelle, aprire una cartella in VS Code, eseguire uno script e lanciare una cella Jupyter con il Python del tuo progetto.

| Orario | Attività | Risultato da vedere |
| --- | --- | --- |
| 17:30–17:40 | Presentazione del corso, primo calcolo in Python e controllo rapido degli strumenti | Ognuno sa quale terminale usare e riconosce il prompt di Python |
| 17:40–18:00 | File, cartelle e percorsi. Demo e prova breve | Ognuno sa dov’è e trova un file con un percorso relativo |
| 18:00–18:20 | Primo script in VS Code. Esecuzione dal terminale e dal pulsante Run | Il programma stampa testo e un numero |
| 18:20–18:30 | Pausa e recupero per chi sta ancora configurando | Si riparte dal primo controllo che manca |
| 18:30–18:50 | Ambiente virtuale, pip e notebook. Demo completa | Il notebook usa il kernel di .venv e mostra un risultato |
| 18:50–19:20 | Esercizio autonomo della scheda | Uno script e un notebook con due risultati verificabili |
| 19:20–19:30 | Correzione, domande e salvataggio dei file | Tutti sanno come riaprire il laboratorio |

Se il download di Ubuntu o di **ipykernel** rallenta l’aula, teniamo lo stesso ordine. Facciamo la demo dal computer del docente, poi chi ha il setup pronto prova il notebook. Gli altri completano la parte `.py` e riprendono il notebook dal punto indicato nella guida.

## Che cos’è Python

Immagina di ricevere un file con le misure raccolte in laboratorio. Vuoi calcolare la media e rifare lo stesso calcolo ogni volta che arrivano nuove misure. Un programma mette per iscritto i passaggi che il computer deve eseguire. **Python è uno dei linguaggi con cui puoi scrivere quelle istruzioni.**

Quando installi Python, installi anche un **interprete**, cioè il programma che esegue il codice. Puoi passargli un file `.py` oppure scrivere un’istruzione alla volta e vedere subito cosa succede. [Introduzione al linguaggio nella documentazione Python](https://docs.python.org/3/tutorial/appetite.html).

## Perché usiamo Python in questo corso

Si parte con poche righe, che possiamo leggere ed eseguire insieme in aula. Quando il problema cresce, possiamo usare librerie già pronte. Per esempio, possiamo leggere un file di misure, trasformarlo in un grafico e ripetere l’analisi su un altro file senza riscrivere il programma. [Applicazioni di Python](https://www.python.org/about/apps/).

Questo ci permette di fare un percorso continuo. Oggi eseguiamo un primo script e un notebook. Poi usiamo lo stesso linguaggio per analizzare dati e immagini, addestrare i primi modelli e capire come più gruppi possono contribuire a un addestramento quando i dati restano presso chi li ha raccolti. [Scheda ufficiale del corso e calendario](https://www.polimi.it/formazione/passion-in-action/dettaglio/python-from-fundamentals-to-ml-neural-networks-and-secure-federated-learning-1).

## Dove scriviamo e dove vediamo il risultato

| Strumento | A cosa serve oggi |
| --- | --- |
| **Terminale** | Vedere in quale cartella siamo, trovare un file e avviare Python. |
| **VS Code** | Aprire la cartella del laboratorio, scrivere e salvare il codice, poi avviarlo. |
| **Notebook Jupyter** | Alternare spiegazioni, codice e risultati, eseguendo una cella alla volta. |

Nel terminale di Ubuntu o macOS digita `python3.13`. Quando compare `>>>` sei dentro Python. Scrivi `7 * 6` e premi Invio. Il risultato è `42`. Scrivi `exit()` per tornare al terminale. Nella seconda demo faremo lo stesso calcolo da un file usando `print(7 * 6)` per mostrare il risultato.

## Demo 1 · File, cartelle e percorsi

Un percorso **assoluto** parte dalla radice e indica il posto per intero. Due esempi sono `/home/andrea/lezione1_lab` su Ubuntu e `/Users/andrea/lezione1_lab` su macOS. Un percorso **relativo** parte dalla cartella in cui ti trovi. Il punto `.` è la cartella corrente, `..` è quella sopra.

Apriamo `lezione1_lab` in VS Code e, da **Terminal → New Terminal**, verifichiamo il punto di partenza con `pwd`. Se il percorso non finisce con `lezione1_lab`, apri quella cartella prima di continuare.

~~~bash
pwd
mkdir -p demo
cd demo
echo "gatto" > promemoria.txt
ls
cat ./promemoria.txt
cd ..
ls
~~~

Dentro **demo** vediamo `promemoria.txt` e leggiamo **gatto**. Tornati su, vediamo **demo**. Il file è rimasto nella sottocartella. Prova a raggiungerlo da qui con `cat demo/promemoria.txt`. Le virgolette aiutano quando un nome contiene spazi.

Ora fai la [prova breve sui percorsi](Python%20Course%20-%20Lezione%201%20-%20Esercizi.md#prova-breve--percorsi) prima di passare allo script.

## Demo 2 · Il primo file .py

Nell’Explorer di VS Code crea `demo.py` nella cartella `lezione1_lab`, allo stesso livello di **demo**. Scrivi e salva.

~~~python
print("Nella scatola c'è un limone.")
print(7 * 6)
~~~

- `print(...)` mostra quello che gli mettiamo tra parentesi. Le virgolette indicano testo.
- `7 * 6` è un calcolo. Prova a prevedere cosa comparirebbe se scrivessi `print("7 * 6")`, poi eseguilo.
- Per eseguire il file dal terminale usa `python3.13 demo.py`. Poi usa anche **Run Python File** in alto a destra. Dovresti vedere la frase e **42** in entrambi i casi.

Se non parte, controlla il nome del file e il percorso del terminale. Per mostrare come si legge un errore, nella demo togli una parentesi di chiusura, salva ed esegui. Cerca l’ultima riga del messaggio e il numero di riga, rimetti la parentesi e riprova.

## Demo 3 · Ambiente virtuale e notebook

Un **venv** è un ambiente per un singolo progetto. Tiene separati i pacchetti che installiamo. `pip` è lo strumento che installa quei pacchetti. Usiamo `python -m pip` per sapere quale Python sta usando pip.

1. Crea `.venv` in `lezione1_lab` con `python3.13 -m venv .venv`. Se ne hai già uno, riusalo dopo aver verificato la versione di Python.
2. Attiva il venv con `source .venv/bin/activate`. Controlla che `python --version` mostri la versione indicata nella guida e che `python -m pip --version` riporti un percorso dentro `.venv`.
3. Se manca **ipykernel**, installalo con `python -m pip install ipykernel` nel venv attivo. In VS Code scegli il venv da **Python: Select Interpreter**.
4. Crea `demo.ipynb` e in alto a destra scegli **Select Kernel → Python Environments → .venv**. Il **kernel** è il processo Python che esegue le celle. Se serve, segui i passaggi illustrati nella sezione **Ambiente virtuale e Jupyter** della [guida di installazione (PDF)](Python%20Installation%20Guide.pdf).
5. Aggiungi una cella **Markdown** con `## Macedonia`. Aggiungi una cella **Code** con il codice qui sotto. Esegui con **Shift+Invio** e salva.

~~~python
print("Porzioni di macedonia")
print(3 * 5)
~~~

Dovresti vedere il titolo formattato e, sotto la cella di codice, **Porzioni di macedonia** e **15**. Modifica il **5** in **6**. L’output cambia a **18** quando riesegui la cella.

## Esercizio autonomo e chiusura

- [ ] Completa la [scheda di laboratorio](Python%20Course%20-%20Lezione%201%20-%20Esercizi.md#esercizio-autonomo--scatole-di-campioni) dopo le tre demo.
- [ ] Riavvia il kernel e usa **Run All** per verificare il notebook dall’inizio.
- [ ] Salva `.py` e `.ipynb` e controlla che siano nella cartella giusta.

Se avanza tempo, nell’interprete interattivo prova `import this`. Stampa lo *Zen of Python*. Cerca la riga sulla leggibilità e torna al file appena scritto per vedere se si capisce al primo sguardo.

Nella [lezione 2](Python%20Course%20-%20Lezione%202.md) ripartiremo dallo script per dare nomi ai dati e prendere le prime decisioni con il codice.
