"""Exercício número 14

Ele iáa te pesir duas
 notas parciais e
 calculará a média final"""


def ex14():
    print('-' * 70
          , '\n',
          ' ' * 33,
          'Exercício número 14\n',
          '-' * 70, '\n\n')

    while True:
        try:
            a = float(input('Insira qual é a  1ª nota do aluno: '))
            if a in range(0, 21):
                break
            else:
                print('Insira um nota válida.\n')
        except ValueError:
            print('Por favor, insira um valor válido.\n')

        except IndexError:
            print('Por favor, insira um valor válido.\n')

    while True:
        try:
            b = float(input('Insira qual é a 2ª nota do aluno: '))
            if b in range(0, 21):
                break
            else:
                print('Por favor, insira uma nota válida.\n')
        except ValueError:
            print('Por favor, insira um valor válido.\n')
        except IndexError:
            print('Por favor, insira um valor válido.\n')

    media = (a+b) / 2

    print('''\n\n\n------------------------
Nota 1: {:.2f} valores
Nota 2: {:.2f} valores

Média: {:.2f} valores
------------------------------'''.format(a,
                                         b,
                                         media))
    if media >= 10:
        print('Voçê foi aprovado, parabéns.\n')
        if range(15, 21):
            print('Voçê está no quadro de honra.\n')
    else:
        print('Estude mais para o ano que vem\nVoçê reprovou.\n')


ex14()