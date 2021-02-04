"""
CPF = 168.995.350-09
-------------------------------------------------
1 * 10 = 10            #     1 * 11 = 11
6 * 9 = 54             #     6 * 10 = 60
8 * 8 = 64             #     8 * 9 = 72
9 * 7 = 63             #     9 * 8 = 72
9 * 6 = 54             #     9 * 7 = 63
5 * 5 = 25             #     5 * 6 = 30
3 * 4 = 12             #     3 * 5 = 15
5 * 3 = 15             #     5 * 4 = 20
0 * 2 = 0              #     0 * 3 = 0
                       #  -> 0 * 2 = 0 Digito 1 da primeira conta
                       #
        297            #             343
11 - (297 % 11) = 11   #    11 - (343 % 11) = 9
11 > 9 = 0             #
Digito 1 = 0           #   Digito 2 = 9
"""
# Loop infinito
while True:
    cpf = input('Digite o seu CPF: ')
    base_cpf = 0
    somado = 0
    multiplicador1 = 10
    multiplicador2 = 11
    digito1 = 0
    digito2 = 0
    if cpf == 'sair':
        break
    if len(cpf) == 11 or len(cpf) == 14:
        if not cpf.isnumeric() and len(cpf) == 14:
            cpf = cpf.replace('-', '')
            cpf = cpf.replace('.', '')

        # print('Analisando o CPF...')
        base_cpf = cpf[0:-2]

        for n in base_cpf:
            somado += int(n) * multiplicador1
            multiplicador1 -= 1

        digito1 = 11 - (somado % 11)

        if digito1 > 9:
            digito1 = 0
        base_cpf += str(digito1)
        # print(f'O Digito 1 é: {digito1}')
        somado1 = 0

        for n in base_cpf:
            somado += int(n) * multiplicador2
            multiplicador2 -= 1

        digito2 = 11 - (somado % 11)

        if digito2 > 9:
            digito2 = 0
        base_cpf += str(digito2)
        # print(f'O Digito 2 é: {digito2}')

        cpf_exibicao = base_cpf[:3] + '.' + base_cpf[3:6] + '.' + base_cpf[6:9] + '-' + base_cpf[9:]
    # Verifica se não é uma sequencia numérica

        sequencia = base_cpf == str(base_cpf[0]) * len(cpf)

        if cpf == base_cpf and not sequencia:
            print(f'CPF válido! {cpf_exibicao}')
            querContinuar = input('Quer verificar outro CPF? ')
            if querContinuar.__contains__('n') or querContinuar.__contains__('N'):
                break
        else:
            print(f'CPF inválido! Tente novamente!')
    else:
        print('Você precisa de digitar um CPF válido!')

