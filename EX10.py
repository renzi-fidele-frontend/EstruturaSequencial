"""Exercício número 10 do tipo Decisão

Ele irá te pedir
 informação acerca do teu
  período atual escolar"""


def ex10():
    print('-' * 50)
    print('Períodos do dia:\nM - Manhã\nT - Tarde\nN - Noite\n\n\n')
    while True:
        try:
            turno = str(input('Bom dia!\nEm que período da manhã vôçe estuda? ')).strip().lower()[0]
            if turno in 'mtn':
                break
        except IndexError:
            print('Por favor, veja bem as tuas opções.\n')
        except ValueError:
            print('Por favor, veja bem as tuas opções.\n')

    if turno == 'm':
        print('Bom dia!!!\n')
    elif turno == 't':
        print('Boa tarde!!!\n')
    else:
        print('Boa noite!!!\n')


ex10()

