"""Exercício número 28

É um caixa electrónico
para venda de carnes em
 estabelecimentos de classe baixa
"""


def ex28():
    registro_vendas = {}
    venda_diAria = 0

    while True:

        while True:
            print('{}\nPromocão das carnes\n{}\nFile duplo\nPeru\nPorco\n\n'.format('-' * 70,
                                                                                    '-' * 70))
            try:
                carne = str(input('Insira qual é o tipo de carne que voçê deseja comprar: ')).strip().lower()
                if carne == 'file duplo' or carne == 'peru' or carne == 'porco':
                    break
                else:
                    print('Por favor, insira uma opção válida.\n')
            except ValueError:
                print('Por favor, insira uma opção válida.\n')
            except IndexError:
                print('Por favor, insira uma opção válida.\n')

        while True:
            try:
                qtd = float(input('Insira qual é a quantidade de {} que desejas comprar em Kg: '.format(carne)))
                if qtd >= 0:
                    break
                else:
                    print('Por favor, insira uma opção válida.\n')
            except ValueError:
                print('Por favor, insira uma opção válida.\n')
            except IndexError:
                print('Por favor, insira um opção válida.\n')

        while True:
            try:
                print('{}\nMétodo de pagamento\n{}\nc - Cartão\nd - dinheiro vivo\n\n'.format('-' * 70,
                                                                                              '-' * 70))
                met_pagamento = str(input('De que maneira voçê deseja pagar a compra? ')).strip().lower()
                if met_pagamento in 'cd':
                    break
                else:
                    print('Por favor, insira uma opção válida.\n')
            except ValueError:
                print('Por favor, insira uma opção válida.\n')
            except IndexError:
                print('Por favor, insira uma opção válida.\n')

        if qtd <= 5:
            file_price = 60 * qtd
            peru_price = 70 * qtd
            porco_price = 80 * qtd
        else:
            file_price = 50 * qtd
            peru_price = 60 * qtd
            porco_price = 70 * qtd

        if met_pagamento == 'c':
            if carne == 'porco':
                desconto = porco_price * 0.05
                total = porco_price
                total_abs = porco_price - desconto
            elif carne == 'peru':
                desconto = peru_price * 0.05
                total = peru_price
                total_abs = peru_price - desconto
            else:
                desconto = file_price * 0.05
                total = file_price
                total_abs = file_price - desconto

            print(
                '\n\n{}\n{}RECIBO\n{}\n\nTipo de carne: {}\nQuantidade: {:.2f} Kg\nTotal: {:.2f} mzn\nMétodo de '
                'pagamento: Cartão Bim\nDesconto(5%): {:.2f} mzn\n\nTotal absoluto: {:.2f} mzn\n{}\n\n\n'.format(
                    '-' * 70,
                    ' ' * 6,
                    '-' * 70,
                    carne,
                    qtd,
                    total,
                    desconto,
                    total_abs,
                    '-' * 70))

        else:
            if carne == 'porco':
                desconto = porco_price * 0.05
                total = porco_price
                total_abs = porco_price - desconto
            elif carne == 'peru':
                desconto = peru_price * 0.05
                total = peru_price
                total_abs = peru_price - desconto
            else:
                desconto = file_price * 0.05
                total = file_price
                total_abs = file_price - desconto

            print(
                '\n\n{}\n{}RECIBO\n{}\n\nTipo de carne: {}\nQuantidade: {:.2f} Kg\nTotal: {:.2f} mzn\nMétodo de '
                'pagamento: Dinheiro vivo\n\nTotal absoluto: {:.2f} mzn\n{}\n\n\n'.format(
                    '-' * 70,
                    ' ' * 6,
                    '-' * 70,
                    carne,
                    qtd,
                    total,
                    total_abs,
                    '-' * 70))

        venda_diAria += total_abs
        while True:
            try:
                resposta = str(input('Voçê deseja continuar[s / n]? ')).strip().lower()[0]
                if resposta in 'sn':
                    break
                else:
                    print('Por favor, selecione uma opção válida.\n')
            except ValueError:
                print('Por favor, selecione uma opção válida.\n')
            except IndexError:
                print('Por favor, selecione uma opção válida.\n')

        if resposta == 's':
            continue
        else:
            print('\n\nObrigado por teres utilizado este mini-programa.\nAté a prróxima\n\nO total de venda diário '
                  'foi de: {} mzn\n\n'.format(venda_diAria))
            break


ex28()