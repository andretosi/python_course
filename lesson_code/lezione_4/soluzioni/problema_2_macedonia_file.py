macedonia = ["Anna", "Luca", "Marco"]

with open("macedonia.txt", "w", encoding="utf-8") as file:
    for nome in macedonia:
        file.write(nome + "\n")

with open("macedonia.txt", "r", encoding="utf-8") as file:
    contenuto = file.read()

print(contenuto)
