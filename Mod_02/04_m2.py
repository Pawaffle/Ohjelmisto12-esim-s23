import math
import statistics

print('Terve! Tarvitaan sinulta seuravat tiedot:')
num1 = int(input('Luku 1 = '))
num2 = int(input('Luku 2 = '))
num3 = int(input('Luku 3 = '))

summ = int(math.fsum([num1, num2, num3]))
avg = statistics.mean([num1, num2, num3])
mult = num1 * num2 * num3

print(f'''
Näiden lukujen
summa = {summ}
tulo = {mult}
keskiarvo = {avg}
''')