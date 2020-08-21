import math

all =[]

incriment = 100
cap = 100
7
with open ("triples.txt", "r+") as txtfile:
    txtfile.truncate(0)
    while True:
        for i in range(1, cap):
            for x in range(1, cap):
                if (math.sqrt(i**2 + x**2)) % 2 == 0 or (math.sqrt(i**2 + x**2)) % 2 == 1:
                    if (i, x, int(math.sqrt(i**2 + x**2))) not in all and (x, i, int(math.sqrt(i**2 + x**2))) not in all:
                        all.append((i, x, int(math.sqrt(i**2 + x**2))))
                        print(f"{len(all)} - {all[-1]}")
                        txtfile.write(f"{len(all)} - {all[-1]}\n")
        cap += incriment