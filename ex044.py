peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / pow(altura, 2)
if imc < 18.5:
    print('Abaixo do peso. IMC = {:.1f}'.format(imc))
elif 18.4 < imc < 25.1:
    print('Peso ideal. IMC = {:.1f}'.format(imc))
elif 25 < imc < 30.1:
    print('Sobrepeso. IMC = {:.1f}'.format(imc))
elif 30 < imc < 40.1:
    print('Obesidade. IMC = {:.1f}'.format(imc))
else:
    print('Obesidad mórbida. IMC = {:.1f}'.format(imc))