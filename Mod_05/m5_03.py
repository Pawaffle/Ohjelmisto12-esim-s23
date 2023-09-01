list = []
var = input('Anna joku luku: ')

while var != '':

    # pikku - "käyttäjat joskus ovat väärässä"
    try:
        var = int(var)
        i = var - 1

    #   while i != 1 or i != 0:
        while i not in {1, 0}:
            list.append(var % i)
            i -= 1
        if 0 in list:
            print('-luku ei ole alkuluku\n')
        else:
            print('-luku on alkuluku\n')

        var = input('Seurava luku tai "Enter" sulkumiseen: ')

    except ValueError:
        print(f'"{var}" - ei ole luku\n')
        var = input('Seurava luku tai "Enter" sulkumiseen: ')

print('Näkemiin!')