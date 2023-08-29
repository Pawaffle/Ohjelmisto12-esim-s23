import random

loto = int(random.randint(1,10))
arpa = int(input('Arvaa numero: '))

while arpa != loto:

    if arpa > loto:
        print('  Liian suuri arvaus \n')
    if arpa < loto:
        print('  Liian pieni arvaus \n')
    arpa = int(input('Yrittää uudellen: '))

print('  Oiken!!!')