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

altezza, larghezza = foto.shape[:2]
ritaglio = foto[
    altezza // 4 : 3 * altezza // 4,
    larghezza // 4 : 3 * larghezza // 4,
]
specchio = np.fliplr(foto)
grigio = foto.mean(axis=2)

figure, assi = plt.subplots(2, 2, figsize=(8, 6))
immagini = [
    (foto, "originale", None),
    (ritaglio, "ritaglio", None),
    (specchio, "specchio", None),
    (grigio, "grigio", "gray"),
]

for asse, (immagine, titolo, mappa_colore) in zip(assi.ravel(), immagini):
    if mappa_colore is None:
        asse.imshow(immagine)
    else:
        asse.imshow(immagine, cmap=mappa_colore)

    asse.set_title(titolo)
    asse.axis("off")

plt.tight_layout()
plt.savefig("foto_aula_griglia.png")
plt.close()

print(f"shape originale: {foto.shape}")
print(f"shape grigio: {grigio.shape}")
print("Immagine salvata: foto_aula_griglia.png")
