luku = int(input("Anna kokonaisluku: "))
onko_alkuluku = True

if luku <= 1:
    onko_alkuluku = False
else:
    for i in range(2, int(luku**0.5) + 1):
        if luku % i == 0:
            onko_alkuluku = False
            break

if onko_alkuluku:
    print("On alkuluku")
else:
    print("Ei ole alkuluku")