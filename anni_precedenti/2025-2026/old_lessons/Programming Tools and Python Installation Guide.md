## Setup (30 min)

Benvenuti al Python Crush Course 2.0! Mi presento a distanza attraverso questa guida che spero sia chiara per tutti, nel caso non lo fosse scrivetemi pure in privato su WhatsApp che la aggiorno con eventuali chiarimenti. 

Sono Andrea Tosi (Ing. Automazione) e terrò il corso con l'aiuto Giacomo Massolini (Ing. Biomedica), ma avremo modo di conoscerci meglio a lezione.

Con questa guida avremo installato il 70% del software necessario. Se avete dubbi riguardo al motivo per cui stiamo installando certi programmi, annotateli e ponetemi le domande di persona alla prima lezione.

Iniziamo.

Chi ha Windows segua il tutorial per Windows, più in giù c'è anche quello per MAC.



### Windows

WSL (Windows Subsystem for Linux) è un componente di Windows che ti permette di eseguire un ambiente Linux direttamente su Windows, senza bisogno di macchine virtuali o dual boot.

Linux offre vantaggi chiave per ingegneri: migliore supporto per strumenti scientifici (R, Python), software di elaborazione immagini e applicazioni bioinformatiche; accesso a numerosi software open-source non disponibili su sistemi proprietari; compatibilità con server di ricerca; e potenti funzionalità di automazione per gestire dataset biomedici, ecc.

Vedremo meglio a lezione perché utilizzare Linux può essere vantaggioso, ma possiamo anticipare che WSL offre il meglio di entrambi i mondi: l'interfaccia familiare di Windows unita alla potenza e agli strumenti scientifici di Linux, il tutto senza la necessità di riavviare il computer o gestire due sistemi operativi separati.

1. Controlla la versione di Windows:
   • Hai bisogno di Windows 10 versione 2004 (Build 19041) o successiva, oppure Windows 11.
   • Per verificare, premi il tasto Windows → digita "winver" → premi Invio.
   • Se hai una versione precedente, consulta le istruzioni di "installazione manuale" nel link Microsoft.

2. Installare Windows Terminal (se non già presente)
	-  Si tratta semplicemente di una versione del terminale con più funzionalità (diminuisce drasticamente il numero di imprecazioni)![](attachment/923bd893e205f4d8f513f0e49fb4ff6a.png)

3. Apri PowerShell o Prompt dei comandi come Amministratore:
   - Clicca sul pulsante Start → digita "PowerShell" (o "Prompt dei comandi").
   - Fai clic destro su Windows PowerShell (o Prompt dei comandi) → seleziona "Esegui come amministratore".
   - Accetta eventuali richieste di autorizzazione. ![](attachment/9b0f4d1da7f4e1482dd288c12d3bc216.png)

5. Esegui il comando di installazione:
    - Nella finestra Amministratore, digita: wsl --install
    - Premi Invio.
    - Questo comando abilita automaticamente i componenti WSL e installa Ubuntu per impostazione predefinita (puoi cambiarlo in seguito se desideri un'altra distribuzione Linux).

4. Riavvia il computer:
    - Lascia che Windows finisca di installare le funzionalità richieste.
    - Ti verrà chiesto di riavviare. Procedi con il riavvio.

5. Completa la configurazione di Linux:
    - Dopo il riavvio, potrebbe aprirsi una finestra della console per finalizzare la configurazione di Ubuntu (o qualsiasi distribuzione tu abbia scelto).
    - Ti verrà chiesto di creare un nome utente e una password per il tuo ambiente Linux. Assicurati di ricordarli!
	- **NOTA BENE CHE LA PASSWORD NON SI VEDE!** Anche se ti sembra di non stare scrivendo ubuntu sta registrando l'input della tastiera.

7. Installa l'ultima versione disponibile di Ubuntu (ubuntu è uno dei sistemi operativi basati su linux):
   • Per vedere le distribuzioni disponibili: `wsl --list --online (o wsl -l -o)`
   • Per installarne una: `wsl --install -d <NomeDistribuzione>` (sostituisci `<NomeDistribuzione>` con Ubuntu, Debian, ecc.)
	1. ![](attachment/d5aa170a488b4ae010f07d20c0430772.png) Usare la colonna NAME e non FRIENDLY NAME per l'installazione

8. Verifica la versione di WSL:
   • Puoi controllare le distribuzioni installate e le loro versioni WSL con: `wsl -l -v`
   • Per impostazione predefinita, una nuova installazione utilizza WSL 2.

9. (Opzionale) Se dovessi avere per qualche motivo imperscrutabile WSL1, passa a WSL2 in questo modo:
   • Per convertire una distribuzione specifica a `WSL 2: wsl --set-version <nomeDistro> 2` (al posto di nome distro metti la versione di ubuntu installata)
   • Per impostare WSL 2 come predefinito per le future installazioni: `wsl --set-default-version 2`

Ecco fatto! Ora hai Linux in esecuzione su Windows tramite WSL. Una volta configurato, potrai aprire il terminale Linux tramite il menu Start (digitando il nome della distribuzione, ad esempio "Ubuntu"), utilizzando i comandi wsl in PowerShell o Prompt dei comandi *o semplicemente aprendo il Windows Terminal installato nel punto 2 e cercando ubuntu nel menù a tendina*.
![](attachment/c460e71d85bac22b64ca98c750948561.png)

##### In caso di problemi...
Provare a seguire il seguente tutorial dall'inizio: https://learn.microsoft.com/en-us/windows/wsl/install. Prima di arrendersi al proprio destino provate a riavviare il computer, a molti ha risolto i problemi.
Come ultima risorsa si può provare a reinstallare windows (senza toccare nessun file! Serve solo ad assicurarsi di avere una versione di windows pulita):
![](attachment/1f62d56d9d9004118d532bba93ffa9bb.png)

#### Installare python:

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

```bash
# note that instead of 3.12 you should use your python version!
sudo apt-get install python3.12-venv
```

#### Installare pip:

Installiamo pip:
```bash
sudo apt install python3-pip
```
Installiamo venv:
```bash
# note that instead of 3.12 you should use your python version!
sudo apt-get install python3.12-venv
```

Controllare che pip sia installato correttamente:
```bash
pip3 --version
```


- - -


### MAC OS

#### Installare Homebrew

**Perché Homebrew?**
Perché è un **gestore di pacchetti gratuito per macOS** che facilita l'installazione di software e strumenti di sviluppo non inclusi nel sistema operativo di Apple. Funzionando attraverso comandi da terminale, Homebrew semplifica notevolmente l'installazione, l'aggiornamento e la gestione di programmi open-source sul tuo Mac. In pratica, funge da "App Store" per software da riga di comando e strumenti di sviluppo.

##### Passo 0 Prerequisiti
Prima di iniziare, assicurati che il tuo Mac soddisfi questi requisiti:
- CPU Intel a 64 bit o Apple Silicon
- macOS Catalina 10.15 o versione successiva
- Privilegi di amministratore
- Command Line Tools per Xcode

**LA PARTE DI SEGUITO LA PUOI SKIPPARE SE SAI GIA' CHE IL TUO MAC RISPETTA I PREREQUISITI!! VAI AL "PASSO 1"**
###### 0.1 Verificare il tipo di CPU (Intel o Apple Silicon)
1. Clicca sul simbolo della mela (🍎) nell'angolo in alto a sinistra dello schermo
2. Seleziona "Informazioni su questo Mac"
3. Nella finestra che appare, controlla:
   - Se vedi scritto "Chip" seguito da "Apple M1" o "Apple M2" (o simili), hai un Mac con Apple Silicon
   - Se vedi "Processore" seguito da "Intel", hai un Mac con CPU Intel
   - Tutti i Mac moderni hanno CPU a 64 bit, quindi questo requisito è quasi certamente soddisfatto

###### 0.2 Verificare la versione di macOS
1. Sempre nella finestra "Informazioni su questo Mac" (se l'hai chiusa, ripeti i passaggi precedenti)
2. Guarda la prima riga dove è indicata la versione di macOS
3. Dovresti vedere qualcosa come "macOS Monterey" o "macOS Ventura" o "macOS Sonoma"
4. Se non sei sicuro che sia Catalina (10.15) o successivo, ecco un riferimento:
   - macOS Catalina (10.15) - rilasciato nel 2019
   - macOS Big Sur (11) - rilasciato nel 2020
   - macOS Monterey (12) - rilasciato nel 2021
   - macOS Ventura (13) - rilasciato nel 2022
   - macOS Sonoma (14) - rilasciato nel 2023
   - Se hai una di queste versioni, sei a posto!

###### 0.3 Verificare i privilegi di amministratore
1. Vai al menu 🍎 > Preferenze di Sistema (o Impostazioni di Sistema nelle versioni più recenti)
2. Clicca su "Utenti e Gruppi"
3. Nella lista degli utenti, controlla il tuo account:
   - Se sotto il tuo nome è scritto "Amministratore", hai i privilegi necessari
   - Se è scritto "Standard", non hai i privilegi di amministratore e dovrai chiedere a un amministratore del Mac di aiutarti con l'installazione

###### 0.4 Verificare se Command Line Tools per Xcode è già installato
Questo è il più semplice, perché se non è installato, lo installeremo durante la procedura:

1. Apri Terminal (puoi trovarlo in Applicazioni > Utility, oppure cerca "Terminal" con Spotlight premendo Cmd+Spazio)
2. Digita questo comando e premi Invio:
   ```
   xcode-select -p
   ```
3. Se vedi un percorso come `/Library/Developer/CommandLineTools` o `/Applications/Xcode.app/Contents/Developer`, significa che Command Line Tools è già installato
4. Se ricevi un messaggio di errore o nessun risultato, non preoccuparti: lo installeremo durante la procedura di installazione di Homebrew

Se non sei sicuro di qualcosa, non preoccuparti! La procedura di installazione di Homebrew è abbastanza intelligente da avvisarti se qualcosa non va. Puoi sempre procedere con l'installazione e vedere se funziona.


##### Passo 1: Installare Command Line Tools per Xcode
Questo è necessario per far funzionare Homebrew correttamente:

1. Apri Terminal (puoi trovarlo in Applicazioni > Utility o cercarlo con Spotlight)
2. Digita il seguente comando e premi Invio:
   ```
   xcode-select --install
   ```
3. Si aprirà una finestra di dialogo: clicca su "Installa" e accetta i termini di licenza
4. Attendi il completamento dell'installazione

##### Passo 2: Installare Homebrew
Una volta installato Xcode Command Line Tools:

1. Apri Terminal (se non è già aperto)
2. Copia e incolla il seguente comando:
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Premi Invio
4. Inserisci la password del tuo account quando richiesto (non vedrai i caratteri mentre digiti)
5. Attendi che l'installazione si completi

##### Passo 3: Configurazione aggiuntiva per Mac con Apple Silicon (M1/M2)
Se hai un Mac con chip Apple Silicon (M1/M2), devi eseguire questi passaggi aggiuntivi:

1. Dopo l'installazione, vedrai un messaggio nel Terminal
2. Copia e incolla il primo comando mostrato (simile a questo):
   ```
   echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/tuonome/.zprofile
   ```
   (sostituisci "tuonome" con il tuo nome utente o usa esattamente il comando mostrato nel Terminal)
3. Poi esegui il secondo comando:
   ```
   eval "$(/opt/homebrew/bin/brew shellenv)"
   ```

##### Passo 4: Verifica l'installazione
Per verificare che Homebrew sia stato installato correttamente:

1. Digita nel Terminal:
   ```
   brew --version
   ```
2. Dovresti vedere la versione di Homebrew installata

##### Passo 5 (Opzionale): Disattivare la raccolta dati
Se non vuoi che Homebrew raccolga dati di utilizzo:

1. Digita nel Terminal:
   ```
   brew analytics off
   ```
2. Per verificare lo stato:
   ```
   brew analytics
   ```

##### (opzionale) Comandi base di Homebrew
- Per installare un software: `brew install [nome-pacchetto]`
- Per aggiornare Homebrew: `brew update`
- Per vedere i pacchetti che necessitano aggiornamento: `brew outdated`
- Per aggiornare un pacchetto: `brew upgrade [nome-pacchetto]`
- Per disinstallare un pacchetto: `brew uninstall [nome-pacchetto]`

##### In caso di problemi durante l'installazione....
Prova a seguire passo passo questo articolo (in pratica riprova a reinstallare homebrew da 0) https://iboysoft.com/howto/install-homebrew-on-mac.html


#### Installare Python su Mac 

1. **Scarica Python**:
   - Vai sul sito [python.org](https://www.python.org/downloads/macos/)
   - Scarica la versione più recente di Python per Mac (sarà un file con estensione `.pkg`)

2. **Avvia l'installazione**:
   - Fai doppio clic sul file `.pkg` scaricato
   - Si aprirà l'app Installer standard di macOS

3. **Segui i passaggi dell'installazione**:
   - Clicca su **Continua** per procedere
   - Leggi le informazioni (ti dicono quale versione di Python stai installando)
   - Accetta i termini di licenza
   - Nella schermata "Tipo di installazione", puoi usare le impostazioni standard

4. **Completa l'installazione**:
   - Clicca su **Installa**
   - Ti verrà chiesta la password del tuo account Mac (devi avere privilegi di amministratore)
   - Attendi che l'installazione si completi

5. **Installa i certificati di sicurezza**:
   - Quando appare la finestra di riepilogo, l'installazione è quasi completa
   - Vai nella cartella `/Applications/Python 3.x/` (dove 3.x è la versione installata)
   - Fai doppio clic su **Install Certificates.command**
   - Si aprirà una finestra del Terminale che installerà automaticamente i certificati
   - Quando vedi "Successfully installed certifi" e "update complete", puoi chiudere la finestra

6. **Cosa viene installato**:
   - Una cartella "Python 3.x" nelle Applicazioni con IDLE (editor) e Python Launcher
   - Python stesso in `/Library/Frameworks/Python.framework`
   - Collegamenti a Python in `/usr/local/bin/`

Ora Python è installato e pronto all'uso sul tuo Mac!

##### In caso di problemi... 
Seguire la sezione 5.1.1 di questo tutorial, non andare oltre.
https://docs.python.org/3/using/mac.html#installation-steps

