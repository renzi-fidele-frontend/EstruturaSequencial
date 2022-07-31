""" Exercício número 13

Ele irá te pedir que
 selcciones o dia da semana"""


def ex13():
    print('-' * 70)
    print(' ' * 33)
    print('Exercício número 13')
    print('-' * 70)
    print('\n\n')
    print('Opções válidas:\n')
    print('''0 - Domingo
1 - 2ªFeira
2 - 3ªFeira
3 - 4ªFeira
4 - 5ªFeira
5 - 6ªFeira
6 - Sábado


''')
    while True:
        try:
            dia = int(input('Seleccione o dia da semana: '))
            if dia in range(0, 7):
                break
            else:
                print('Por favor, selccione uma opção válida.\n')
        except IndexError:
            print('Por favor, seleccione uma opção válida.\n')
        except ValueError:
            print('Por favor, seleccione uma opção válida.\n')

    if dia == 0:
        print('Você seleccionou Domingo.\n')
    elif dia == 1:
        print('Você seleccionou 2ªFeira.\n')
    elif dia == 2:
        print('Você seleccionou 3ªFeira.\n')
    elif dia == 3:
        print('Você seleccionou 4ªFeira.\n')
    elif dia == 4:
        print('Você seleccionou 5ªFeira.\n')
    elif dia == 5:
        print('Você seleccionou 6ªFeira.\n')
    elif dia == 6:
        print('Você seleccionou Sábado.\n')

    print('-' * 70)


ex13()