"""exercício número 19

Ele irá te pesir que voçê lhe
 infome qualquer valor inteiro e
  daí te mostrará as suas partições"""


def ex19():
    print('\n\n\n', '-' * 70, '\nExercício número 19\n', '-' * 70), '\n\n'

    while True:
        try:
            a = int(input('Insira qualquer valor inteiro: '))
            if 0 <= a < 1001:
                if a in range(0, 10):
                    print('\nUnidades: {}.\n'.format(a))
                elif a in range(10, 100):
                    print('\nUnidade: {}\nDezenas: {}.\n'.format(str(a)[1],
                                                                 str(a)[0]))
                elif a in range(100, 1000):
                    print('\nUnidades: {}\nDezenas: {}\nCentenas: {}.\n'.format(str(a)[2],
                                                                                str(a)[1],
                                                                                str(a)[0]))

                break
            else:
                print('Por favor, insira um número que seja menor do que 1000')
                continue
        except ValueError:
            print('Por favor, insira um número válido.\n')
        except IndexError:
            print('Por favor, insira um número válido.\n')


ex19()



