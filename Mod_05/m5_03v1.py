var = input('Anna joku luku: ')

while var != '':

    # pikku - "käyttäjat joskus ovat väärässä"
    try:
        var = int(var)
        i = 2
        list = []

        while i != var and var != 1:
            list.append(var % i)
            i += 1

            if 0 in list:
                print('-luku ei ole alkuluku\n')
                break

        if 0 not in list:
            print('-luku on alkuluku\n')

        var = input('Seurava luku tai "Enter" sulkumiseen: ')

    except ValueError:
        print(f'"{var}" - ei ole luku\n')
        var = input('Seurava luku tai "Enter" sulkumiseen: ')

print('Näkemiin!')