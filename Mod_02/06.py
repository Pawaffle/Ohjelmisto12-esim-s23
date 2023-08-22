import random
d1 = 0
d2 = 0
digit1 = 'kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9 = '
digit2 = 'nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6 = '

while d1 < 3:
    digit1 += str(random.randint(0,9))
    d1 += 1

while d2 < 4:
    digit2 += str(random.randint(1, 6))
    d2 += 1

print(digit1)
print(digit2)
