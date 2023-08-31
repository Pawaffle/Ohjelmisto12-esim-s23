import random

while True:
    luku = int(input('Anna nooppien määrä: ' ))

    for x in range(luku):
        print(random.randint(1,6))