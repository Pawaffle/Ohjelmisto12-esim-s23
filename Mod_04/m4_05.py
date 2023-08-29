root_tunnus = 'python'
root_salasana = 'rules'
x = 1
k = 5

tunnus = input('Anna käyttäjätunnus: ')
salasana = input('Anna salasana: ')

while ( tunnus != root_tunnus or salasana != root_salasana ) and x < 5:
    x += 1
    k -= 1
    print(f''' 
 Jompikumpi tai molemmat ovat väärin
 Voit kokeilä vielä {k} kertaa
     ''')
    tunnus = input('Anna käyttäjätunnus uudelleen: ')
    salasana = input('Anna salasana uudelleen: ')

if tunnus == root_tunnus and salasana == root_salasana:
    print('\n Tervetuloa!!!')
else:
    print('\n Pääsy evätty')
