"""Exercício múmero 5 do tipo Decisão

Ele irá te pedir uma certa quantidade de notas
e te mostrará qual é a média"""


def ex5():
    notas = []
    round = 1
    resposta = 's'

    while True:
        try:
            nota = float(input('Insira qual foi a {}ª nota do aluno: '.format(round)))

            if nota in range(0, 21):
                notas.append(nota)
                round += 1
                while True:
                    try:
                        resposta = str(input('Voçê deseja continuar a inserir notas deste aluno[S/N]: ')).strip().upper(

                        )[0]
                        if resposta in 'SN':
                            break
                    except IndexError:
                        print('Por favor, escolha entre sim ou não.\n')
            else:
                print('A nota deve estar entre 0 a 20.\n')
                continue

            if resposta == 'S':
                continue

            else:
                break
        except ValueError:
            print('Por favor, insira uma nota válida.\n')
        except IndexError:
            print('Por favor, insira uma nota válida.\n')

    media = sum(notas) / round
    if media >= 10:
        print('Parabéns, voçê passou de classe.\n')
        if media >= 16:
            print('Voçê está no quadro de honra.\n')

    else:
        print('Estude mais pro ano que vem\nVoçê reprovou.\n')
    print('Média alcançada: {} valores.\n'.format(media))


ex5()
