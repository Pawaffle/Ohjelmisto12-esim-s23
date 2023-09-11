import random


def noppan_heitto():
    x = random.randint(1,6)
    return x

num = 0
while num != 6:
    num = noppan_heitto()
    print(num)