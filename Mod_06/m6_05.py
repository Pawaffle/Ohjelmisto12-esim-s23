lst = []

def nums(lst):
    global even_lst
    even_lst = []
    for i in lst:
        if i % 2 == 0:
            even_lst.append(i)
    return even_lst

print('Jos painat "Enter" ilman lukua, ohjelma päätyy')
num = input('Anna joku luku: ')

while num != '':
    num = int(num)
    lst.append(num)
    num = input('Anna seurava luku: ')

lst.sort()

print(f'''
Sinun listassa on seuravat luvut: {lst}
Parilliset niista ovat {nums(lst)}
''')