import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


ore = [1, 2, 3, 4]
sedie_occupate = [12, 18, 21, 17]

plt.plot(ore, sedie_occupate, marker="o")
plt.xlabel("ora")
plt.ylabel("sedie occupate")
plt.title("Sedie occupate durante la lezione")
plt.savefig("grafico_presenze.png")
plt.close()

print("Grafico salvato: grafico_presenze.png")
