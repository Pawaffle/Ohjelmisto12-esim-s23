def summa(some_list):
    x = sum(some_list)
    return x

list = []

print('''Jos painat "Enter" ilman lukua, ohjelma päätyy
Ohjelma laskee anetuuen lukuen summan''')
num = input('Anna joku luku: ')

while num != '':
    num = int(num)
    list.append(num)
    num = input('Anna seurava luku: ')

print(f'Anettuen numeroiden summa on {summa(list)}.')