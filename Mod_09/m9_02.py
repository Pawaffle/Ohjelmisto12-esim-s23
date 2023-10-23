class Auto:
    speed = 0
    dist = 0
    def __init__(self, rekisteritunnus, huippunopeus):
        self.reg_plate = rekisteritunnus
        self.max_speed = huippunopeus

    def lisätään_nopeutta(self,nopeus):
        if self.speed + nopeus > 0:
            self.speed = self.max_speed
        elif self.speed + nopeus < 0:
            self.speed = 0
        else:
            self.speed += nopeus



bentley = Auto('ABC-123', 142)

print(f'Benleyn rekisteritunnus: {bentley.reg_plate} ja huippunopeus: {bentley.max_speed} km/t \n'
      f'Nykyhetkinen nopeus on {bentley.speed} km/t ja ajettu matka {bentley.dist} km/t \n')

bentley.lisätään_nopeutta(30)
bentley.lisätään_nopeutta(70)
bentley.lisätään_nopeutta(50)

print(f'Bentlyn nykyhetkinen nopeus on {bentley.speed} km/t')

bentley.lisätään_nopeutta(-200)

print(f'Bentlyn nykyhetkinen nopeus on {bentley.speed} km/t')
