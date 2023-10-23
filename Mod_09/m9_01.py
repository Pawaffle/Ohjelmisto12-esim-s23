class Auto:
    speed = 0
    dist = 0
    def __init__(self, rekisteritunnus, huippunopeus):
        self.reg_plate = rekisteritunnus
        self.max_speed_kmh = huippunopeus


bentley = Auto('ABC-123', 142)

print(f'Benleyn rekisteritunnus: {bentley.reg_plate} ja huippunopeus: {bentley.max_speed_kmh} km/t \n'
      f'Nykyhetkinen nopeus on {bentley.speed} km/t ja ajettu matka {bentley.dist} km/t')