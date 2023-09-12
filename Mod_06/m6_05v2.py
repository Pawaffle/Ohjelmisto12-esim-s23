lst = []

def nums(lista):
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            lista[i] = 0

    c = lista.count(0)
    for i in range(c):
        lista.remove(0)
    return lista

'''
print('Jos painat "Enter" ilman lukua, ohjelma päätyy')
num = input('Anna joku luku: ')

while num != '':
    num = int(num)
    lst.append(num)
    num = input('Anna seurava luku: ')
'''

lst = [1, 2, 3, 4, 5, 7, 9]
lst.sort()

even_lst = []
even_lst.extend(lst)

nums(even_lst)
#even_lst = [j for i, j in enumerate(even_lst) if j != 0]
#even_lst = [j for i, j in enumerate(even_lst) if j % 2 == 0]


print(f'''
Sinun listassa on seuravat luvut: {lst}
Parilliset niista ovat {even_lst}
''')