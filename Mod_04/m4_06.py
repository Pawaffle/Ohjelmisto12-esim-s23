import random
n = 0
i = 0

N = int(input('Anna toistoen määrä: '))


while i != N :
    i += 1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x*x + y*y < 1:
        n += 1

print(f'pii = noin {4*n/N}')