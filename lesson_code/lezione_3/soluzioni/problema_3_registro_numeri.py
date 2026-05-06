numeri = []

while True:
    valore = float(input("Numero (-1 per terminare): "))

    if valore < 0:
        break

    numeri.append(valore)

print(f"Valori inseriti: {len(numeri)}")
print(numeri)
