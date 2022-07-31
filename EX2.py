"""Exercício número 2 do tipo Decisão

Ele irá te pedir um valor
 qualquer e depois te dirá
  se o mesmo é positivo ou negativo"""


def ex2():
    while True:
        try:
            a = float(input('Insira qualquer valor: '))
            if a >= 0:
                print('O valor é positivo.\n')
            else:
                print('O valor é negativo.\n')
            break
        except ValueError:
            print('Por favor, insira um valor válido.\n')
        except IndexError:
            print('Por favor, insira um valor válido.\n')


ex2()
