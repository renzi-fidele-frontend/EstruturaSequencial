#   As notas:       100     200    500    1000
def ex21():
    cem = 0
    duze = 0
    quinhe = 0
    mil = 0
    while True:
        try:
            a = int(input('Insira quantos meticais voçê deseja levantar: '))
            if a % 100 == 0:
                if a >= 1000:
                    print('')
                elif a in range(500, 1000):
                    while a < 1000:
                        quinhe += 1
                        duze += 1

                elif a in range(200, 500):
                    print('Voçê precisará de ')
                elif a in range(100, 200):
                    while a < 200:
                        cem += 1
                    else:
                        break
        except ValueError:
            print('Por favor, insira um valor válido.\nNotas disponíveis: 100,  200,  500, 1000\n')
        except IndexError:
            print('Por favor, insira um valor válido.\n\nNotas disponíveis: 100,  200,  500, 1000\n')

    print('Notas que saião da máquina:\n\n100 x {}\n200 x {}\n500 x {}\n1000 x {}\nn\nImprimindo o valor...\n{}'.format(cem,
                                                                                                                        duze,
                                                                                                                        quinhe,
                                                                                                                        mil,
                                                                                                                        '-' * 70))

ex21()
