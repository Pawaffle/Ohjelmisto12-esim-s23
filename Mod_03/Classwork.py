leiviskät = int(input('Anna leiviskät: '))
naulat = int(input('Anna naulat: '))
luodit = float(input('Anna luodit: '))


naulatYht = naulat + 20 * leiviskät

luoditYht = luodit + naulatYht * 32

yht = luoditYht * 13.3
print(f'Grammoja yheensä: {yht}')

# nyt grammat pitäisi saada muunnettua kiloiksi ja grammoiksi
kilot = int(yht // 1000)
gramma = yht % 1000

print('Massa nykymittojen mukaan:')
print(f'{kilot} kilogrammaa ja {gramma:.2f} grammaa')

