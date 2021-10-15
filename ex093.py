from datetime import datetime

trabalhador = {}
trabalhador['nome'] = input('Digite o nome:')
trabalhador['idade'] = datetime.now().year - int(input('Digite o ano de nascimento:'))
trabalhador['ctps'] = int(input('Digite o número da carteira (0 não tem):'))
if trabalhador['ctps'] != 0:
    trabalhador['anoContratacao'] = int(input('Digite o ano de contratação:'))
    trabalhador['salario'] = float(input('Digite o salário:'))
    trabalhador['aposentadoria'] = trabalhador['anoContratacao'] + 35
print(trabalhador)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
