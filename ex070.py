idade = maiores = homens = mulheresMenosVinte = 0
sexo = continuar = ''
while True:
    idade = int(input('Digite a idade da pessoa:'))
    sexo = input('Digite o sexo da pessoa: (M/F)').upper()
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresMenosVinte += 1
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? (S/N)').upper()
    if continuar == 'N':
        break
    continuar = ''
print(f'Maiores: {maiores}; Homens: {homens}; Mulheres com menos de 20: {mulheresMenosVinte}')
