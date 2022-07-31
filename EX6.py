"""Exercício número 6 do tipo Decisão

Ele irá te pedir 3 números e
te dirá qual é o maior valor"""


def ex6():
    nrs = []
    for c in range(1, 4):
        while True:
            try:
                a = float(input('Insira o {}º nr: '.format(c)))
                nrs.append(a)
                break

            except IndexError:
                print('Por favor, insira um valor válido.\n')

            except ValueError:
                print('Por favor, insira um valor válido.\n')

    print('O maior número foi: {}.\n'.format(max(nrs)))


ex6()
