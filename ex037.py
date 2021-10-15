retas = input('Digite as medidas das retas:').split(' ')
reta1 = int(retas[0])
reta2 = int(retas[1])
reta3 = int(retas[2])
if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    print('As retas podem formar um triângulo')
else:
    print('As retas não podem formar um triângulo.')