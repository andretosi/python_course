# Lezione 1 – Esercizi guidati

Questi esercizi servono a verificare che l'ambiente di lavoro sia davvero pronto. L'idea è semplice: fai un esercizio alla volta, controlla subito il risultato e non andare avanti se qualcosa non torna.

## Regole del gioco
- Lavora in una cartella nuova, per esempio `lezione1_lab`.
- Se usi Windows, esegui tutto dentro WSL/Ubuntu.
- Salvo dove indicato, evita `sudo`.
- Ogni esercizio ha un **check rapido**: se quel check passa, sei sulla strada giusta.

## Esercizio 1 – Cartelle e percorsi

Consegna
- Crea una cartella `lezione1_lab`.
- Dentro crea due sottocartelle: `appunti` e `prove`.
- Entra nella cartella `appunti`.

Comandi suggeriti
- `mkdir`
- `cd`
- `pwd`
- `ls`

Check rapido
```bash
pwd
ls ..
```

Risultato atteso
- `pwd` deve terminare con `/lezione1_lab/appunti`
- `ls ..` deve mostrare almeno `appunti` e `prove`

---

## Esercizio 2 – File, copia, rinomina, cancellazione

Consegna
- Dentro `appunti` crea un file `note.txt`.
- Scrivi nel file due righe di testo.
- Crea una copia chiamata `note_backup.txt`.
- Rinomina `note.txt` in `note_importanti.txt`.
- Cancella il backup.

Comandi suggeriti
- `touch`
- `echo`
- `cat`
- `cp`
- `mv`
- `rm`

Check rapido
```bash
ls
cat note_importanti.txt
```

Risultato atteso
- `ls` deve mostrare `note_importanti.txt`
- `ls` non deve più mostrare `note_backup.txt`
- `cat note_importanti.txt` deve stampare esattamente le due righe che hai scritto

---

## Esercizio 3 – Primo script Python

Consegna
- Torna nella cartella `lezione1_lab`.
- Crea un file `hello.py`.
- Il programma deve stampare:
  - `Ciao Python`
  - una frase a tua scelta
  - il risultato di `7 * 6`

Check rapido
```bash
python3 hello.py
```

Risultato atteso
- L'output deve avere 3 righe
- L'ultima riga deve essere `42`
- Il programma deve partire senza errori

---

## Esercizio 4 – Visual Studio Code

Consegna
- Apri `lezione1_lab` con `code .`
- Apri `hello.py` in VS Code
- Eseguilo da VS Code, non dal terminale esterno

Check rapido
- In VS Code devi vedere l'output del programma senza errori
- Devi riuscire ad aprire anche il terminale integrato

Risultato atteso
- Lo script produce lo stesso output visto nell'esercizio 3
- Riesci a passare da editor a terminale senza uscire da VS Code

---

## Esercizio 5 – Ambiente virtuale

Consegna
- Sempre dentro `lezione1_lab`, crea un ambiente virtuale chiamato `.venv`
- Attivalo
- Installa `notebook` e `ipykernel`

Comandi suggeriti
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install notebook ipykernel`

Per chi usa PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

Check rapido
```bash
ls -a
pip -V
```

Risultato atteso
- `ls -a` deve mostrare la cartella `.venv`
- Il prompt del terminale deve iniziare con `(.venv)`
- `pip -V` deve contenere un percorso che passa dentro `.venv`

---

## Esercizio 6 – Primo notebook

Consegna
- Con il venv attivo, crea un notebook chiamato `test_notebook.ipynb`
- Aggiungi:
  - una cella Markdown con titolo `## Test notebook`
  - una cella di codice che stampi `Notebook ok`
  - una seconda cella di codice che calcoli `3 * 5`
- Esegui tutte le celle

Check rapido
- Il notebook si apre senza errori
- Il kernel selezionato è quello del tuo `.venv`
- Le celle producono output

Risultato atteso
- Devi vedere `Notebook ok`
- Devi vedere il risultato `15`
- Se riapri il notebook, il file `test_notebook.ipynb` deve essere presente dentro `lezione1_lab`

---

## Check finale

Sei a posto per la lezione 1 se riesci a fare tutto questo senza guardare ogni riga delle slide:
- creare cartelle e file dal terminale
- copiare, rinominare e cancellare file
- lanciare `python3 hello.py`
- aprire la cartella in VS Code con `code .`
- creare e attivare `.venv`
- installare un pacchetto con `pip`
- eseguire almeno una cella in un notebook col kernel corretto

Se uno di questi punti salta, non è un dramma: è esattamente il segnale giusto su cosa ripassare.
