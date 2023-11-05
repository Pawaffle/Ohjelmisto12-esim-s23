import json, requests

num = int(input("Montako vitsia haluat ?: "))

for i in range(num):
    response = requests.get('https://api.chucknorris.io/jokes/random').json()
    print(response['value'])
    print()