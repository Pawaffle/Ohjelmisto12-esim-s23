leiv = float(input('Anna leiviskät. \n'))
print()
naul = float(input('Anna naulat. \n'))
print()
luod = float(input('Anna luodit. \n'))

luod *= 13.3
naul *= 13.3*32
leiv *= 13.3*32*20
summ = luod + naul + leiv

kg = int(summ // 1000)
g = summ % 1000

print(f'''
Massa nykymittojen mukaan:
{kg} kilogrammaa ja {g:.2f} grammaa. 
''')