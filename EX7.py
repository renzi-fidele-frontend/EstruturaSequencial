"""Exercício número 7 do tipo decisão

Ele irá te pedir 3 números
e daí te dirá quais são
 o maior e o menor """


def ex7():
    nrs = []
    for c in range(1, 4):
        while True:
            try:
                a = float(input('Insira o {}º valor: '.format(c)))
                nrs.append(a)
                break
            except ValueError:
                print('Por favor, insira um valor válido.\n')
            except IndexError:
                print('Por favor, insira um valor válido.\n')
    print('O maior úmero foi: {}\nO menor número foi: {}.\n'.format(max(nrs), min(nrs)))


ex7()
