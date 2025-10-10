---
tags:
  - resource
Areas:
  - "[[Programming]]"
  - "[[University]]"
Projects:
  - "[[Python Course]]"
Creation Date: 2025-05-25 18:37
References:
---
# Programma dettagliato
Il corso si struttura in 9 lezioni:

### Lezione 1
La prima lezione è dedicata alla configurazione dell'ambiente di sviluppo e all'introduzione dei concetti basilari necessari per iniziare a programmare in Python. Si partirà dall'importanza di un ambiente Linux-like, per poi passare ai comandi essenziali del terminale e concludere con una prima infarinatura di Python.

*   **Configurazione Ambiente di Sviluppo (per utenti Windows):**
    *   Installazione guidata di WSL (Windows Subsystem for Linux) per creare un ambiente Linux su Windows (attività stimata: 1 ora).
*   **Introduzione al Corso:**
    *   Panoramica della struttura del corso: obiettivi, argomenti trattati in ogni lezione.
    *   Presentazione del progetto finale: sviluppo di un'applicazione pratica utilizzando PyTorch.
*   **Perché Linux? I Vantaggi di un Ambiente UNIX-like:**
    *   Discussione sui benefici dell'utilizzo di sistemi operativi basati su UNIX (Linux, macOS) per lo sviluppo software.
*   **Il Terminale: Il Nostro Strumento Principale:**
    *   Installazione e configurazione del terminale su Ubuntu e macOS.
    *   Gestione dei pacchetti: come installare e aggiornare software da riga di comando (es. `apt` su Ubuntu, `brew` su macOS).
*   **Comandi Essenziali del Terminale:**
    *   **Navigazione e Gestione File:** Comandi come `ls`, `cd`, `pwd`, `mkdir`, `rm`, `cp`, `mv`.
    *   **Visualizzazione e Modifica File:** Comandi come `cat`, `less`, `head`, `tail`.
    *   **Nano Editor:** Introduzione all'editor di testo Nano per creare e modificare file direttamente da terminale.
    *   Comprendere le estensioni dei file e come aprire cartelle e file.
*   ***Problema Pratico di Avvio:***
    *   *Esercitazione guidata: creare una struttura di cartelle, navigare al suo interno, creare un file di testo con Nano, modificarlo e salvarlo, eseguire un semplice script (se applicabile).*
*   **Visual Studio Code (VS Code):**
    *   Introduzione a VS Code come Integrated Development Environment (IDE) consigliato.
    *   Installazione e configurazione base, cenni sulle estensioni utili per Python.
*   **Introduzione a Python:**
    *   Cos'è Python: caratteristiche principali, filosofia e campi di applicazione.
    *   Python da Terminale: avviare l'interprete interattivo di Python e scrivere le prime righe di codice.
*   **Ospite (Guest):**
    *   (Da definire: eventuale intervento di un professionista o esperto).
*   **Culture Pill / Contenuti Esterni:**
    *   **The Zen of Python:** Lettura e commento dei principi guida della filosofia di Python (`import this`).

### Lezione 2: Primi Passi in Python – Tipi di Dati e Controllo del Flusso
La seconda lezione si addentra nel linguaggio Python, introducendo i tipi di dati fondamentali e le prime strutture di controllo del flusso, essenziali per scrivere programmi che possano prendere decisioni ed eseguire compiti ripetitivi.

*   **Tipi di Dati Fondamentali (Parte 1) e Operazioni Relative:**
    *   Esercitazioni pratiche utilizzando l'interprete Python da terminale per familiarizzare con i tipi di dati.
    *   **Booleans (`bool`):**
        *   Valori letterali: `True` e `False`.
        *   Operatori logici: `and`, `or`, `not`.
        *   Contesto booleano e valutazione della verità (truthiness).
    *   **Integers (`int`):**
        *   Numeri interi di precisione arbitraria.
        *   Operatori aritmetici: `+`, `-`, `*`, `/`, `//` (divisione intera), `%` (modulo), `**` (potenza).
    *   **Floats (`float`):**
        *   Numeri in virgola mobile (decimali).
        *   Precisione e potenziali problemi di rappresentazione.
        *   Operazioni aritmetiche e confronto tra float.
    *   **Stringhe (`str`):**
        *   Sequenze immutabili di caratteri.
        *   Creazione: apici singoli, doppi, tripli (per stringhe multiriga e docstring).
        *   Operazioni base: concatenazione (`+`), ripetizione (`*`).
        *   Indicizzazione e slicing.
        *   Metodi comuni: `upper()`, `lower()`, `strip()`, `find()`, `replace()`, `split()`, `join()`.
        *   Formattazione basilare (cenni a f-strings).
*   **Strutture Condizionali: `if`, `elif`, `else`:**
    *   Sintassi e logica delle istruzioni condizionali per controllare il flusso di esecuzione del programma.
    *   Indentazione e la sua importanza in Python.
    *   Esempi pratici: scrivere programmi semplici che prendono decisioni basate su input o stati variabili, combinando condizionali e manipolazione di stringhe/numeri.
*   ***Problema Pratico: Gestione Condizionale dei Dati:***
    *   *Esercizi focalizzati sull'utilizzo di variabili booleane, intere, float, stringhe e sulla costruzione di logiche `if/elif/else` per risolvere problemi specifici (es. validazione input, classificazione semplice).*
*   **Tipi di Dati Fondamentali (Parte 2): Le Liste:**
    *   **Liste (`list`):**
        *   Sequenze ordinate e mutabili di elementi eterogenei.
        *   Creazione: `[]` o `list()`.
        *   Accesso agli elementi tramite indice, slicing.
        *   Modifica: aggiunta (`append()`, `insert()`), rimozione (`remove()`, `pop()`, `del`), modifica di elementi esistenti.
        *   Metodi comuni: `sort()`, `reverse()`, `count()`, `index()`.
        *   Liste annidate (cenni).
*   **Cicli Iterativi: Il Ciclo `for`:**
    *   Iterare su elementi di una sequenza (stringhe, liste).
    *   Utilizzo della funzione `range()` per iterazioni numeriche.
    *   Sintassi del ciclo `for` e variabile di ciclo.
    *   Esempi di utilizzo per elaborare dati contenuti in liste o caratteri di una stringa.
*   ***Problema Pratico: Iterazione e Liste:***
    *   *Esercizi che richiedono l'uso di liste per memorizzare collezioni di dati e cicli `for` per processare tali dati (es. calcolare somme, trovare elementi, trasformare dati).*
*   **Culture Pill / Contenuti Esterni:**
    *   (Da definire: spunti di riflessione, curiosità sul mondo della programmazione o risorse utili).

### Lezione 3
In questi due file di Jupyter Notebook (lezione3.ipynb e lezione3_esercizi.ipynb) vengono trattati i seguenti argomenti di Python:

*   **Matrici:** Creazione e manipolazione di matrici utilizzando liste annidate.
*   **Cicli `for`:** Iterazione su sequenze (liste, stringhe) e utilizzo della funzione `range()`.
*   **Cicli `while`:** Utilizzo per iterazioni basate su una condizione, con esempi come la serie di Fibonacci. Viene anche presentato un problema pratico sulla simulazione di un termometro elettronico.
*   **Funzioni:** Definizione di funzioni, parametri, valori di ritorno, argomenti di default, argomenti keyword e la gestione di argomenti di default mutabili. Viene proposto un esercizio sulla formattazione di matrici tramite funzioni.
*   **Tipi di Dati Avanzati:**
    *   **Dizionari:** Creazione, accesso, modifica, eliminazione di elementi, metodi principali (`keys()`, `values()`, `items()`), iterazione e comprensioni di dizionari.
    *   **Tuple:** Creazione, immutabilità, indicizzazione, nesting e unpacking.
    *   **Set:** Introduzione ai set e operazioni di base.
*   **Esercizi Pratici:**
    *   Visualizzazione allineata di matrici.
    *   Simulazione di un termometro elettronico (utilizzo di cicli `while` e gestione input utente).
    *   Gestione di dati strutturati (es. cartella clinica) utilizzando dizionari e tuple.


### Lezione 4
La lezione 4 tratta i seguenti argomenti:

*   **Ambienti Virtuali:**
    *   Spiegazione del perché sono utili.
    *   Panoramica dei principali strumenti: `venv`, `conda`, `virtualenv`, `pipenv`.
    *   Focus su `venv`: creazione, attivazione (Windows e macOS/Linux), installazione pacchetti, salvataggio (`pip freeze > requirements.txt`) e ripristino (`pip install -r requirements.txt`) delle dipendenze, disattivazione.
    *   Breve accenno a `conda` per la data science.
*   **Jupyter Notebook:**
    *   Cos'è e a cosa serve.
    *   Guida all'installazione su Ubuntu e macOS (tramite `pip` e `conda`).
    *   Utilizzo di Jupyter Notebook all'interno di VS Code (installazione estensione, creazione/apertura notebook, selezione kernel).
    *   Utilizzo base (esecuzione celle).
*   **Funzioni (approfondimento):**
    *   Definizione di base.
    *   Funzioni con parametri.
    *   Valori di ritorno.
    *   Parametri con valori predefiniti.
    *   *Scope* (ambito) delle variabili (locali).
    *   Valori di ritorno multipli (tuple).
    *   `*args` e `**kwargs` per un numero variabile di argomenti.
    *   Funzioni Lambda (piccole funzioni anonime).
    *   Documentazione delle funzioni (docstring).
*   **Classi (introduzione):**
    *   Definizione di base di una classe (`class`).
    *   Il costruttore `__init__`.
    *   Attributi (dati) e metodi (funzioni) di una classe.
    *   Creazione di istanze (oggetti) di una classe.
*   **Iteratori:**
    *   Concetto di base (`__iter__()`, `__next__()`).
    *   Perché usarli (dataset grandi, flussi di dati).
    *   Iteratori integrati (liste, tuple, dizionari, set).
*   **NumPy (introduzione):**
    *   Cos'è NumPy e i suoi concetti chiave (`ndarray`, vettorizzazione, broadcasting).
    *   Importazione (`import numpy as np`).
    *   Creazione di array (monodimensionali, bidimensionali, `np.zeros`, `np.ones`, `np.eye`, `np.arange`, `np.linspace`).
    *   Operazioni di base (element-wise, statistiche come `np.mean`, `np.std`, `np.min`, `np.max`, algebra lineare come `np.dot`, `np.linalg.det`, `np.linalg.inv`).
    *   Slicing e Indicizzazione di array.
    *   Esempio applicato al contesto biomedico (filtro media mobile, calcolo BMI).
### Lezione 5
La lezione 5 tratta i seguenti argomenti:

*   **Iteratori in Python (approfondimento):**
    *   Concetto di base (`__iter__()`, `__next__()`).
    *   Perché usare gli iteratori (dataset di grandi dimensioni, flussi di dati).
    *   Iteratori integrati.
    *   Creazione di iteratori personalizzati (implementando una classe con `__iter__` e `__next__`).
    *   **Generatori:** Un modo più semplice per creare iteratori utilizzando la parola chiave `yield`.
    *   Funzioni integrate utili per lavorare con iteratori: `map()`, `filter()`, `zip()`.

*   **Ereditarietà (Inheritance) nelle Classi:**
    *   Concetto e vantaggi (riuso del codice, estensione, override, polimorfismo).
    *   Esempio pratico con una classe base `Veicolo` e una classe derivata `Auto`.
    *   Utilizzo di `super()` per richiamare metodi e costruttori della classe madre.

*   **Esercizio sulle Classi:**
    *   Traccia per creare una classe `Studente` con metodi per aggiungere voti, calcolare la media e rappresentare lo studente come stringa.
    *   Suggerimenti per la validazione dei voti e il calcolo della media.

*   **File Handling:** (Menzionato come titolo di sezione, ma il contenuto specifico non è dettagliato nel notebook fornito).

*   **Error Handling (Gestione degli Errori):**
    *   Distinzione tra Errori di Sintassi (`SyntaxError`) ed Eccezioni (`Exceptions`).
    *   Esempi di `SyntaxError` e `ZeroDivisionError`.
    *   **Assertion Error:**
        *   Utilizzo di `raise Exception` per sollevare eccezioni personalizzate.
        *   Utilizzo dell'istruzione `assert` per controlli e debug, con l'avvertenza che le asserzioni possono essere disabilitate.
    *   **Blocco `try...except`:**
        *   Sintassi base per catturare e gestire le eccezioni.
        *   Importanza di catturare eccezioni specifiche (`except NomeEccezione as e:`) invece di un `except` generico.
        *   Gestione di multiple clausole `except` per diversi tipi di errore.
    *   **Clausole `else` e `finally`:**
        *   `else`: blocco di codice eseguito se nessuna eccezione si verifica nel `try`.
        *   `finally`: blocco di codice eseguito sempre, indipendentemente dal fatto che si sia verificata o meno un'eccezione (utile per operazioni di pulizia).
    *   Illustrazione del flusso `try...except...else...finally`.

*   **Riferimenti:** Indicazione di risorse esterne per approfondimenti.

### Lezione 6
La lezione 6 tratta i seguenti argomenti principali:

1.  **Programmazione Orientata agli Oggetti (Esercizio/Continuazione):**
    *   Definizione di una gerarchia di classi (`Persona`, `Esame`, `Studente`) con attributi e metodi specifici, suggerendo un esercizio di implementazione.

2.  **Pandas:**
    *   **Introduzione al Data Wrangling:** Perché Pandas è ideale per la pulizia e trasformazione dei dati.
    *   **Funzionalità Chiave:** Importazione dati (`read_*`), pulizia (`dropna`, `fillna`), ristrutturazione (`melt`, `pivot`), filtraggio (`boolean indexing`, `query`, `groupby`), aggregazione (`groupby().agg()`, `describe`), unione (`merge`, `concat`), gestione di serie temporali.
    *   **Confronto con Liste Python e Array NumPy:** Vantaggi di Pandas per etichette, dati eterogenei, valori mancanti, operazioni SQL-like, time series, I/O, leggibilità.
    *   **Casi d'Uso:**
        *   Analisi di dataset clinici multifattoriali.
        *   Preparazione di file di dati (creazione di `pazienti_demo.csv` e `pazienti_demo.xlsx`).
        *   Esempio pratico: caricamento, visualizzazione (`head()`), statistiche di base (`describe()`), filtraggio.
    *   **Gestione File con Pandas:** Lettura e scrittura di CSV, Excel, JSON, TSV. Integrazione con librerie scientifiche.
    *   **Studi di Coorte Longitudinali:** Esempio di unione (`merge`) di dati baseline e follow-up.

3.  **NumPy (Approfondimento):**
    *   **Vantaggi:** Velocità (implementazione in C), riduzione dei cicli (operazioni vettoriali), codice leggibile, affidabilità.
    *   **Concetti Fondamentali:**
        *   Creazione di array (`np.array`).
        *   `dtype` (tipo di dati dell'array).
        *   **Vettorizzazione e Broadcasting:** Applicazione di operazioni a interi array e allineamento di array con forme diverse. Esempio con la funzione `curve` e `np.clip()`.
        *   **Shape (Forma):** Tupla che descrive le dimensioni (`.shape`), `reshape()`.
        *   **Axes (Assi):** Indicizzazione delle dimensioni, uso del parametro `axis` in funzioni come `.max()`.
        *   **Broadcasting (Dettaglio):** Regole per combinare array di forme diverse, espansione virtuale. Esempi pratici (vettore + matrice, matrice + colonna, scalare).
    *   **Operazioni su Array:**
        *   **Indicizzazione (Indexing):** Slicing (`:`), indici multi-asse (separati da virgola). Esempio con il quadrato magico di Dürer.
        *   **Mascheramento e Filtraggio (Masking & Filtering):** Uso di array booleani per selezionare elementi. Esempi con `np.linspace()`, `rng.standard_normal()`, operatore `&`.
        *   **Trasposizione:** `.T`, `.transpose()`.
        *   **Ordinamento (Sorting):** `np.sort()` con e senza `axis`.
        *   **Concatenazione:** `np.hstack()`, `np.vstack()`, `np.concatenate()`.
        *   **Aggregazione (Aggregating):** Metodi come `.sum()`, `.max()`, `.mean()`, `.std()` con il parametro `axis`.

4.  **Matplotlib (Introduzione alla Visualizzazione):**
    *   **Importazione Standard:** `import matplotlib.pyplot as plt`.
    *   **Gerarchia degli Oggetti:** `Figure` (contenitore), `Axes` (grafico), elementi minori.
    *   **Due Approcci:**
        *   **Statico (pyplot):** Semplice per grafici base (`plt.plot()`, `plt.title()`, ecc.).
        *   **Orientato agli Oggetti:** Più flessibile (`fig, ax = plt.subplots()`, `ax.plot()`, `ax.set_title()`, ecc.).
    *   **Grafici Multipli:** Uso di `plt.subplots()` per creare griglie di grafici (`axes.flatten()`, `fig.tight_layout()`). Esempi: grafico a linee, a dispersione (scatter), istogramma, a barre.
    *   **Personalizzazione dei Grafici:** Stili di linea, colori, `fill_between`, limiti degli assi (`set_xlim`, `set_ylim`), griglia, titoli, etichette, legende, annotazioni.
    *   **Integrazione con Pandas:** Visualizzazione diretta da DataFrame (es. `df.boxplot()`, grafici a barre da dati raggruppati).
    *   **Consigli Utili:** Uso dell'approccio orientato agli oggetti, `tight_layout()`, salvataggio figure (`plt.savefig()`), stili (`plt.style.use()`), `plt.show()`.

### Lezione 7
La lezione 7 introduce **PyTorch** e il suo utilizzo per costruire un classificatore di immagini, concentrandosi sui seguenti argomenti:

1.  **Concetti Fondamentali di Deep Learning:**
    *   **Gradient Descent:** Spiegazione del concetto e delle sue varianti (Batch, Stochastic SGD, Mini-batch).

2.  **Introduzione a PyTorch e Torchvision:**
    *   Installazione di `torch` e `torchvision`.
    *   Ruolo di `torchvision`: fornitura di dataset comuni (es. CIFAR10), funzioni di preprocessing e modelli pre-addestrati.

3.  **Preparazione dei Dati con PyTorch:**
    *   **Trasformazioni (`torchvision.transforms`):**
        *   `transforms.Compose` per concatenare trasformazioni.
        *   `transforms.ToTensor()` per convertire immagini in tensori PyTorch.
        *   `transforms.Normalize()` per normalizzare i valori dei pixel.
    *   **Caricamento Dataset:**
        *   Utilizzo di `torchvision.datasets.CIFAR10` per scaricare e caricare il dataset CIFAR-10.
        *   `torch.utils.data.DataLoader` per creare iteratori (`trainloader`, `testloader`) che forniscono i dati in batch, con opzioni per `batch_size`, `shuffle` e `num_workers`.
    *   Definizione delle classi del dataset.

4.  **Visualizzazione dei Dati:**
    *   Utilizzo di `matplotlib.pyplot` e `numpy` per visualizzare le immagini.
    *   Funzione `imshow` per denormalizzare e mostrare le immagini tensorizzate.

5.  **Definizione di una Rete Neurale Convoluzionale (CNN):**
    *   Utilizzo di `torch.nn` e `torch.nn.functional`.
    *   Creazione di una classe `Net` che eredita da `nn.Module`.
    *   **Costruttore (`__init__`):** Definizione dei layer della rete:
        *   `nn.Conv2d` (layer convoluzionali).
        *   `nn.MaxPool2d` (layer di pooling).
        *   `nn.Linear` (layer fully connected o densi).
    *   **Metodo `forward(self, x)`:** Definizione del flusso dei dati attraverso la rete:
        *   Applicazione delle convoluzioni e pooling.
        *   Funzione di attivazione `F.relu`.
        *   `torch.flatten()` per appiattire i feature map prima dei layer densi.
    *   Spiegazione dettagliata delle dimensioni dei tensori in output da ogni layer.

6.  **Definizione della Funzione di Perdita (Loss Function) e Ottimizzatore:**
    *   **Loss Function:** `nn.CrossEntropyLoss` per problemi di classificazione multi-classe.
    *   **Ottimizzatore:** `torch.optim.SGD` (Stochastic Gradient Descent) con impostazione di `lr` (learning rate) e `momentum`.

7.  **Addestramento della Rete:**
    *   Ciclo di addestramento su più epoche (`epochs`).
    *   Iterazione sui batch di dati forniti dal `trainloader`.
    *   **Passaggi chiave per ogni batch:**
        1.  `optimizer.zero_grad()`: Azzera i gradienti accumulati.
        2.  `outputs = net(inputs)`: Forward pass (calcolo delle predizioni).
        3.  `loss = criterion(outputs, labels)`: Calcolo della loss.
        4.  `loss.backward()`: Backward pass (calcolo dei gradienti).
        5.  `optimizer.step()`: Aggiornamento dei pesi della rete.
    *   Monitoraggio della `running_loss`.

8.  **Salvataggio del Modello Addestrato:**
    *   `torch.save(net.state_dict(), PATH)` per salvare i pesi del modello.

9.  **Test della Rete su Dati Nuovi:**
    *   Caricamento dei pesi del modello salvato: `net.load_state_dict(torch.load(PATH))`.
    *   Ottenere predizioni per un batch di immagini di test.
    *   `torch.max(outputs, 1)` per ottenere la classe predetta.
    *   Valutazione delle prestazioni sull'intero dataset di test:
        *   Utilizzo di `with torch.no_grad():` per disabilitare il calcolo dei gradienti durante l'inferenza.
        *   Calcolo dell'accuratezza totale.
        *   Calcolo dell'accuratezza per ogni singola classe.

10. **Addestramento su GPU (Cenno):**
    *   Verifica della disponibilità di CUDA: `torch.cuda.is_available()`.
    *   Definizione del `device` (`cuda:0` o `cpu`).
    *   (Il notebook menziona come trasferire la rete e i tensori sulla GPU, anche se non lo implementa completamente nel codice mostrato).

11. **Approfondimento sul Layer `Conv2d`:**
    *   Spiegazione dettagliata di come viene calcolata la dimensione dell'output di un layer `Conv2d` in base a: dimensione dell'input (`H_in`, `W_in`), dimensione del kernel (`kernel_size`), `padding` e `stride`.
    *   Relazione tra `out_channels` e il numero di filtri appresi.

### Lezione 8
In questa lezione sono stati presentati diversi spunti per possibili progetti da realizzare, con l'obiettivo di mettere in pratica le competenze acquisite durante il corso.

La filosofia dietro questa proposta è che **il modo migliore per imparare davvero un linguaggio di programmazione e consolidare i concetti è applicarli a un problema pratico**. Non importa la dimensione del progetto: può essere un'idea ambiziosa o una piccola automazione personale. L'importante è scegliere qualcosa che risolva un problema reale o che sia di interesse personale.

Per la prossima volta, l'idea è che ognuno definisca un progetto in modo più dettagliato, specificando:
*   **Librerie da usare:** Quali strumenti Python saranno necessari.
*   **Struttura del progetto:** Come sarà organizzato il codice.
*   **Piano di lavoro:** I passaggi per iniziare e sviluppare il progetto.
*   **Dati da raccogliere:** Che tipo di dati servono, come ottenerli, ecc.

Presentare queste idee al gruppo servirà anche per ricevere suggerimenti e ispirare gli altri.

Ecco i progetti presentati, suddivisi per categoria:

**Progetti Generali:**

1.  **Sito Web con Django:**
    *   **Idea:** Creare applicazioni web complete.
    *   **Esempi:** Mini-portale per appunti, dashboard per report.
    *   **Tool & Skill:** Django, HTML/CSS/JS, database (SQLite/PostgreSQL), Docker (opz.), Pandas, Git.
    *   **Difficoltà:** ⭐⭐
    *   **Tempo stimato:** 20-28 h

2.  **Web Scraper (senza IA):**
    *   **Idea:** Automatizzare il download e l'archiviazione di dati da web o API, con notifiche.
    *   **Esempi:** Tracker prezzi Amazon, bot per ritardi Trenitalia.
    *   **Tool & Skill:** `requests`/`httpx`, `BeautifulSoup4` o `Playwright`, Pandas, `SMTP`/`Telegram-bot`, `cron`/`APScheduler`.
    *   **Difficoltà:** ⭐
    *   **Tempo stimato:** 8-12 h

3.  **Web Scraper con IA:**
    *   **Idea:** Oltre al download, usare l'IA per sintetizzare il contenuto estratto.
    *   **Esempi:** Digest di notizie, agente per bandi universitari.
    *   **Tool & Skill:** Strumenti del #2 + `OpenAI-Python`/`HuggingFace transformers`, `LangChain`, `pdfkit`/`WeasyPrint`.
    *   **Difficoltà:** ⭐⭐⭐
    *   **Tempo stimato:** 16-24 h

4.  **Backup File automatico:**
    *   **Idea:** Sincronizzare cartelle locali o cloud con log dettagliati.
    *   **Esempi:** Backup notturno PDF tesi su Google Drive, mirroring foto telefono su NAS.
    *   **Tool & Skill:** `watchdog`, `pathlib`/`shutil`, `boto3` (AWS) o Google Drive API, `logging`/`rich`, `argparse`.
    *   **Difficoltà:** ⭐
    *   **Tempo stimato:** 4-8 h

5.  **Rinominatore Batch:**
    *   **Idea:** Script da riga di comando per applicare pattern di rinomina a file, con anteprima/undo.
    *   **Esempi:** Rinominare foto (`IMG_...jpg` → `ARRAMPICATA_01.jpg`), uniformare nomi file CSV.
    *   **Tool & Skill:** `argparse` / `click`, `re`, `pathlib`, `tqdm`, `pytest`.
    *   **Difficoltà:** ⭐
    *   **Tempo stimato:** 2-4 h

6.  **Report PDF automatici:**
    *   **Idea:** Creare PDF con tabelle, grafici e calendari generati dinamicamente.
    *   **Esempi:** Resoconto settimanale calorie/passi, planner mensile da Google Calendar.
    *   **Tool & Skill:** Pandas, Matplotlib/Plotly, Jinja2, WeasyPrint / pdfkit, icalendar, cron.
    *   **Difficoltà:** ⭐⭐
    *   **Tempo stimato:** 8-12 h

**Sezione "Biomedico":**

7.  **Classificatore immagini (PyTorch):**
    *   **Idea:** Applicare il transfer-learning su immagini mediche per classificazione.
    *   **Esempi:** RX torace "normale vs polmonite", selezione vetrini istopatologici "buoni vs sfocati".
    *   **Tool & Skill:** PyTorch, torchvision, Albumentations, TensorBoard, metriche (accuracy, AUC).
    *   **Difficoltà:** ⭐⭐
    *   **Tempo stimato:** 16-20 h

8.  **Segmentazione con U-Net (PyTorch):**
    *   **Idea:** Isolare strutture a livello pixel in immagini mediche (es. tumori, organi).
    *   **Esempi:** Contorno fegato in ecografie, segmentazione tumori in MRI cerebrali.
    *   **Tool & Skill:** PyTorch, `segmentation-models-pytorch`, OpenCV, Dice Score, augmentation avanzata.
    *   **Difficoltà:** ⭐⭐⭐
    *   **Tempo stimato:** 20-28 h

9.  **Algoritmo di Reinforcement Learning:**
    *   **Idea:** Addestrare un agente in un ambiente simulato per prendere decisioni continue.
    *   **Esempi:** Robot dosatore farmaco per glicemia, controllo esoscheletro per riabilitazione.
    *   **Tool & Skill:** `gymnasium`, `Stable-Baselines3` (PPO/SAC), PyTorch, `wandb`, `MoviePy`.
    *   **Difficoltà:** ⭐⭐⭐
    *   **Tempo stimato:** 20-28 h

Inoltre, la lezione include un **mini tutorial su Git** per condividere il progetto su GitHub, che comprende:
*   Creazione di un account GitHub.
*   Inizializzazione di un repository Git locale (`git init`, .gitignore, `git add`, `git commit`).
*   Creazione di un repository remoto su GitHub.
*   Collegamento del repository locale a quello remoto e invio del codice (`git remote add`, `git branch -M main`, `git push`).
*   Suggerimenti per scrivere un file README.md con obiettivo del progetto, setup, risultati e idee di miglioramento.

### Lezione 9: Mini-Hackathon, Presentazione Progetti e Chiusura Corso
Quest'ultima lezione è il culmine del percorso di apprendimento: un momento di condivisione, valutazione e celebrazione dei progressi fatti. Sarà strutturata come un "mini-hackathon" in cui ogni partecipante avrà l'opportunità di presentare il proprio progetto finale.

*   **Presentazione dei Progetti Finali (Mini-Hackathon):**
    *   Ogni studente (o gruppo) presenterà il proprio lavoro.
    *   **Formato dei Progetti:** Sono ammessi sia MVP (Minimum Viable Product) funzionanti, sia idee progettuali con specifiche di realizzazione ben definite (obiettivi, architettura, tecnologie, piano di sviluppo).
    *   **Obiettivo della Presentazione:** Illustrare il problema affrontato, la soluzione proposta, le tecnologie utilizzate, le sfide incontrate e i risultati ottenuti (o attesi).
    *   Tempo dedicato a ciascuna presentazione (da definire in base al numero di partecipanti).
    *   Sessione di Q&A e feedback costruttivo da parte dei docenti e degli altri partecipanti.
*   **Valutazione e "Premiazione":**
    *   I progetti saranno valutati in base a criteri come originalità, complessità tecnica, utilità, qualità della presentazione e completezza (per gli MVP) o chiarezza e fattibilità (per le idee progettuali).
    *   Verrà decretato un "progetto migliore" o verranno riconosciuti meriti particolari.
    *   **Premio:** Da definire (es. menzione speciale, piccolo gadget, risorsa formativa aggiuntiva).
*   **Consegna Progetto e Attestato di Partecipazione:**
    *   **Importante:** La consegna del progetto (MVP o specifiche dettagliate) è un requisito necessario per il rilascio dell'attestato di partecipazione al corso. L'impegno profuso è apprezzato, ma la finalizzazione e consegna di *qualcosa* di concreto è fondamentale.
*   **Culture Pill / Contenuti Esterni:**
    *   Spazio per riflessioni finali, condivisione di risorse utili per continuare l'apprendimento, discussione su possibili sviluppi futuri dei progetti.
    *   Eventuale "Lezione sui meme di Python" o altro contenuto leggero e aggregante.
*   **Saluti Finali e Feedback sul Corso:**
    *   Ringraziamenti ai partecipanti.
    *   Momento dedicato alla raccolta di feedback sul corso per miglioramenti futuri.
    *   Saluti e auspici per il futuro percorso nel mondo della programmazione Python.





- - -
# Programmazione Python con Fondamenti di Data Science e Intelligenza Artificiale 
## Descrizione dell’iniziativa
### Obiettivi
- Introdurre sintassi, paradigmi e best practice di Python dal terminale alla programmazione a oggetti.  
- Sviluppare capacità di problem-solving algoritmico applicando strutture dati, funzioni, classi e librerie scientifiche.  
- Fornire un primo toolkit per Data Science (NumPy, Pandas, Matplotlib) e un assaggio di deep learning (PyTorch).  
- Abituare a un workflow professionale: Linux/WSL, virtual-env, VS Code, versionamento Git.  
- Potenziare soft-skills: lavoro di squadra, gestione di progetto, public speaking tecnico.  
### Strumenti didattici
- **Ambiente:** WSL + Ubuntu o macOS Terminal, VS Code con estensioni Python/Git.  
- **Stack:** Python 3.12, venv/pip, NumPy, Pandas, Matplotlib, PyTorch (intro), Markdown per i report.  
- **Metodologia:** lezioni brevi alternate a micro-challenge “Problema”, sessioni hands-on, “Culture Pill” (pillole su etica, storia e community open-source, progetti Python di esperti, ecc.).  
### Criteri di superamento

| Requisito                                       | Soglia                              | Obbligo       |
|-------------------------------------------------|-------------------------------------|---------------|
| Frequenza                                       | ≥ 75 % (≥ 7 su 9 lezioni)           | Obbligatoria  |
| Progetto finale (singolo o in team)             | MVP funzionante **oppure** tech-report dettagliato | Obbligatorio  |

### Perché partecipare?
Imparerai a trasformare un’idea in un MVP funzionante, acquisendo competenze Python immediatamente spendibili in tesi, stage e progetti personali.

## Informazioni logistiche
- **Lingua di erogazione:** Italiano  
- **Crediti formativi universitari (CFU):** 2 CFU (≈ 50 h)  
- **Ore in aula:** 19 h  
- **Tipologia di attività:** laboratorio progettuale, laboratorio informatico, didattica frontale, competizioni  
- **Numero massimo di studenti:** 70  
### Conoscenze o abilità richieste
Eventuali prerequisiti di programmazione di base (logiche, variabili, strutture di controllo).

> **Criteri di selezione:** ordine di arrivo (salvo diversa indicazione del docente).
### Validazione del corso
Vedi “Criteri di superamento” sopra.
### Sede e spazi
- **Spazi previsti:** aula di Ateneo, online  
- **Campus:** Leonardo  
- **Aula:** da confermare (richiesta aula in Leonardo)  
### Periodo
**Inizio – fine:** Ottobre 2025 – Dicembre 2025  
**Prima lezione (stimata):** **Lun 06/10/2025**
### Calendario (provvisorio)

| Data       | Giorno | Orario      |
|------------|--------|------------|
| 06/10/2025 | Lun    | 17:30–19:30 |
| 08/10/2025 | Mer    | 17:30–19:30 |
| 13/10/2025 | Lun    | 17:30–19:30 |
| 15/10/2025 | Mer    | 17:30–19:30 |
| 22/10/2025 | Mer    | 17:30–19:30 |
| 12/11/2025 | Mer    | 17:30–19:30 |
| 19/11/2025 | Mer    | 16:30–19:30 |
| 26/11/2025 | Mer    | 17:30–19:30 |
| 03/12/2025 | Mer    | 17:30–19:30 |
**Nota:** Questo orario è stato scelto per affrontare gli argomenti già visti in altri corsi di programmazione velocemente e lasciare più tempo tra una volta e l'altra per argomenti più difficili o relativi unicamente a python. La lezione di tre ore è una lezione speciale su reti neurali e fondamenti di Deep Learning.
### Parole chiave / Tags
Python , AI , Machine Learning , Data Science , Programming , Challenge , Course
- - -
## Lezioni nel Dettaglio
### Lezione 0: Installazione software
Non è una vera e propria lezione ma semplicemente verrà mandato un file con una guida da svolgere prima del corso, per avere tutto installato. In questo modo nella lezione 1 si risolvono i problemi di chi non è riuscito e si evitano perdite di tempo.
### Lezione 1: Introduzione e Configurazione Ambiente
*   Configurazione Ambiente di Sviluppo (WSL per Windows).
*   Introduzione al Corso: obiettivi, struttura, progetto finale (PyTorch).
*   Vantaggi di un ambiente UNIX-like (Linux/macOS).
*   Il Terminale: installazione, gestione pacchetti, comandi essenziali (`ls`, `cd`, `mkdir`, `nano`, ecc. ).
*   Esercitazione pratica con il terminale.
*   Visual Studio Code (VS Code): introduzione e configurazione.
*   Introduzione a Python: caratteristiche, filosofia, interprete interattivo.
*   Culture Pill: The Zen of Python.

### Lezione 2: Tipi di Dati e Controllo del Flusso
*   Tipi di Dati Fondamentali (Parte 1):
    *   Booleans (`bool`): valori, operatori logici.
    *   Integers (`int`): numeri interi, operatori aritmetici.
    *   Floats (`float`): numeri decimali, operazioni.
    *   Stringhe (`str`): creazione, operazioni base, indicizzazione, slicing, metodi comuni.
*   Strutture Condizionali: `if`, `elif`, `else` (sintassi, indentazione, esempi).
*   Tipi di Dati Fondamentali (Parte 2):
    *   Liste (`list`): sequenze mutabili, creazione, accesso, modifica, metodi comuni.
*   Cicli Iterativi: Il Ciclo `for` (iterare su sequenze, `range()`).
*   Esercizi pratici su tipi di dati, condizionali e cicli.

### Lezione 3: Strutture Dati Complesse, Cicli Avanzati e Funzioni
*   Matrici: creazione e manipolazione con liste annidate.
*   Cicli `for` (approfondimento).
*   Cicli `while`: iterazioni basate su condizione (es. serie di Fibonacci, simulazione termometro).
*   Funzioni: definizione, parametri, valori di ritorno, argomenti di default e keyword, gestione argomenti mutabili.
*   Tipi di Dati Avanzati:
    *   Dizionari (`dict`): creazione, accesso, modifica, metodi, iterazione, comprensioni.
    *   Tuple (`tuple`): creazione, immutabilità, indicizzazione, unpacking.
    *   Set (`set`): introduzione e operazioni di base.
*   Esercizi Pratici: visualizzazione matrici, simulazione termometro, gestione dati strutturati.

### Lezione 4: Ambienti Virtuali, Jupyter, Funzioni Avanzate, Classi e NumPy
*   Ambienti Virtuali: utilità, `venv` (creazione, attivazione, gestione dipendenze).
*   Jupyter Notebook: introduzione, installazione, utilizzo base (anche in VS Code).
*   Funzioni (approfondimento): scope, valori di ritorno multipli, `*args`, `**kwargs`, funzioni Lambda, docstring.
*   Classi (introduzione): definizione (`class`), costruttore `__init__`, attributi, metodi, istanze.
*   Iteratori: concetto (`__iter__`, `__next__`), utilità.
*   NumPy (introduzione): `ndarray`, vettorizzazione, broadcasting, creazione array, operazioni base, slicing, indicizzazione (se non si finisce si sposta alla lezione successiva).

### Lezione 5: Iteratori Avanzati, Ereditarietà, File Handling e Gestione Errori
*   Iteratori (approfondimento): creazione personalizzata, Generatori (`yield`), funzioni `map()`, `filter()`, `zip()`.
*   Ereditarietà nelle Classi: concetto, vantaggi, `super()`.
*   Esercizio sulle Classi: implementazione classe `Studente`.
*   File Handling (cenni).
*   Error Handling (Gestione degli Errori): `SyntaxError` vs `Exceptions`, `AssertionError`, `raise Exception`, `assert`, blocco `try...except...else...finally` (se non si finisce si sposta alla lezione successiva).

### Lezione 6: OOP Avanzata, Pandas, NumPy Avanzato e Matplotlib
*   Programmazione Orientata agli Oggetti (OOP): esercizio su gerarchia di classi (`Persona`, `Esame`, `Studente`).
*   Pandas:
    *   Data Wrangling: importazione, pulizia, ristrutturazione, filtraggio, aggregazione, unione dati.
    *   Gestione File: CSV, Excel, JSON.
*   NumPy (approfondimento) (se non si finisce va nella lezione buffer):
    *   Concetti: `dtype`, vettorizzazione, broadcasting, shape, axes.
    *   Operazioni: indicizzazione avanzata, masking, trasposizione, ordinamento, concatenazione, aggregazione.
*   Matplotlib (Introduzione alla Visualizzazione) (se non si finisce va nella lezione buffer):
    *   Gerarchia oggetti (`Figure`, `Axes`), approccio statico vs. orientato agli oggetti.
    *   Creazione grafici multipli, personalizzazione, integrazione con Pandas.

### Lezione 7: Introduzione a PyTorch per il Deep Learning (Lezione speciale da 3 ore)
*   Concetti Fondamentali di Deep Learning: Spiegazione dei vari algoritmi, applicazioni e di dove si colloca all'interno del Machine Learning.
*   Introduzione alle reti neurali, percettrone, rete neurale, forward and backward propagation, Gradient Descent (intuitivamente), preparazione dei dati e divisione del dataset.
*   Introduzione a PyTorch e Torchvision: installazione, dataset, trasformazioni.
*   Preparazione Dati: `torchvision.transforms`, `torchvision.datasets.CIFAR10`, `DataLoader`.
*   Visualizzazione Dati con `matplotlib`.
*   Definizione Rete Neurale Convoluzionale (CNN): `nn.Module`, `nn.Conv2d`, `nn.MaxPool2d`, `nn.Linear`, metodo `forward`.
*   Funzione di Perdita (`nn.CrossEntropyLoss`) e Ottimizzatore (`torch.optim.SGD`).
*   Addestramento Rete: ciclo epoche, forward/backward pass, aggiornamento pesi.
*   Salvataggio e Test del Modello: `torch.save`, `load_state_dict`, calcolo accuratezza.
*   Cenni su addestramento GPU e layer `Conv2d`.
*   È molto da presentare in una sola lezione, se non si finisce va nella lezione buffer!
**Presentazione Progetti Pratici**
*   Filosofia: importanza dell'applicazione pratica per l'apprendimento.
*   Proposte di Progetti (Generali e Biomedici):
    *   Sito Web con Django, Web Scraper (con/senza IA), Backup automatico, Rinominatore Batch, Report PDF, ecc.
    *   Classificatore immagini (PyTorch), Segmentazione U-Net (PyTorch), Reinforcement Learning, ecc.

### Lezione 8: (Lezione Buffer) Aiuto per i Progetti e Introduzione a Git/GitHub
-   Si seguono i ragazzi nei loro progetti individualmente, si approfondiscono eventuali argomenti che non sono stati trattati per mancanza di tempo nelle lezioni precedenti
*   Mini tutorial su Git e GitHub: `init`, `add`, `commit`, `push`, `README.md`.

### Lezione 9: Mini-Hackathon, Presentazione Progetti e Chiusura Corso
*   Presentazione Progetti Finali: MVP o idee progettuali dettagliate.
*   Valutazione Progetti e "Premiazione".
*   Consegna Progetto come requisito per attestato.
*   Riflessioni finali, risorse per apprendimento continuo.
*   Saluti e raccolta feedback sul corso.


### Note
Alla fine di ogni lezione potrebbe esserci una *culture pill* su python o in alternativa un intervento di qualche professore o dottorando che sta usando python per applicazioni di ricerca o aziendali. Questo per dare esempi pratici di come usare python nella propria carriera accademica e lavorativa, fornendo anche spunti sulla filosofia dietro il linguaggio di programmazione e la sua comunità *open-source*.