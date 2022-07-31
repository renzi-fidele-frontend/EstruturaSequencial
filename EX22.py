"""Exercício número 22

Ele irá te pedir qualquer
 valor inteiro e daí te
 dirá se é par ou ímpar"""


def ex22():
    resposta = 'sim'
    while True:
        print('\n\n{}'.format('-' * 70))
        try:
            a = int(input('Insira qualquer valor inteiro: '))
            if a % 2 == 0 or a == 1:
                print('{} é um valor par.\n'.format(a))
            else:
                print('{} é um valor ímpar\n'.format(a))
            while True:
                try:
                    resposta = str(input('Voçê deseja continuar?[sim/não]: ')).strip().lower()
                    if resposta == 'sim' or resposta == 'não':
                        break
                    else:
                        print('Por favcor, insira uma alternativa válida.\n')
                except IndexError:
                    print('Por favor, insira uma alternativa válida.\n')
                except ValueError:
                    print('Por favor, insira uma alternativa válida.\n')
            if resposta == 'sim':
                continue
            else:
                print('Obrigado por teres usado este programa.\n')
                break
        except ValueError:
            print('Por favor, insira um valor válido.\n')
        except IndexError:
            print('Por favor, insira um valor válido.\n')


ex22()
