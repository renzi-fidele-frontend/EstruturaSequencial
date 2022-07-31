"""Exercício número 3 do tipo Decisão
Ele irá te pedir informação
sobre o seu sexo"""


def ex3():
    while True:
        sexo = str(input('Insira qual é o sexo[F/M]: ')).strip().upper()[0]
        if sexo in 'FM':
            break
        else:
            print('Por favor, as suas opções são:\nF - Feminino\nM - Masculino.\n')

    if sexo == 'F':
        print('Voçê escolheu o sexo Feminino.\n')
    else:
        print('Voçê escolheu o sexo Masculino.\n')


ex3()