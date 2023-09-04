print('Terve, kalastaja!')
length = float(input('Anna kuhan pituuden senttimetreinä: '))
print()

if length < 37:
    print('Kuha on alamittainen, kun sen pituus on alle 37 cm.')
    print(f'Pituudesta puuttu {37-length}. Laske kuhan takaisin järveen!!!')
else:
    print('Hyvää poikka, voit pitää sen!')