import math
r = int(input('Anna ympyrän säteen: \n'))

# debug rivit ja muu kokeilu
# print('\n', r , '\n')
# result1 = math.pi * r * r

result = math.pi * r ** 2

print(f'Ympyrän pinta-ala on {result} tai {result:.2f}')