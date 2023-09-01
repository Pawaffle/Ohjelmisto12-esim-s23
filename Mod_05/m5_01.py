import random

while True:
    luku = int(input('Anna noppien määrä: ' ))

    for x in range(luku):
        print(random.randint(1,6))