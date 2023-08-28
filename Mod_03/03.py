# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.


sex = input('Anna sukupuolisi: ')

while sex not in {'Mies','mies','MIES','Nainen','nainen','NAINEN'}:
    print('\n Virhellinen syöttö \n')
    sex = input('Anna sukupuolisi: ')

Hb = int(input('Anna hemoglobiiniarvosi numerona (g/l): '))

while Hb <= 0:
    print('\n Virhellinen syöttö \n')
    Hb = int(input('Anna hemoglobiiniarvosi numerona (g/l): '))

# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
if sex in {'Mies','mies','MIES'}:
    if Hb < 134:
        print('\n Teidän hemoglobiiniarvo on alhainen')
    elif Hb > 195:
        print('\n Teidän hemoglobiiniarvo on korkea')
    else:
        print('\n Teidän hemoglobiiniarvo on normaali')

# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
if sex in {'Nainen','nainen','NAINEN'}:
    if Hb < 117:
        print('\n Teidän hemoglobiiniarvo on alhainen')
    elif Hb > 175:
        print('\n Teidän hemoglobiiniarvo on korkea')
    else:
        print('\n Teidän hemoglobiiniarvo on normaali')