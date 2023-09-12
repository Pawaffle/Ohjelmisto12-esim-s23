lst = []

def nums(lista):
    i = 0
    while i < len(lista):
        if lista[i] % 2 != 0:
            lista.remove(lista[i])
            i -= 1
        i += 1
    return lista

print('Jos painat "Enter" ilman lukua, ohjelma päätyy')
num = input('Anna joku luku: ')

while num != '':
    num = int(num)
    lst.append(num)
    num = input('Anna seurava luku: ')

lst.sort()
even_lst = []
even_lst.extend(lst)
nums(even_lst)

print(f'''
Sinun listassa on seuravat luvut: {lst}
Parilliset niista ovat {even_lst}
''')