number_list = []

luku = input('Anna joku luku tai "Enter" lupuksi: ')

while luku != '':
    luku = int(luku)
    number_list.append(luku)
    luku = input('Anna joku luku tai "Enter" lupuksi: ')

print(number_list)
number_list.sort(reverse=True)
print((number_list))
print(number_list[:5])