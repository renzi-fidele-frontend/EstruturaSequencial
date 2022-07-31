"""Exercício número 4 do tipo Decisão

Ele irá te pedir para inserir uma letra
e depois ele te dirá se é um vogal ou uma consoante"""


#   As letras do abecedário
letras = 'abcdefghijklmnopqrstuvwxyz'


def ex4():
    while True:
        try:
            letra = str(input('Insira qualquer letra: ')).strip().lower()[0]
            if letra in letras:
                if letra in 'aeiou':
                    print('A letra {} é uma vogal.\n'.format(letra))
                else:
                    print('A letra {} é uma consoante.\n'.format(letra))
                break

            else:
                print('Por favor, insira uma letra existente.\n')
        except IndexError:
            print('Por favor, insira uma letra existente.\n')


ex4()
