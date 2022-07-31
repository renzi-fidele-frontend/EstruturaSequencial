"""Exercício número 8

Ele irá te pedir o preço de 3 produtos
daí ele te dirá qual é o produto mais barato a comprar"""


def ex8():
    precos = []
    for c in range(1, 4):
        while True:
            try:
                price = float(input('Insira o preço do {}º produto: '.format(c)))
                precos.append(price)
                break
            except ValueError:
                print('Por favor, insira um valor válido.\n')
            except IndexError:
                print('Por favor, insira um valor válido.\n')
    if precos[0] == min(precos):
        print('Voçê deve comprar o 1º produto, cujo preço é de {:.2f} mzn.\n'.format(precos[0]))
    elif precos[1] == min(precos):
        print('Voçê deve comprar o 2º produto, cujo preço é de {:.2f} mzn.\n'.format(precos[1]))
    elif precos[2] == min(precos):
        print('Voçê deve comprar o 3º produto, cujo preço é de {:.2f} mzn.\n'.format(precos[2]))


ex8()
