import random

maara = int(input("Montako arpakuutiota: "))
summa = 0

for _ in range(maara):
    summa += random.randint(1, 6)

print("Silmälukujen summa:", summa)