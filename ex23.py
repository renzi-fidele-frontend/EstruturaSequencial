"""Exercício número 23

Ele irá te pedir qualquer
 valor inteiro e daí te dirá
  se é decimal ou se é inteiro"""


import math as m


def ex23():

    while True:
        print('\n')
        print('-' * 70)
        while True:
            try:
                a = float(input('Insira qualquer valor inteiro: '))
                if m.ceil(a) == a:
                    print('{} é um valor inteiro.\n'.format(a))
                else:
                    print('{} é um valor decimal.\n'.format(a))
                break
            except ValueError:
                print('Por favor, insira um valor válido.\n')
            except IndexError:
                print('Por favor, insira um valor válido.\n')
        print('-' * 70)
        while True:
            try:
                resposta = str(input('Voçê deseja continuar? [sim/não]: ')).strip().lower()
                if resposta == 'sim' or resposta == 'não':
                    break
                else:
                    print('Por favor, selecione uma opção válida.\n')
            except ValueError:
                print('Por favor, insira uma opção válida.\n')
            except IndexError:
                print('Por favor, insira uma opção válida.\n')
        if resposta == 'sim':
            continue
        else:
            print('\nObrigado por teres usado este programa.\n')
            break


ex23()

