luvut = []

while True:
    syote = input("Anna luku: ")
    if syote == "":
        break
    luvut.append(float(syote))

luvut.sort(reverse=True)
print("Viisi suurinta:", luvut[:5])