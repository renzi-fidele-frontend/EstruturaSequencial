"""Exercício número 9 do tipo decisão

Ele irá te pedir
 3 números e te mostrará
  uma lista em ordem decrescente"""


def ex9():
    lista = []
    for c in range(1, 4):
        while True:
            try:
                a = float(input('Insira o {}º número: '.format(c)))
                lista.append(a)
                break
            except ValueError:
                print('Por favor, insira um valor válido.\n')
            except IndexError:
                print('Por favor, insira um valor válido.\n')
    print('\n\nA lista em ordem decrescente: {}.\n'.format(sorted(reversed(lista))))


ex9()
