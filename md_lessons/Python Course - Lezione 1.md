# Lezione 1 – Ambiente di lavoro, Jupyter Notebook, ambienti virtuali e introduzione a Python

## Intro (20 min)

1) *Cos’è Python*  
Python è un linguaggio di programmazione ad alto livello, interpretato e multi-paradigma. In pratica: ha una sintassi abbastanza leggibile da permettere di concentrarsi più sul problema che sulla "burocrazia" del linguaggio. Per questo è una scelta molto comune sia per chi inizia sia per chi lavora già in automazione, analisi dati, machine learning e ricerca.

2) *Cosa significa interpretato?* 
A livello introduttivo, la differenza utile è questa:
- in un linguaggio compilato (es. C, C++) il codice sorgente viene tradotto in un file eseguibile *prima* dell'esecuzione;
- in Python il codice viene eseguito tramite un interprete, quindi di solito scrivi un file `.py` e lo lanci con `python3 nome_file.py`.

Questo rende Python molto comodo per fare prove rapide, esercizi e prototipi. Il rovescio della medaglia è che, in generale, non è il linguaggio più veloce in assoluto.
*Se vuoi un'immagine mentale: il compilatore ti consegna il testo già tradotto; l'interprete traduce mentre "parla". Il primo è in genere più efficiente, il secondo più flessibile per lavorare in modo interattivo.*

3) *Perché Python*  
• **Semplicità e velocità di sviluppo**: La sintassi chiara e la ricca collezione di librerie permettono di realizzare progetti in meno tempo rispetto ad altri linguaggi.  
• **Comunità e risorse**: Python ha un’enorme community di sviluppatori, quindi è facile trovare guide e risolvere problemi, soprattutto nei campi più specialistici come la scienza dei dati e la bioinformatica.  
• **Versatilità**: Python si usa in tantissimi ambiti, dal web development (Django, Flask), all’analisi dati e Machine Learning (pandas, NumPy, scikit-learn, PyTorch), fino ad applicazioni embedded (seppure meno frequenti).  
• **Integrazione con altri linguaggi**: Python può interfacciarsi con librerie in C/C++ e Java, sfruttando così performance e compatibilità già esistenti.
Le sue strutture dati integrate di alto livello, combinate con la tipizzazione dinamica (cioè il tipo di una variabile viene determinato durante l’esecuzione) e il binding dinamico, lo rendono molto attraente per lo Sviluppo Rapido di Applicazioni (RAD), nonché per l’uso come linguaggio di scripting o “collante” per collegare componenti esistenti. La sintassi semplice e facile da imparare di Python enfatizza la leggibilità e riduce quindi i costi di manutenzione del programma.
Python funge da “colla” che delega certe funzioni a pacchetti scritti in C.
Python supporta moduli e pacchetti, che favoriscono la modularità del programma e il riutilizzo del codice. L’interprete Python e l’estesa libreria standard sono disponibili in forma sorgente o binaria senza costi per tutte le principali piattaforme e possono essere liberamente distribuiti.
4) *Come useremo Python nel corso*  
• **Installazione:** In ambiente Linux/Ubuntu, è spesso pre-installato o facile da aggiungere tramite apt-get. In macOS si può installare con Homebrew o scaricando il pacchetto ufficiale, mentre in Windows è necessario scaricarlo dal sito ufficiale o tramite Microsoft Store (o usare WSL, come previsto dal corso).  
• **Editor e terminale:** Scriveremo file `.py`, li lanceremo da riga di comando e useremo Visual Studio Code come ambiente principale.  
• **Jupyter Notebook:** Lo useremo quando ha senso lavorare in modo interattivo, per fare prove, esperimenti e piccole analisi.  
• **Virtual environment:** Gestiremo le dipendenze con `venv`, così ogni progetto avrà il suo spazio isolato.

5) *Esempi di Python in ambito biomedico*  
• **Analisi di dati clinici**: Python è molto utilizzato per analizzare dataset di pazienti, estrarre statistiche grazie a librerie di data science e anche per la creazione di modelli di Machine Learning in ambito diagnostico o predittivo (ad esempio, previsione di complicanze post-operatorie).  
• **Elaborazione di immagini medicali**: Con OpenCV, SimpleITK o librerie di deep learning, si possono processare immagini di TAC, risonanze magnetiche o radiografie. Python facilita la prototipazione rapida di algoritmi per la segmentazione o il riconoscimento di patologie.  
• **Modellazione e simulazioni:** Per la modellazione computazionale di processi biologici (dalla struttura proteica fino alla cinetica di farmaci), esistono librerie in Python che semplificano la creazione e il test di modelli matematici e statistici.  
• **Bioinformatica:** Librerie come Biopython aiutano nell’analisi di sequenze di DNA/RNA, nell’interazione con database di proteine e di geni e nel parsing di formati di file standard come FASTA, GenBank, ecc.


6) *Pro e contro di Python*  
- Punti di forza:  
	- Facile da imparare e molto leggibile, ideale per prototipazione rapida.  
	- Eccellente ecosistema di librerie (soprattutto per data science e bioinformatica). 
	- Community e documentazione vastissime, risolve i problemi più comuni in modo immediato.  
  
- Limiti e svantaggi:  
    - **Performance**: Python è solitamente più lento di C++ o Java. In molti casi, tuttavia, questo deficit si supera accedendo a librerie ottimizzate in C/C++ (la parte più pesante gira in nativo, mentre Python funge “solo” da interfaccia).  
    - **Non è il più adatto agli ambienti embedded con memoria molto ridotta**, anche se esiste MicroPython per dispositivi particolarmente limitati.  
    - La gestione dell’ambiente (versioni e dipendenze) può diventare complessa se non ci si organizza bene, soprattutto quando si lavora su più progetti contemporaneamente.

In sintesi, Python si rivela un linguaggio flessibile, potente e molto comprensibile, con una curva di apprendimento amichevole e un ecosistema di strumenti concepiti per la ricerca scientifica e il settore biomedico.


#### Dove cercare aiuto quando qualcosa non funziona
- Documentazione ufficiale
- Stack Overflow
- Siti vari, ma confrontando sempre più fonti
- ChatGPT (può essere utile, ma se ci si appoggia troppo presto rischia di rendere l’apprendimento più frustrante: ricompensa immediata, comprensione meno solida)

## Setup (60 min)

Guida di supporto: [Python Installation Guide.pdf](Python%20Installation%20Guide.pdf)
### Windows

**Installare WSL:**

Usa una versione leggermente diversa da quella che abbiamo visto noi. Provare a seguire il tutorial dall'inizio in caso di problemi. Prima di arrendersi al proprio destino provate a riavviare il computer, a molti ha risolto i problemi.
https://learn.microsoft.com/en-us/windows/wsl/install


**Installare Python:**

```bash
sudo apt update
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

### Perché Linux

- perché è lo standard in tanti contesti tecnici, dai server ai cluster di calcolo;
- perché per progetti embedded e ambienti HPC lo incontreremo spesso;
- perché è molto versatile e si presta bene all'automazione;
- perché ha una curva di apprendimento un po' più ruvida, quindi affrontarlo con qualcuno all'inizio aiuta parecchio.

- Nel campo biomedico, molti dispositivi e strumenti diagnostici implementano sistemi operativi Linux, sfruttandone la stabilità e la versatilità.
- L'ecosistema open-source di Linux offre grande trasparenza e possibilità di personalizzazione, una caratteristica importante per la ricerca.

**Esempi di Linux in ambito biomedico**

1) Sistemi di analisi e modellazione di dati clinici su Linux in ambiente HPC (High Performance Computing)  
	- In un laboratorio di ricerca biomedica, capita di dover processare grandi moli di dati, come immagini di risonanza magnetica (MRI), dati di genomica o sequenziamenti di DNA (NGS). Per elaborare questi dataset in modo efficiente, si utilizzano server Linux dotati di GPU e altre risorse ad alte prestazioni.  
	- I software bioinformatici più usati (ad esempio, diversi tool per l’analisi del DNA e dell’RNA) sono spesso sviluppati o ottimizzati per Linux, il che riduce problemi di compatibilità e aumenta la stabilità dell’ambiente di lavoro.  
	- La facilità di automazione (tramite script Bash o Python) rende Linux molto adatto a pipeline complesse di analisi, in cui i dati passano attraverso vari passaggi (pulizia, filtraggio, allineamento, analisi statistica, ecc.).

2) Utilizzo di Raspberry Pi o sistemi embedded basati su Linux per dispositivi di monitoraggio o analisi diagnostica  
	- Un Raspberry Pi o un’altra scheda embedded (come BeagleBone, Jetson Nano, o simili) può essere impiegato come cervello “low cost” di piccoli dispositivi biomedici, ad esempio per monitorare parametri vitali di un paziente.
	- Nel campo della telemedicina, un sistema embedded Linux può raccogliere dati tramite sensori (pressione arteriosa, battito cardiaco, temperatura corporea) e inviarli in modo sicuro a un server remoto, permettendo un monitoraggio costante anche fuori dall’ospedale.  
	- Grazie alla natura open-source di Linux, è possibile customizzare il sistema operativo e installare soltanto ciò che serve, ottimizzando prestazioni e consumo energetico. Questo risulta prezioso se il dispositivo deve funzionare a batteria o in contesti con risorse limitate.

3) Laboratori di ricerca che gestiscono grandi volumi di dati (sequenziamento del DNA, elaborazione di immagini mediche) con software ottimizzati per Linux  
	 - I laboratori che si occupano di genomica, proteomica o imaging biologico utilizzano software specializzati (come BLAST, Bowtie, GATK per genetica, oppure ANTs, FSL per neuroimaging). Questi tool sono spesso nativi per Linux o vantano performance migliori su Linux grazie a dipendenze e librerie ottimizzate.  
	- In molti casi, i laboratori dispongono di cluster di calcolo interni o si appoggiano a servizi cloud – quasi sempre basati su distribuzioni Linux – per eseguire analisi a elevato carico computazionale.  
	- Lavorare in Linux semplifica anche l’automazione di processi ripetitivi (con cron job, script Bash/Python, container Docker, ecc.), un vantaggio notevole in pipeline sperimentali lunghe e cicliche.

In sintesi, i punti chiave sono l’elevata efficienza, la flessibilità e la stabilità che Linux offre in molti settori biomedici: dalla ricerca di base (analisi bioinformatiche, HPC) allo sviluppo di piccoli dispositivi embedded e strumenti di telemedicina.

**Cos'è Ubuntu**

Ubuntu è una distribuzione Linux particolarmente user-friendly e diffusa, ideale per chi desidera avvicinarsi al mondo Linux. Offre un ciclo di aggiornamenti stabile, un vasto supporto della community e un’ampia disponibilità di software precompilato, inclusi molti strumenti bioinformatici.


## Linux Commands 101

Questa sezione è una guida rapida ai comandi base di Linux. Gli esempi sono pensati per essere eseguiti in sequenza, utilizzando un file `prova.txt` che creeremo e modificheremo. Non serve impararli tutti a memoria oggi: l'obiettivo è iniziare a orientarsi.

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

**`touch`:** Crea un file vuoto. Se il file esiste già, ne aggiorna la data di modifica. Storicamente nasce per aggiornare il timestamp, ma nella pratica si usa spesso anche per creare file vuoti al volo.
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
*Nasce per essere usato con più file, con una sintassi del tipo:* 
```bash
cat file1 file2 
```
*Però in pratica si usa continuamente anche per leggere rapidamente un file singolo.*
 
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
>*Di nuovo: il caso "rinomina" è un uso comodissimo di un comando pensato soprattutto per spostare file. La sintassi generale è:*
```bash
mv nome_file_originale cartella_target/nuovo_nome_file
```
>*Se non specifichi una cartella target, lo puoi usare per cambiare nome al file. Se non cambi il nome, l'effetto è solo lo spostamento.*

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
>*Si può anche usare `rm` per rimuovere una directory e tutto il suo contenuto, ma qui bisogna fare ancora più attenzione. Serve l'opzione `-r` ("recursive"):*
```bash
rm -r appunti_python
```

**`man` (Manual):** Mostra il manuale di un comando, spiegando come funziona e quali opzioni ha. Per uscire, premi `q`.
```bash
man ls
```

**`sudo` (Super User Do):** Esegue un comando con i privilegi di amministratore. È necessario per operazioni di sistema, come installare software.
```bash
sudo apt-get update
```
#### Gestione dei pacchetti
- - -
Come gestire i pacchetti software da command line. 

>[! warning] Attenzione!
>Per chi usa mac è necessario aver installato homebrew!

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
|                                  |                                                                                                    |                                 |


## Visual Studio Code (15 min)
**Windows**
1. Installa [Visual Studio Code](https://code.visualstudio.com/Download).
2. Cerca il terminale (`Windows + S`)
	![](attachment/99216af86ab123fa9fb2afaeeec4d448.png)
3. Scegli ubuntu 2024-4.1 LTS dal menù a tendina
	![](attachment/8746bdc7feaed470ab3f172228dfc575.png)
4. Vai nella cartella python course:
	`cd python_course`
5. Avvia Visual Studio Code in quella cartella
	`code .`
	Dovrebbe partire un download di un server che connette Visual Studio Code a WSL: in questo modo VS Code gira su Windows modificando i dati in Linux.

6. Cliccare nella barra a sinistra sull'icona estensioni 
![](attachment/29eefb4da27cd8021280634e57b146f5.png)
7. Cercare python nella barra di ricerca ed installare le seguenti estensioni (Python + Jupyter)
![](attachment/aef99a4d055e83109f0f00048b70334f.png)

8. Crea un nuovo file `.py` (per esempio `hello.py`) e scrivi un `print("Ciao")`
9. Eseguilo da VS Code
10. Nota che si può accedere al terminale da VS Code alzando la tendina in fondo alla videata

**MAC**

1. [Scarica Visual Studio Code](https://go.microsoft.com/fwlink/?LinkID=534106) per macOS.
2. Apri l'elenco dei download del browser e individua l'app o l'archivio scaricato.
3. Se è un archivio, estrai il contenuto. Usa il doppio clic per alcuni browser o seleziona l'icona della 'lente d'ingrandimento' con Safari.
4. Trascina `Visual Studio Code.app` nella cartella **Applicazioni**, rendendolo disponibile nel Launchpad di macOS.
5. Apri VS Code dalla cartella **Applicazioni**, facendo doppio clic sull'icona.

Puoi anche eseguire VS Code dal terminale digitando `code` dopo averlo aggiunto al percorso:
- Avvia VS Code.
- Apri la **Command Palette** (Cmd+Shift+P) e digita `shell command` per trovare il comando **Shell Command: Install 'code' command in PATH**.
- Riavvia il terminale affinché il nuovo valore `$PATH` abbia effetto. Potrai digitare `code .` in qualsiasi cartella per iniziare a modificare i file in quella cartella.

> **Nota:** Se hai ancora il vecchio alias `code` nel tuo `.bash_profile` (o equivalente) da una versione precedente di VS Code, rimuovilo e sostituiscilo eseguendo il comando **Shell Command: Install 'code' command in PATH**.

[Se non funziona, provare a copiare ed incollare nel terminale questi comandi](https://code.visualstudio.com/docs/setup/mac#_alternative-manual-instructions).

6. Cliccare nella barra a sinistra sull'icona estensioni 
![](attachment/29eefb4da27cd8021280634e57b146f5.png)
7. Cercare python nella barra di ricerca ed installare le seguenti estensioni (Python + Jupyter)
![](attachment/aef99a4d055e83109f0f00048b70334f.png)
8. Crea un nuovo file `.py`
9. Eseguilo da VS Code
10. Nota che si può accedere al terminale da VS Code alzando la tendina in fondo alla videata

---

## Ambienti Virtuali (venv) (15 min)

Un **ambiente virtuale** isola le dipendenze di un progetto Python. Evita che le librerie di un progetto "inquinino" quelle di un altro, e ti permette di avere versioni diverse delle stesse librerie in progetti diversi.

>*Esempio: il progetto A usa `numpy 1.26`, il progetto B ha bisogno di `numpy 2.0`. Senza venv, scontro garantito.*

### Creare e attivare

```bash
# 1. Creare l'ambiente (viene creata una cartella .venv nel progetto)
python3 -m venv .venv

# 2. Attivarlo (Linux / Mac / WSL)
source .venv/bin/activate

# 2b. Attivarlo (Windows PowerShell)
.venv\Scripts\Activate.ps1
```

Quando è attivo, il prompt del terminale cambia e mostra `(.venv)` all'inizio.
Da quel momento, i comandi `python` e `pip` puntano all'ambiente virtuale attivo e non all'installazione globale del sistema.

### Installare pacchetti

```bash
pip install numpy pandas matplotlib
```

I pacchetti finiscono dentro `.venv/`, **non** nel sistema globale.

### Salvare e ripristinare le dipendenze

```bash
pip freeze > requirements.txt     # congela la lista attuale in un file
pip install -r requirements.txt   # reinstalla tutto da zero
```

`requirements.txt` va versionato in git, così chi clona il progetto può ricreare l'ambiente identico al tuo.

### Uscire

```bash
deactivate
```

> **Convenzione:** chiama la cartella del venv `.venv` (col punto), aggiungila al `.gitignore` e non versionarla — è legata alla singola macchina. Va versionato solo `requirements.txt`.

---

## Jupyter Notebook (10 min)

Un **Jupyter Notebook** è un file `.ipynb` fatto di **celle**: ogni cella contiene codice Python oppure testo in Markdown. Esegui una cella alla volta e vedi subito sotto l'output (numeri, tabelle, grafici). È lo strumento di elezione per analisi dati, sperimentazione rapida e presentazione di risultati.

### Installazione
Dentro il venv attivo:
```bash
pip install notebook ipykernel
```

### Due modi per usarli
- **Da VS Code** (consigliato): crea un file `.ipynb`, apri, in alto a destra seleziona il kernel Python (quello del tuo `.venv`) e premi ▶️ su una cella.
- **Da terminale**:
  ```bash
  jupyter notebook
  ```
  Apre il server locale nel browser.

### Tipi di cella
- **Code** → esegue Python, l'output appare subito sotto.
- **Markdown** → testo formattato (titoli, liste, immagini, formule LaTeX).

### Scorciatoie utili
| Tasto                | Effetto                                 |
| -------------------- | --------------------------------------- |
| `Shift + Invio`      | Esegue la cella e passa alla successiva |
| `Ctrl + Invio`       | Esegue la cella senza spostarsi         |
| `Esc` poi `M`        | Trasforma la cella in Markdown          |
| `Esc` poi `Y`        | Trasforma la cella in codice            |
| `Esc` poi `A` / `B`  | Nuova cella sopra / sotto               |

### Attenzione all'ordine di esecuzione
Le variabili rimangono in memoria tra una cella e l'altra. Se esegui le celle fuori ordine rischi risultati incoerenti. Se qualcosa sembra sbagliato: **Kernel → Restart & Run All**.

### Quando usarlo (e quando no)
- ✅ Esplorazione dati, grafici, prototipi, tutorial, condivisione di analisi.
- ❌ Software in produzione, pipeline automatiche, applicazioni: meglio script `.py` o moduli.

### Check finale rapido
A fine lezione dovresti riuscire a:
- aprire la cartella del corso con `code .`;
- verificare l'installazione con `python3 -V`;
- creare e attivare `.venv`;
- installare almeno un pacchetto con `pip`;
- eseguire un file `.py` o una cella Jupyter usando il kernel corretto.

Per esercitarti in autonomia: [Lezione 1 - Esercizi](Python%20Course%20-%20Lezione%201%20-%20Esercizi.md)
