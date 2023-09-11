def gallons_to_liters():
    global liter
    liter = gallon * 3.785

print('Jos annat negatiivisen luvun, ohjelma päätyy')
gallon = float(input('Anna gallonamäärän: '))

while gallon >= 0:
    gallons_to_liters()
    print(f'{gallon} galonia on {liter:.3f} litraa \n')
    gallon = float(input('Anna seuravan gallonamäärän: '))

print('\n Näkemiin')