"""Exercício número 11 do tipo Decisão

Ele irá te pedir o seu salário
 e depois calculará o novo salário
  de acordo com a decisão do director da empresa"""


def ex11():
    while True:
        try:
            sal = float(input('Insira qual é o seu salário atual: '))
            sal20 = sal * 0.20
            sal15 = sal * 0.15
            sal10 = sal * 0.10
            sal5 = sal * 0.5

            if sal in range(1, 4761):
                print('\n\n{}\nSalário Anterior: {:.2f} mzn\nAumento em 20%: {:.2f} mzn\nNovo Salário: {} mzn\n{}'.format(
                    '-' * 70,
                    sal,
                    sal20,
                    sal20 + sal,
                    '-' * 70
                ))

            elif sal in range(4761, 11901):
                print('\n\n{}\nSalário Anterior: {:.2f} mzn\nAumento em 15%: {:.2f} mzn\nNovo Salário: {} nzb\b{}'.format(
                    '-' * 70,
                    sal,
                    sal15,
                    sal15 + sal,
                    '-' * 70
                ))
            elif sal in range(11901, 25501):
                print('\n\n{}\nSalário Anterior: {:.2f} mzn\nAumento em 20%: {:.2f} mzn\nNovo Salário: {} mzn\n{}'.format(
                    '-' * 70,
                    sal,
                    sal10,
                    sal10 + sal,
                    '-' * 70
                ))

            elif sal >= 25501:
                print('\n\n{}\nSalário Anterior: {:.2f} mzn\nAumento em 20%: {:.2f} mzn\nNovo Salário: {} mzn\n{}'.format(
                    '-' * 70,
                    sal,
                    sal5,
                    sal5 + sal,
                    '-' * 70
                ))
            break
        except ValueError:
            print('Por favor, insira um salário válido meu trabalhador.\n\n')
        except IndexError:
            print('POr favor, insira um salário válido meu trabalhador.\n\n')


ex11()
