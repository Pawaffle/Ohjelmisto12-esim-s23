print('Terve! Tarvitaan sinulta seuravat tiedot:')
a = int(input('Suorakulmion kanta = '))
b = int(input('Suorakulmion korkeus = '))

piiri = 2*a + 2*b
pinta = a * b

print(f'''
Suorakulmion piiri = {piiri}
Suorakulmion pinta-ala = {pinta}    ''')