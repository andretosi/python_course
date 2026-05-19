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


percorso_foto = trova_o_crea_foto()
foto = plt.imread(percorso_foto)

if foto.ndim == 3 and foto.shape[2] == 4:
    foto = foto[:, :, :3]

print(f"File: {percorso_foto.name}")
print(f"shape: {foto.shape}")
print(f"dtype: {foto.dtype}")
print(f"min: {foto.min():.2f}")
print(f"max: {foto.max():.2f}")
print(f"pixel [0, 0]: {foto[0, 0, :3]}")

plt.imshow(foto)
plt.axis("off")
plt.savefig("foto_aula_controllo.png", bbox_inches="tight", pad_inches=0)
plt.close()

print("Immagine salvata: foto_aula_controllo.png")
