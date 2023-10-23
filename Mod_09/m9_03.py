class Auto:
    speed = 0
    dist = 2000
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


bentley = Auto('ABC-123', 142)

print(f'Benleyn rekisteritunnus: {bentley.reg_plate} ja huippunopeus: {bentley.max_speed} km/t \n'
      f'Nykyhetkinen nopeus on {bentley.speed} km/t ja ajettu matka {bentley.dist} km/t \n')

print(f'--------------------------------\n'
      f'Auton mittarilukema on {bentley.dist} aluksi')
bentley.kiihdytä(60)
bentley.kulje(1.5)
print(f'Auton mittarilukema on {bentley.dist:.0f} lopuksi')

