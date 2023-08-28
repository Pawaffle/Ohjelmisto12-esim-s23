clss = input('Terve, kerro sun laivan hyttiluokan: ')

if clss == 'Lux' or clss == 'LUX' or clss =='lux':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif clss == 'A' or clss =='a':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif clss in {'B', 'b'}:
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif clss in {'C', 'c'}:
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka')