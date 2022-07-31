"""Exercício número 1 do tipo Decisão

Ele irá te pedir dois números e te mostrará qual
deles é o maior"""


def ex1():
    while True:
        try:
            a = float(input('Insira o primeiro número: '))
            break
        except ValueError:
            print('Por favor, insira um valor válido.\n')
        except IndexError:
            print('Por favor, insira um valor válido.\n')

    while True:
        try:
            b = int(input('Insira o segundo número: '))
            break
        except ValueError:
            print('Por favor, insira um valor válido.\n')
        except IndexError:
            print('Por favor, insira um valor válido.\n')

    if a > b:
        print('O maior número é: {}.\n'.format(a))
    elif b > a:
        print('O maior número é: {}.\n'.format(b))
    else:
        print('O número é o mesmo.\n')


ex1()
