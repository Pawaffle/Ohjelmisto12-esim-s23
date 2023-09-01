var = int(input('Anna joku luku: '))
i = var - 1
list = []

while i != 1:
    list.append( var % i )
    i -= 1

print(list)

if 0 in list:
    print('shity shit')
else:
    print('luku on alkuluku')