town_list = []
i = 5

while i != 0:
    town = input(f'Anna joku kaupungin nimi ({i} jäljellä): ')
    town_list.append(town)
    i -= 1

print('\nTässä on sun kaupungit:')
for town in town_list:
    i += 1
    print(f'{i}) {town}')