import math

var = input('Anna joku luku: ')

while var != '':

    # pikku - "käyttäjat joskus ovat väärässä"
    try:
        var = int(var)
        loppu = int((var ** 0.5) + 1)

        for i in range(2, loppu):
            if var % i == 0:
                print('-luku ei ole alkuluku\n')
                var = 'luku'
                break

        if var != 'luku':
            print('-luku on alkuluku\n')

        var = input('Seurava luku tai "Enter" sulkumiseen: ')

    except ValueError:
        print(f'"{var}" - ei ole luku\n')
        var = input('Seurava luku tai "Enter" sulkumiseen: ')

print('Näkemiin!')