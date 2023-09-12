import math


def price_per_meter(diameter, price):
    r = diameter * 0.5
    A_cm = math.pi * (r ** 2)
    A_m = A_cm * 0.0001
    m2_price = price / A_m
    return m2_price


# d - diameter / r - radius
d1 = int(input('Anna ensimmäinen pizzan halkaisijan: '))
p1 = float(input('Anna ensimmäinen pizzan hinnan: '))
pizza1 = price_per_meter(d1, p1)

d2 = int(input('Anna toisen pizzan halkaisijan: '))
p2 = float(input('Anna toisen pizzan hinnan: '))
pizza2 = price_per_meter(d2, p2)

if pizza1 < pizza2:
    print(f'''
    Ensimmäinen pizza on halvempi kuin toinen.
    Sen neliohinta on {pizza1:.2f} euroa, ja toisnen {pizza2:.2f}''')
elif pizza2 < pizza1:
    print(f'''
    Toinen pizza on halvempi kuin toinen.
    Sen neliohinta on {pizza2:.2f} euroa, ja ensimmäisen {pizza1:.2f}''')
else:
    print('Pizzoilla on samat hinnat')