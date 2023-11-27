class Elain:

    def __init__(self, tyyppi, aani):
        self.tyyppi = tyyppi
        self.aani = aani

    def tee_aani(self):
        print(f'{self.tyyppi} {self.aani}')


class Lintu(Elain):
    def __init__(self, tyyppi, aani, vari):
        Elain.__init__(self, tyyppi, aani)
        #self().__init__(tyyppi, aani)
        self.vari = vari

    #metodi ylikirjoittaminen, eli lisataan myos vari
    def tee_aani(self):
        print(f'{self.tyyppi} {self.aani}')
        print(f'Sulkeni vari on: {self.vari}')

class Elaintarha:

    # tassa on pysyva assotiatio luokkien vallissa
    def __init__(self):
        self.elaimet = []

    def lisaa_elain(self,elain):
        self.elaimet.append(elain)

    def lista_elaimet(self):
        for elain in self.elaimet:
            elain.tee_aani()

elain1 = Elain('kissa', 'myau')
elain2 = Elain('tiikeri', 'rrrrrrr')
lintu1 = Lintu('kaki', 'kukkuu', 'ruskea')



