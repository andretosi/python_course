import numpy as np


aula_piccola = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
    ]
)

ruotata = np.rot90(aula_piccola)
ribaltata = np.fliplr(aula_piccola)
ruotata_a_mano = aula_piccola.T[::-1, :]

angolo = np.deg2rad(90)
matrice_rotazione = np.array(
    [
        [np.cos(angolo), -np.sin(angolo)],
        [np.sin(angolo), np.cos(angolo)],
    ]
)

punto = np.array([2, 1])
nuovo_punto = matrice_rotazione @ punto

print("matrice originale")
print(aula_piccola)
print("np.rot90")
print(ruotata)
print("np.fliplr")
print(ribaltata)
print("rotazione a mano")
print(ruotata_a_mano)
print("matrice geometrica di rotazione")
print(matrice_rotazione.round(2))
print("punto ruotato")
print(nuovo_punto.round(2))
