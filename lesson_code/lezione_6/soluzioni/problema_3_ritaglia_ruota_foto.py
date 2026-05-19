from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def crea_foto_demo(percorso):
    altezza = 120
    larghezza = 180
    foto = np.ones((altezza, larghezza, 3), dtype=float)
    foto[:, :] = [0.84, 0.87, 0.82]
    foto[80:, :] = [0.50, 0.46, 0.40]
    foto[10:28, 18:162] = [0.72, 0.78, 0.86]

    for colonna in range(20, 160, 35):
        foto[58:75, colonna : colonna + 20] = [0.18, 0.26, 0.36]
        foto[75:86, colonna + 5 : colonna + 15] = [0.10, 0.12, 0.16]

    for colonna in range(30, 150, 45):
        foto[42:52, colonna : colonna + 12] = [0.76, 0.56, 0.42]

    plt.imsave(percorso, foto)


def trova_o_crea_foto():
    for nome in [
        "foto_aula.jpg",
        "foto_aula.jpeg",
        "foto_aula.png",
        "aula.jpg",
        "aula.jpeg",
        "aula.png",
    ]:
        percorso = Path(nome)
        if percorso.exists():
            return percorso

    demo = Path("foto_aula_demo.png")
    crea_foto_demo(demo)
    return demo


def in_float_rgb(foto):
    if foto.ndim == 3 and foto.shape[2] == 4:
        foto = foto[:, :, :3]

    foto = foto.astype(float)

    if foto.max() > 1:
        foto = foto / 255

    return foto


percorso_foto = trova_o_crea_foto()
foto = in_float_rgb(plt.imread(percorso_foto))

aula_piccola = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
    ]
)

print("matrice originale")
print(aula_piccola)
print("np.rot90")
print(np.rot90(aula_piccola))
print("np.fliplr")
print(np.fliplr(aula_piccola))
print("rotazione a mano")
print(aula_piccola.T[::-1, :])

altezza, larghezza = foto.shape[:2]
ritaglio = foto[
    altezza // 4 : 3 * altezza // 4,
    larghezza // 4 : 3 * larghezza // 4,
]
ruotata = np.rot90(ritaglio)

plt.imshow(ruotata)
plt.axis("off")
plt.savefig("foto_aula_ritaglio_ruotato.png", bbox_inches="tight", pad_inches=0)
plt.close()

print(f"shape originale: {foto.shape}")
print(f"shape ritaglio: {ritaglio.shape}")
print(f"shape ruotata: {ruotata.shape}")
print("Immagine salvata: foto_aula_ritaglio_ruotato.png")
