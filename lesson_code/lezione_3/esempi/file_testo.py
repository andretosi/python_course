with open("note.txt", "w", encoding="utf-8") as file:
    file.write("gatto\n")

with open("note.txt", "r", encoding="utf-8") as file:
    contenuto = file.read()

print(contenuto)
