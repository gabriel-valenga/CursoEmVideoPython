reta1 = float(input('Digite o comprimento da reta 1:'))
reta2 = float(input('Digite o comprimento da reta 2:'))
reta3 = float(input('Digite o comprimento da reta 3:'))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    if reta1 == reta2 == reta3:
        print('As retas formam um triângulo equilátero.')
    elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        print('As retas formam um triângulo escaleno.')
    else:
        print('As retas formam um triângulo isósceles.')
else:
    print('As retas não podem formar um triângulo')