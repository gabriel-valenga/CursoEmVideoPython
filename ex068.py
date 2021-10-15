numero = i = 0
while True:
    numero = int(input('Você quer a tabuada de qual valor?'))
    if numero < 0:
        break
    for i in range(0,11):
        print(f'{numero} X {i} = {numero * i}')