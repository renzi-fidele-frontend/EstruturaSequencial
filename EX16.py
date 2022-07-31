import sys
import math


def ex16():
    print('\n',
          '-' * 70,
          '\n',
          ' ' * 33,
          'Exercício número 16\n',
          '-' * 70,
          '\n\n'
          )

    print('Tipo de equação:    ax^2+bx+c\n\n')

    while True:
        try:
            a = float(input('Insira qual é o valor de a: '))
            if a == 0:
                print('A equação não é de 2º grau, pois o valor de a é igual a 0.\n')
                sys.exit()
            else:
                break
        except IndexError:
            print('Por favor, insira um valor válido.\n')
        except ValueError:
            print('Por favor, insira um valor válido.\n')

    while True:
        try:
            b = float(input('Insira qual é o valor de b: '))
            break
        except IndexError:
            print('Por favor, insira um valor válido.\n')
        except ValueError:
            print('Por favor, insira um valor válido.\n')

    while True:
        try:
            c = float(input('Insira qual é o valor de c: '))
            break
        except ValueError:
            print('Por favor, insira um valor válido.\n')
        except IndexError:
            print('Por favor, insira um valor válido.\n')
    print('-' * 70)

    delta = b ** 2 - 4 * a * c
    delta *= 1
    if delta < 0:
        print('A equação não possui raízes reais.\n')
        sys.exit()
    elif delta == 0:
        raiz1 = (-b - math.sqrt(delta)) / (2 * a)
        raiz2 = (-b + math.sqrt(delta)) / (2 * a)
        print('A equação possui apenas uma raíz real, pois o delta é igual a 0.\nA raíz é: {}'.format(raiz1))

    else:
        raiz1 = (-b - math.sqrt(delta)) / (2 * a)
        raiz2 = (-b + math.sqrt(delta)) / (2 * a)
        print('A equação possui duas raízes reais.\nRaiz 1: {:.1f}\nRaíz 2: {:.1f}\n\n'.format(raiz1,
                                                                                               raiz2))


ex16()
