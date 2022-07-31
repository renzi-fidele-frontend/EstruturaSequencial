"""Exercício número 26 do tipo Decisão

Ele irá te pedir o tipo e a
 quantidade de combustível que
 voçê deseja comprar edepois
 te dirá quantos meticais voçê deve pagar"""


def ex26():

    while True:

        while True:
            try:
                print('\n\n{}\n'.format('-' * 70))
                print('Opçoes:\nD - Diesel\nG - Gasolina\n\n')
                tipo_comb = str(input('Insira qual é o tipo de combustivel que se deseja comprar: ')).strip().lower()[0]
                if tipo_comb in 'dg':
                    if tipo_comb == 'd':
                        tipo_comb = 'Diesel'
                    else:
                        tipo_comb = 'Gasolina'
                    break
                else:
                    print('Por favor, selecione uma opção válida.\n')
            except ValueError:
                print('Por favor, insira um valor válido.\n')
            except IndexError:
                print('Por favor, insira um valor válido.\n')

        while True:
            try:
                qtd = float(input('Insira qual é a quantidade em litros do {} que desejas comprar: '.format(tipo_comb)))
                if qtd >= 0:
                    break
                else:
                    print('Por favor, insira uma quantidade válida.\n')

            except ValueError:
                print('Por favor, insira uma quantidade válida.\n')
            except IndexError:
                print('Por favor, insira uma quantidade válida-\n')

        price_diesel = 42.5 * qtd
        price_gasol = 32.5 * qtd

        if qtd <= 20:
            desconto_diesel = price_diesel * 0.03
            desconto_gasol = price_gasol * 0.04
        else:
            desconto_gasol = price_diesel * 0.05
            desconto_diesel = price_gasol * 0.06
        if tipo_comb == 'Gasolina':
            print('\n\nO comprador deve pagar: {:.2f} mts para comprar {} litros de {}\nDesconto: {:.2f} mts'.format(
                price_gasol,
                qtd,
                tipo_comb,
                desconto_gasol))
        else:
            print('\n\nO comprador deve pagar: {:.2f} mts para comprar {} litros de {}\nDesconto: {:.2f} mts'.format(
                price_diesel,
                qtd,
                tipo_comb,
                desconto_diesel))
        print('-'*70)

        while True:
            try:
                resposta = str(input('Voçê deseja continuar[sim/não]? ')).strip().lower()
                if resposta == 'sim' or resposta == 'não':
                    break
                else:
                    print('Por favor, insira uma opção válida.\n')
            except ValueError:
                print('Por favor, insira uma opção válida.\n')
            except IndexError:
                print('Por favor, insira uma opção válida.\n')

        if resposta == 'sim':
            continue
        else:
            print('Obrigado por teres usado este programa.\n')
            break


ex26()

