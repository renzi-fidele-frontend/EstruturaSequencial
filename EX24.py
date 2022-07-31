"""Exercício número 24 do tipo Decisão

Ele irá te pedir dois valor e logo
 de seguida irá daí calcurará te mostrando
  se o resultado é par ou ímpar,
  se é positivo ou negativo e
  se é inteiro ou decimal"""


import math as m


def ex24():
    valor = 0
    while True:

        while True:
            try:
                a = float(input('Insira o 1º valor: '))
                break
            except ValueError:
                print('Por favor, inisra um valor válido.\n')
            except IndexError:
                print('Por favor, insira um valor válido.\n')

        while True:
            try:
                b = float(input('Insira o 2º valor: '))
                break
            except ValueError:
                print('Por favor, inisra um valor válido.\n')
            except IndexError:
                print('Por favor, insira um valor válido.\n')

        while True:
            print('-' * 70)
            print('Opções:\n* - Multiplicar\n+ - Adicionar\n- - Subtrair\n/ - Dividir\n% - Resto da divisão\n')
            try:
                operacao = str(input('Insira qual operação voçê deseja executar: ')).strip()[0]
                if operacao in '/*-+%':
                    break
                else:
                    print('Por favor, insira uma opção válida.\n')
            except ValueError:
                print('Por favor, insira um valor válido.\n')
            except IndexError:
                print('Por favor, insira um valor válido.\n')
        if operacao == '-':
            valor = a-b
        elif operacao == '*':
            valor = a*b
        elif operacao == '/':
            valor = a/b
        elif operacao == '+':
            valor = a+b
        else:
            valor = a % b

        if valor % 2 == 0:
            print('{} é um valor par.\n'.format(valor))
        else:
            print('{} é um valor ímpar.\n'.format(valor))

        if valor >= 0:
            print('{} é um valor positivo.\n'.format(valor))
        else:
            print('{} é um valor negativo.\n'.format(valor))

        if m.ceil(valor) == valor:
            print('{} é um valor inteiro.\n'.format(valor))
        else:
            print('{} é um valor decimal.\n'.format(valor))
        print('-' * 70)

        while True:
            try:
                resposta = str(input('Voçê deseja continuar? [sim/não]: ')).strip().lower()
                if resposta == 'sim' or resposta == 'não':
                    break
                else:
                    print('Por favor, insira uma opção válida.\n')
            except ValueError:
                print('Por favor, insira uma opção válida.\n')
            except IndexError:
                print('Por favor, insira uma opção válida.\n')

        if resposta == 'sim':
            continue
        else:
            print('Obrigado por teres usado este programa.\n')
            break


ex24()

