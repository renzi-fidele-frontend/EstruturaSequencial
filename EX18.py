"""Exercício número 18

Ele irá te pedir que insiras
 uma data e te mostrará a data
  em formato dd/mm/yyyy"""


def ex18():
    while True:
        try:
            dia = int(input('Insira qual é o dia: '))
            if dia in range(1, 32):
                break
            else:
                print('Por favor, insira um dia válido.\n')
        except IndexError:
            print('Por favor, insira um dia válido.\n')
        except ValueError:
            print('Por favor, insira um dia váiido.\n')

    while True:
        try:
            mes = int(input('Insira qual é o mês: '))
            if mes in range(1, 13):
                break
            else:
                print('Por favor, insira um mês válido.\n')
        except ValueError:
            print('Por favor, insira um mês válido.\n')
        except IndexError:
            print('Por favor, insira um mês válido.\n')

    while True:
        try:
            ano = int(input('Insira qual é o ano: '))
            if ano >= 1:
                break
            else:
                print('Por favor, insira um ano válido.\n')
        except IndexError:
            print('Por favor, insira um ano válido.\n')
        except ValueError:
            print('Por favor, insira um ano válido.\n')

    print('\n\n', '-' * 70, '\n', 'Exercíco número 18\n', '-' * 70, '\n\nA data inserida foi: {}/{}/{}.\n'.format(dia,
                                                                                                                  mes,
                                                                                                                  ano))


ex18()
