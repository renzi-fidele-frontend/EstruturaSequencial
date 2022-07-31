"""Exercício número 27 do tipo Decisão

Ele irá calcular o preço
 a pagar pelo fruto desejado"""


def ex27():
    fruta = ''

    while True:

        while True:
            try:
                print('{}\nFrutas disponíveis:\nMorango\nMaçã\n{}\n\n'.format('-' * 70,'-' * 70))
                fruta = str(input('Insira qual fruto voçê deseja comprar: ')).strip().lower()
                if fruta == 'morango' or fruta == 'maçã':
                    print('Fruto selecionado.\n\n')
                    break
                else:
                    print('Por favor, selecione uma opção válida.\n')
            except ValueError:
                print('Por favor,  selecione uma opção válida.\n')
            except IndexError:
                print('Por favor, selecione uma opção válida.\n')

        while True:
            try:
                qtd = float(input('Inisra qual é a quantidade de {} que voçê deseja comprar em Kg: '.format(fruta)))
                if qtd >= 0:
                    print('Quantidade definida.\n\n')
                    break
                else:
                    print('Por favor, insira uma opção válida.\n')
            except ValueError:
                print('Por favor, insira uma opção válida.\n')
            except IndexError:
                print('Por favor, insira uma opção válida.\n')

        if fruta == 'morango':
            if 0 <= qtd < 6:
                morango_price = qtd * 25
            else:
                morango_price = qtd * 20
            print('\n\nVoçê comprou {:.2f} Kg de {} pelo preço de {:.2f} mt\n\n'.format(qtd, fruta, morango_price))

        else:
            if 0 <= qtd < 6:
                maca_price = qtd * 15
            else:
                maca_price = qtd * 10
            print('\n\nVoçê comprou {:.2f} Kg de {} pelo preço de {:.2f} mt\n\n'.format(qtd, fruta, maca_price))

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
                print('Por favor, selecione uma opcção válida.\n')

        if resposta == 's':
            continue
        else:
            print('Obrigado por teres usado este programa, até a próxima!\n\n\n')
            break


ex27()