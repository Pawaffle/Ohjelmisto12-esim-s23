'''
#tulostetaan komentin
print('terve \n tuntematon henki!')

#tässä on vielä yksi komentti lisää
name = input('kuka olet? :')
name = name + ', perkele'
age = int(input('miten vanha oot?:' ))
age1 = age + 1

print('Terve,', name)
print('Sun ikä on ' + str(age))
print(f'vuoden päästä olet {age1} vuotta vanha')
'''
'''
num1 = input('anna luku 1: ')
num2 = input('anna luku 2: ')
result = int(num1) / int(num2)

# luku :'merkkien määrä'.'desimaali merkien määrä'f
print(f'Jakolaskun tulos: {result:.2f}')
'''
import math
print(f'Piin arvo {math.pi:.5f}')
