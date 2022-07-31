"""Exercício número 20

Ele irá te pedir 3 notas
paarciasis e depois
calculará a sua média"""

import time


def ex20():
    round = 1
    notas = []

    print('\n\n', '-' * 70, '\nExercício número 20\n', '-' * 70, '\n\n')

    for c in range(1, 4):
        while True:
            try:
                a = float(input('Insira qual é a {}ª nota do aluno: '.format(c)))
                if a in range(1, 21):
                    notas.append(a)
                    round += 1
                    break
                else:
                    print('Por favor, insira uma nota válido.\n')
            except ValueError:
                print('Por favor, insira uma nota válida.\n')
            except IndexError:
                print('Por favor, insira uma nota válida.\n')

    print('\n\n')
    print('Nota 1: {}\nNota 2: {}\nNota 3: {}\n{}\n\nAGUARDE PELO RESULTADO EM 10 SEGUNDOS\n\n\033[34m'.format(notas[0],
                                                                                                               notas[1],
                                                                                                               notas[2],
                                                                                                               '-' * 70))

    media = sum(notas) / len(notas)

    for c in range(10, -1, -1):
        print(c)
        time.sleep(1)

    print('\033[m\n\nMédia: {:.2f} valores'.format(media))
    if media <= 9:
        print('Estume mais para o ano que vem.\n')
    else:
        print('Parabéns, voçê passou de classe.\n')
        if media >= 15:
            print('WAUUU, voçê está no quadro de honras.\n')


ex20()
