"""Exercício número 15

Ele irá te pedir as medidas dos lados
 de um triângulo qualquer e
 depois te dirá se é possível
 construi-lo com as tais medidas,
  e tambeém te dirá a tipologia do mesmo """


def ex15():
    print('\n\n',
          '-' * 70,
          '\nExecício número 15\n',
          '-' * 70)

    lados = []
    round = 1

    while True:
        try:
            while True:
                l = float(input('Insira qual é a media do lado {}: '.format(round)))
                if l >= 0:
                    lados.append(l)
                    round += 1
                    break
        except ValueError:
            print('Por favor, insira uma medida válida.\n')
        except IndexError:
            print('Por favor, insira uma medida válida.\n')

        if round == 4:
            break

    if (lados[0] + lados[1]) > lados[2] or (lados[0] + lados [2]) > lados[1] or lados[2] + lados[1] > lados[0]:
        print('\n\nCom essas medidas voçê pode formar um triângulo.\n')

        if lados[0] == lados[1] == lados[2]:
            print('O triângulo é equilátero.\n')

        elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
            print('O triângulo é Isósceles.\n')

        elif lados[0] != lados[1] != lados[2]:
            print('O triângulo é escaleno.\n')

        else:
            print('\n\nCom essas medidas não se pode formar um triângulo.\n')

    print('-' * 70)


ex15()
