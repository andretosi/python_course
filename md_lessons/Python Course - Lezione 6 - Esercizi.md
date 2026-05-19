# Lezione 6 - Esercizi

Gli esercizi di questa lezione consolidano:
- NumPy
- Matplotlib
- immagini come array
- assi, shape e canali RGB
- prime idee di machine learning

Le soluzioni eseguibili sono raccolte in:
- `lesson_code/lezione_6/soluzioni/`

Per gli esercizi con la foto, salvare nella cartella di lavoro una foto dell'aula con uno di questi nomi:
- `foto_aula.jpg`
- `foto_aula.png`
- `aula.jpg`
- `aula.png`

Se non c'e una foto, le soluzioni generano una piccola immagine di esempio.

---

## Problema 1 - Un grafico con gli assi

Creare un grafico con Matplotlib usando:

```python
ore = [1, 2, 3, 4]
sedie_occupate = [12, 18, 21, 17]
```

Il grafico deve avere:
- marker sui punti
- etichetta asse x
- etichetta asse y
- titolo

Salvare il grafico in `grafico_presenze.png`.

---

## Problema 2 - Leggere la foto dell'aula

Leggere la foto dell'aula con `plt.imread()`.

Stampare:
- nome del file usato
- `shape`
- `dtype`
- valore minimo
- valore massimo
- valore del pixel in alto a sinistra

Visualizzare la foto con `plt.imshow()` e salvarla in `foto_aula_controllo.png`.

---

## Problema 3 - Ritagliare e ruotare

Prima creare questa matrice:

```python
aula_piccola = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
```

Stampare:
- matrice originale
- matrice ruotata con `np.rot90()`
- matrice ribaltata con `np.fliplr()`
- matrice ruotata a mano con `aula_piccola.T[::-1, :]`

Partendo dalla foto dell'aula:
- ritagliare la zona centrale
- ruotare il ritaglio di 90 gradi
- salvare il risultato in `foto_aula_ritaglio_ruotato.png`

Stampare:
- shape originale
- shape del ritaglio
- shape dell'immagine ruotata

---

## Problema 4 - Colori e luminosita

Partendo dalla foto dell'aula:
- convertire l'immagine in valori tra 0 e 1
- creare una versione piu chiara
- creare una versione con solo il canale rosso
- salvare una figura con entrambe le versioni in `foto_aula_colori.png`

Stampare:
- media del canale rosso
- media del canale verde
- media del canale blu

---

## Problema 5 - Griglia di trasformazioni

Creare una figura 2x2 con:
- foto originale
- ritaglio centrale
- foto ribaltata orizzontalmente
- versione in scala di grigio

Salvare la figura in `foto_aula_griglia.png`.

---

## Problema 6 - Dal dato al problema di machine learning

Rispondere per iscritto:

1. Se ogni foto e un esempio, che cosa potrebbe essere `X`?
2. Che cosa potrebbe essere `y`?
3. Perche ha senso dividere i dati in training set e test set?
4. Perche normalizzare i pixel tra 0 e 1 puo essere utile?
5. Che cosa cambia tra una foto a colori e una foto in scala di grigio dal punto di vista della `shape`?
