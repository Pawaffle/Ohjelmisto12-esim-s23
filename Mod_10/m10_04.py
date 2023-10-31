import random, string
from tabulate import tabulate

under_10000 = True
cars = []

def random_char(y):
    return ''.join(random.choice(string.ascii_uppercase) for x in range(y))


class Auto:
    speed = 0
    dist = 0
    def __init__(self, num_plate, max_speed):
        self.reg_plate = num_plate
        self.max_speed = max_speed

    def accelerate(self, new_speed):
        if self.speed + new_speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed + new_speed < 0:
            self.speed = 0
        else:
            self.speed += new_speed

    def drive(self, time):
        self.dist += (time * self.speed)


class Race:

    def __init__(self, n_name, n_dist, race_list):
        self.name = n_name
        self.dist = n_dist
        self.cars = []
        self.cars.extend(race_list)
        self.table = []

    def one_hour_later(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def kowalsky_report(self):
        self.cars.sort(key=lambda x: x.dist, reverse=True)

        headers = ('kilpailussa', 'rek.num', 'huip.nopeus', 'nyk.nopeus', 'ajettu matka')

        for car in self.cars:
            line = (self.cars.index(car) + 1, car.reg_plate, car.max_speed, car.speed, car.dist)
            self.table.append(line)

        print(tabulate(self.table, headers=headers, tablefmt='grid'))


    def finish(self):
        for car in self.cars:
            if car.dist >= self.dist:
                return True
        return False


for i in range(1, 11):
    plate = random_char(3) + '-' + str(i)
    new_car = Auto(plate, random.randint(100,200))
    cars.append(new_car)
    #print(f'Rekisteritunnus: {new_car.reg_plate} ja huippunopeus: {new_car.max_speed} km/t')

race = Race("Suuri romuralli", 8000, cars)


while not race.finish():
    race.one_hour_later()
    race.finish()

race.kowalsky_report()
