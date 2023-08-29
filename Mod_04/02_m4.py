print('Muunnetaan tuumia senttimetreiksi')
print('Jos annat negatiivisen tuumamäärän - ohjelma lopettaa toimintansa \n')
inch = int(input('Anna joku pituus: '))

while inch >= 0:
    cm = inch * 2.54
    print(inch,'tuuma =',cm,'senttimetrinä')
    print()
    inch = int(input('Anna uuden pituuden: '))

print('Ohjelma lopitettu. Näkemiin!')