import random, string
alle_10000 = True
kilpailu = []

def random_char(y):
    return ''.join(random.choice(string.ascii_uppercase) for x in range(y))


class Auto:
    speed = 0
    dist = 0
    def __init__(self, rekisteritunnus, huippunopeus):
        self.reg_plate = rekisteritunnus
        self.max_speed = huippunopeus

    def kiihdytä(self, nopeus):
        if self.speed + nopeus > self.max_speed:
            self.speed = self.max_speed
        elif self.speed + nopeus < 0:
            self.speed = 0
        else:
            self.speed += nopeus

    def kulje(self, tuntien_määrä):
        self.dist += ( tuntien_määrä * self.speed )


for i in range (1,11):
    plate = random_char(3) + '-' + str(i)
    new_car = Auto(plate, random.randint(100,200))
    kilpailu.append(new_car)
    #print(f'Rekisteritunnus: {new_car.reg_plate} ja huippunopeus: {new_car.max_speed} km/t')


while alle_10000:
    for car in kilpailu:
        car.kiihdytä(random.randint(-10,15))
        car.kulje(1)
        if car.dist >= 10000:
            alle_10000 = False


kilpailu.sort(key=lambda x: x.dist, reverse=True)

for car in kilpailu:
    print(f'\nAuto, jonka rekisterinumero on {car.reg_plate}, ajoi maaliin numerolla {kilpailu.index(car) + 1} \n'
          f'Sen huippunopeus oli {car.max_speed} km/t \n'
          f'Nykyhetkinen nopeus on {car.speed} km/t ja ajettu matka {car.dist} km/t')