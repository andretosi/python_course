# Lezione 1 – Scheda di laboratorio

Lavora nella cartella `lezione1_lab` che hai aperto in VS Code. Usa il terminale di **Ubuntu 26.04 LTS** o di **macOS**. Su Windows apri la cartella da Ubuntu in WSL 2. Prima di ogni prova fai la demo corrispondente della [lezione](Python%20Course%20-%20Lezione%201.md).

## Prova breve · Percorsi

**5 minuti, dopo la demo 1.**

- [ ] Dentro `lezione1_lab` crea una cartella **prove** e aprila dal terminale.
- [ ] Crea `lista.txt` con una riga che dice **limone**. Leggilo dal terminale.
- [ ] Torna su di una cartella. Leggi di nuovo lo stesso file usando il percorso relativo da `lezione1_lab`.

Alla fine il terminale deve essere in `lezione1_lab`. L’ultimo comando deve stampare **limone**.

## Esercizio autonomo · Scatole di campioni

**25–30 minuti, dopo le tre demo.** In un piccolo laboratorio ci sono 4 scatole con 8 provette ciascuna. Prepariamo uno script da rilanciare e un notebook che faccia vedere il calcolo.

1. [ ] Dentro `lezione1_lab` crea una sottocartella **campioni**. Nel terminale entra in **campioni** e controlla il percorso.
2. [ ] Crea `provette.py` in **campioni**. Deve stampare **Provette da etichettare** e, sulla riga dopo, il prodotto di **4** per **8**.
3. [ ] Esegui lo script dal terminale. Poi eseguilo dal triangolo **Run Python File** in VS Code e confronta l’output.
4. [ ] Crea `campioni.ipynb` nella stessa sottocartella. Usa il kernel di `.venv` che hai già preparato in `lezione1_lab`. Aggiungi una cella Markdown con il titolo **Provette per il laboratorio** e una cella di codice che mostri il totale.
5. [ ] Esegui le celle, poi modifica solo il numero di scatole nel notebook, da **4** a **6**, e riesegui la cella di codice. Salva entrambi i file.

**Risultato atteso.** Lo script stampa **32**. Il notebook mostra il titolo e stampa prima **32**, poi **48** quando cambi il numero di scatole. Se riavvii il kernel e usi **Run All**, il notebook deve tornare a mostrare **48**.

Se Jupyter è ancora in installazione, completa i punti 1–3. Riprendi dal 4 appena **ipykernel** è pronto. Per i passaggi, vedi **Ambiente virtuale e Jupyter** nella [guida di installazione (PDF)](Python%20Installation%20Guide.pdf).

<details>
<summary>Soluzioni da aprire dopo il tentativo</summary>

**Prova breve.** Parti da `lezione1_lab`.

~~~bash
mkdir prove
cd prove
echo "limone" > lista.txt
cat lista.txt
cd ..
cat prove/lista.txt
~~~

**Scatole di campioni.** Crea **campioni** dall’Explorer di VS Code e usa `cd campioni` per entrarci dal terminale. Questo è il contenuto di `provette.py`.

~~~python
print("Provette da etichettare")
print(4 * 8)
~~~

Lancialo con `python3.13 provette.py`. Se il venv è attivo puoi usare `python provette.py`.

Nel notebook seleziona `.venv`, crea la cella Markdown con `## Provette per il laboratorio` e scrivi **print(4 * 8)** nella cella di codice. Esegui entrambe, poi sostituisci la riga di codice con **print(6 * 8)** ed esegui di nuovo.

</details>

Altri esempi della prima lezione sono nella [cartella delle soluzioni delle edizioni precedenti](../lesson_code/lezione_1/soluzioni/).
