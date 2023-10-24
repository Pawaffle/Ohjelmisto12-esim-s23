import random, string
under_10000 = True
race = []
finish = []

def random_char(y):
    return ''.join(random.choice(string.ascii_uppercase) for x in range(y))


class Auto:
    speed = 0
    dist = 0
    time = 0
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
        self.time += time


for i in range (1,11):
    plate = random_char(3) + '-' + str(i)
    new_car = Auto(plate, random.randint(100, 200))
    race.append(new_car)

while len(race) > 0:
    for car in race:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.dist >= 10000:
            finish.append(car)
            race.remove(car)

finish.sort(key=lambda x: x.time, reverse=False)

for car in finish:
    print(f'\nAuto, jonka rekisterinumero on {car.reg_plate}, ajoi maaliin numerolla {finish.index(car) + 1} \n'
          f'Sen huippunopeus oli {car.max_speed} km/t \n'
          f'Auton ajettu matka {car.dist} km se on suorittu {car.time}:ssa tunnissa')

'''
car_name = 'car_' + str(i)
    new_car = Auto(plate, random.randint(100,200))
    race[car_name] = new_car
'''