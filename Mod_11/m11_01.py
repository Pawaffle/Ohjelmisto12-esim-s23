class Julkaisu:

    def __init__(self, uusi_nimi):
        self.name  = uusi_nimi

    def report(self):
        print(f'Julkasun nimi: {self.name}')

class Kirja(Julkaisu):

    def __init__(self, uusi_nimi, kirjoitaja, sivujen_määrä):
        Julkaisu.__init__(self, uusi_nimi)
        self.kirjoitja = kirjoitaja
        self.sivut = sivujen_määrä

    def report(self):
        Julkaisu.report(self)
        print(f'Kirjoittaja on {self.kirjoitja}, kirjassa on {self.sivut} sivuja.')

class Lehti(Julkaisu):
    def __init__(self, uusi_nimi, päätoimentaja):
        Julkaisu.__init__(self, uusi_nimi)
        self.pomo = päätoimentaja

    def report(self):
        print(f'{self.pomo} on päätoimentaja "{self.name}" lehdissä')


lehti = Lehti('Aku Ankka', 'Aki Hyyppä')
kirja = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)

print()
lehti.report()
print()
kirja.report()
