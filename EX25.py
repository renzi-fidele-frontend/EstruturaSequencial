"""Exercício número 25 do tipo Decisão

Ele irá te fazer um interogatório
 e logo de seguida te julgará
"""


def ex25():
    print('\n\n{}\nInterrogatório\n{}\n\n'.format('-' * 70, '-' * 70))

    sims = 0
    naos = 0
    while True:

        while True:
            try:
                a = str(input('\nVoçê telefou para a vítima[sim/não]? ')).strip().lower()
                if a == 'sim' or a == 'não':
                    break
                else:
                    print('Por favor, insira uma opção válida.\n')
            except ValueError:
                print('Por favor, insira um valor válido.\n')
            except IndexError:
                print('Por favor, insira um valor válido.\n')

        while True:
            try:
                b = str(input('\nVoçê esteve no local do crime[sim/não]? ')).strip().lower()
                if b == 'sim' or b == 'não':
                    break
                else:
                    print('Por favor, insira uma opção válida.\n')
            except ValueError:
                print('Por favor, insira uma opção válida.\n')
            except IndexError:
                print('Por favor, insira uma opção válida.\n')

        while True:
            try:
                c = str(input('\nVoçê mora perto da casa da vítima[sim/não]? ')).strip().lower()
                if c == 'sim' or c == 'não':
                    break
                else:
                    print('Por favor, insira uma opção válida.\n')

            except ValueError:
                print('Por favor, insira uma opção válida.\n')
            except IndexError:
                print('Por favor, insira uma opção válida.\n')

        while True:
            try:
                d = str(input('\nVoçê devia algum dinheiro para a vítima[sim/não]? ')).strip().lower()
                if d == 'sim' or d == 'não':
                    break
                else:
                    print('Por favor, insira uma opção válida.\n')
            except ValueError:
                print('Por favor, insira uma opção válida.\n')
            except IndexError:
                print('Por favor, insira uma opção válida.\n')

        while True:
            try:
                e = str(input('\nJá trabalhaste com a vítima[sim/não]? ')).strip().lower()
                if e == 'sim' or e == 'não':
                    break
                else:
                    print('Por favor, isnira uma opção válida.\n')
            except IndexError:
                print('Por favor, insira uma opção válida.\n')
            except ValueError:
                print('Por favor, insira uma opção válida.\n')

        #   Calculando as possibilidades
        if a == 'sim':
            sims += 1
        else:
            naos += 1

        if b == 'sim':
            sims += 1
        else:
            naos += 1

        if c == 'sim':
            sims += 1
        else:
            naos += 1

        if d == 'sim':
            sims += 1
        else:
            naos += 1

        if e == 'sim':
            sims += 1
        else:
            naos += 1

        #   Julgando o suspeito
        if sims == 5:
            print('\n\nVoçê foi classificado como sendo o Assasino.\n')
        elif sims == 4:
            print('\n\nVoçê foi classificado como sendo o Cúmplice do assasino.\n')
        elif sims == 3:
            print('\n\nVoçê foi classificado cmoo sendo um suspeito.\n')
        else:
            print('\n\nVoçê foi classificado como sendo Inocente.\nPodes ir.\n')

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
            break


ex25()























