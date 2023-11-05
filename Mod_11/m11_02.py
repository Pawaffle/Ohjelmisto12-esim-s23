import random, string
from tabulate import tabulate

under_10000 = True
cars = []
line=()


def random_char(y):
    return ''.join(random.choice(string.ascii_uppercase) for x in range(y))


class Auto:
    speed = 0
    dist = 0
    time = 0

    def __init__(self, num_plate, max_speed):
        self.reg_plate = num_plate
        self.max_speed = max_speed


class Electric(Auto):
    def __init__(self, num_plate, max_speed, battery_capacity):
        super().__init__(num_plate, max_speed)
        self.battery = battery_capacity
        self.economy = random.randint(10, 16)

    def drive(self, time, speed):
        self.speed = speed
        self.dist += (time * self.speed)
        self.battery = self.battery - ((self.economy / 100) * self.speed * time)
        self.time += time

    def report(self):
        line = ('sähkö', self.reg_plate, f'{self.max_speed} km/t', f'{self.speed} km/t', f'{self.dist} km',
                f'{self.economy} kWh/100km', f'{self.battery:.2f} kWh')
        return line

class Petrol(Auto):
    def __init__(self, num_plate, max_speed, tank_capacity):
        super().__init__(num_plate, max_speed)
        self.tank = tank_capacity
        self.economy = random.randint(6, 12)

    def report(self):
        line = ('pensa', self.reg_plate, f'{self.max_speed} km/t', f'{self.speed} km/t', f'{self.dist} km',
                f'{self.economy} l/100km', f'{self.tank:.2f} l')
        return line

    def drive(self, time, speed):
        self.speed = speed
        self.dist += (time * self.speed)
        self.tank -= (self.economy / 100) * self.speed * time
        self.time += time


def kowalsky_report():
    cars.sort(key=lambda x: x.dist, reverse=True)

    headers = ('kilpailussa', 'rek.num', 'huip.nopeus', 'nopeus', 'ajettu matka', 'kulutus', 'jäljellä',)
    table = []

    for car in cars:
        line = car.report()
        table.append(line)

    print(tabulate(table, headers=headers, tablefmt='grid'))


cars.append(Electric((random_char(3) + '-' + str(1)), 180, 52.5))
cars.append(Petrol((random_char(3) + '-' + str(2)), 165, 32.3))

for car in cars:
    car.drive(3, 100)

kowalsky_report()