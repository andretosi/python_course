# Lezione 6 - Immagini, NumPy, Matplotlib e machine learning

## Indice
- [Lezione 6 - Immagini, NumPy, Matplotlib e machine learning](#lezione-6---immagini-numpy-matplotlib-e-machine-learning)
  - [Prima di iniziare](#prima-di-iniziare)
  - [Obiettivi della lezione](#obiettivi-della-lezione)
  - [Struttura della lezione](#struttura-della-lezione)
  - [Un grafico per capire gli assi](#un-grafico-per-capire-gli-assi)
  - [Una foto come tabella di numeri](#una-foto-come-tabella-di-numeri)
    - [Leggere una foto](#leggere-una-foto)
    - [Dimensioni e canali](#dimensioni-e-canali)
    - [Ritaglio](#ritaglio)
    - [Rotazione e ribaltamento](#rotazione-e-ribaltamento)
    - [Colori e luminosita](#colori-e-luminosita)
    - [Normalizzazione](#normalizzazione)
  - [Collegamento con il machine learning](#collegamento-con-il-machine-learning)
  - [Introduzione al machine learning](#introduzione-al-machine-learning)
  - [Esercizi](#esercizi)
  - [Collegamento con la prossima lezione](#collegamento-con-la-prossima-lezione)

---

## Prima di iniziare

- Aprire la cartella di lavoro corretta in VS Code.
- Attivare l'ambiente virtuale se presente.
- Creare una cartella per la lezione, per esempio `lezione_6`.
- Salvare nella stessa cartella la foto dell'aula ricevuta via WhatsApp o email.

Per questa lezione servono:
```bash
pip install numpy matplotlib
```

Nei file di esempio il nome usato e `foto_aula.jpg`, ma vanno bene anche:
- `foto_aula.png`
- `aula.jpg`
- `aula.png`

---

## Obiettivi della lezione

Al termine della lezione:
- creare un grafico semplice con Matplotlib
- distinguere asse x, asse y e assi di un array NumPy
- leggere un'immagine come array NumPy
- interpretare `shape`, altezza, larghezza e canali colore
- ritagliare, ruotare e ribaltare un'immagine usando indici e assi
- modificare luminosita e canali RGB con operazioni numeriche
- capire perche le immagini sono dati adatti al machine learning
- riconoscere i concetti base di dataset, feature, label, training e test

---

## Struttura della lezione

1. Grafico essenziale con Matplotlib e assi - 10 min
2. Immagini come array NumPy - 20 min
3. Ritaglio, rotazione, canali e luminosita - 30 min
4. Dal pixel alla feature - 15 min
5. Introduzione generale al machine learning - 60 min
6. Esercizi guidati e discussione - 45 min

Argomenti della lezione:
- NumPy
- Matplotlib
- immagini digitali
- array multidimensionali
- normalizzazione dei dati
- fondamenti di machine learning

---

## Un grafico per capire gli assi

Matplotlib permette di visualizzare dati numerici.

```python
import matplotlib.pyplot as plt

ore = [1, 2, 3, 4]
sedie_occupate = [12, 18, 21, 17]

plt.plot(ore, sedie_occupate, marker="o")
plt.xlabel("ora")
plt.ylabel("sedie occupate")
plt.title("Esempio di grafico")
plt.show()
```

Nel grafico:
- l'asse x contiene i valori orizzontali
- l'asse y contiene i valori verticali
- ogni punto collega una coppia di valori

Nei file eseguibili del corso viene usata una versione che salva il grafico su file:

```python
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

ore = [1, 2, 3, 4]
sedie_occupate = [12, 18, 21, 17]

plt.plot(ore, sedie_occupate, marker="o")
plt.xlabel("ora")
plt.ylabel("sedie occupate")
plt.title("Esempio di grafico")
plt.savefig("grafico_assi.png")
plt.close()
```

---

## Una foto come tabella di numeri

Una foto digitale non e solo un'immagine visibile sullo schermo. Per Python e una struttura di numeri.

Una foto a colori di solito ha tre dimensioni:

```text
altezza, larghezza, canali
```

Per esempio:

```text
(1200, 1600, 3)
```

significa:
- 1200 righe di pixel
- 1600 colonne di pixel
- 3 canali colore: rosso, verde, blu

### Leggere una foto

```python
import matplotlib.pyplot as plt

foto = plt.imread("foto_aula.jpg")

print(foto.shape)
print(foto.dtype)
print(foto.min())
print(foto.max())

plt.imshow(foto)
plt.axis("off")
plt.show()
```

`plt.imread()` legge l'immagine e restituisce un array NumPy.

### Dimensioni e canali

```python
altezza = foto.shape[0]
larghezza = foto.shape[1]
canali = foto.shape[2]

print(altezza)
print(larghezza)
print(canali)
```

Gli assi dell'immagine sono:
- asse 0: righe, quindi direzione verticale
- asse 1: colonne, quindi direzione orizzontale
- asse 2: canali colore

Un singolo pixel e una piccola lista di valori:

```python
pixel = foto[0, 0]
print(pixel)
```

In una foto RGB, quel pixel contiene tre numeri: rosso, verde e blu.

### Ritaglio

Il ritaglio si fa usando gli indici, come nelle liste, ma su due assi.

```python
altezza, larghezza = foto.shape[:2]

ritaglio = foto[
    altezza // 4 : 3 * altezza // 4,
    larghezza // 4 : 3 * larghezza // 4,
]

plt.imshow(ritaglio)
plt.axis("off")
plt.show()
```

Qui si prendono solo le righe e le colonne nella zona centrale della foto.

### Rotazione e ribaltamento

Prima di farlo su una foto, conviene guardare una matrice piccola.

```python
import numpy as np

aula_piccola = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

print(aula_piccola)
print(np.rot90(aula_piccola))
print(np.fliplr(aula_piccola))
```

Risultato:

```text
[[1 2 3]
 [4 5 6]]

[[3 6]
 [2 5]
 [1 4]]

[[3 2 1]
 [6 5 4]]
```

`np.rot90()` non cambia i numeri: cambia dove vengono messi. Una rotazione di 90 gradi in senso antiorario equivale a:

```python
ruotata_a_mano = aula_piccola.T[::-1, :]
print(ruotata_a_mano)
```

Passaggi:
- `.T` scambia righe e colonne
- `[::-1, :]` inverte l'ordine delle righe

Con una foto succede la stessa cosa, solo che ogni elemento non e un numero singolo ma un pixel RGB.

```python
import numpy as np

ruotata = np.rot90(foto)
specchio = np.fliplr(foto)

plt.imshow(ruotata)
plt.axis("off")
plt.show()
```

Il ribaltamento orizzontale e ancora piu diretto:

```python
specchio = foto[:, ::-1]
```

Qui si tengono tutte le righe, ma le colonne vengono lette al contrario.

La matrice di rotazione geometrica descrive invece cosa succede alle coordinate di un punto:

```python
angolo = np.deg2rad(90)

rotazione = np.array([
    [np.cos(angolo), -np.sin(angolo)],
    [np.sin(angolo), np.cos(angolo)],
])

punto = np.array([2, 1])
nuovo_punto = rotazione @ punto

print(rotazione)
print(nuovo_punto)
```

Questa matrice lavora su coordinate come `(x, y)`. In un'immagine, pero, i pixel sono indicizzati come `(riga, colonna)` e l'origine e in alto a sinistra. Per rotazioni di 90 gradi NumPy puo riordinare direttamente righe e colonne. Per rotazioni arbitrarie, per esempio 17 gradi, bisogna calcolare nuove coordinate e stimare i pixel mancanti: questa stima si chiama interpolazione.

### Colori e luminosita

Se l'immagine e un array, i colori possono essere modificati con operazioni sui numeri.

```python
import numpy as np

foto_float = foto.astype(float)

if foto_float.max() > 1:
    foto_float = foto_float / 255

piu_chiara = np.clip(foto_float * 1.25, 0, 1)

solo_rosso = foto_float.copy()
solo_rosso[:, :, 1] = 0
solo_rosso[:, :, 2] = 0
```

`np.clip()` evita che i valori escano dall'intervallo valido.

### Normalizzazione

Molti modelli di machine learning lavorano meglio con numeri in un intervallo stabile.

```python
foto_float = foto.astype(float)

if foto_float.max() > 1:
    foto_float = foto_float / 255

grigio = foto_float[:, :, :3].mean(axis=2)

print(grigio.shape)
print(grigio.min())
print(grigio.max())
```

Una foto a colori ha forma:

```text
altezza, larghezza, canali
```

Una versione in scala di grigio ha forma:

```text
altezza, larghezza
```

Per un modello, spesso l'immagine viene poi trasformata in un tensore e raccolta in un dataset.

---

## Collegamento con il machine learning

Una foto puo diventare un esempio di dataset:

```text
X = immagine
y = etichetta
```

Per esempio:
- `X`: foto dell'aula
- `y`: "aula"

Oppure, in un problema di classificazione:
- `X`: immagine
- `y`: classe corretta

Le trasformazioni viste prima sono importanti perche preparano i dati:
- ridurre la dimensione
- ritagliare una zona utile
- normalizzare i valori
- convertire colori e canali
- creare piu versioni della stessa immagine

---

## Introduzione al machine learning

Il machine learning studia metodi con cui un programma impara un comportamento a partire da esempi.

Concetti principali:
- dataset: insieme di esempi
- feature: numeri usati per descrivere un esempio
- label: risposta corretta associata a un esempio
- modello: funzione con parametri modificabili
- training: fase in cui il modello aggiorna i parametri
- test: controllo su dati non usati per allenare il modello
- loss: numero che misura quanto il modello sta sbagliando

Esempio minimale:

```text
immagini di gatti e cani -> modello -> previsione: gatto o cane
```

Il modello non vede "gatto" come lo vede una persona. Vede numeri:
- pixel
- canali
- matrici
- tensori

Per questo e utile capire prima che cos'e un'immagine per Python.

---

## Esercizi

Gli esercizi della lezione 6 sono raccolti in:
- [Python Course - Lezione 6 - Esercizi.md](Python%20Course%20-%20Lezione%206%20-%20Esercizi.md)

Le soluzioni eseguibili sono raccolte in:
- `lesson_code/lezione_6/soluzioni/`

Gli esempi eseguibili sono raccolti in:
- `lesson_code/lezione_6/esempi/`

---

## Collegamento con la prossima lezione

La prossima lezione entra nelle reti neurali con PyTorch.

Le immagini viste qui diventano il caso concreto per parlare di:
- tensori
- dataset di immagini
- batch
- classificazione
- valutazione delle previsioni
