"""Exercício número 12 do tipo Decisão

Ele irá te pedir que
informe o seu salário e logo
de seguida produzirá a folha
 de cálculo empresarial"""


def ex12():
    print('\n\n', '-' * 70, 'Exercício 12 ', '-' * 70, '\n\n')
    while True:
        try:
            #   Meticais ganho por gora
            mt_hora = float(input('Insira quantos meticais voçê ganha por hora: '))
            if mt_hora >= 0:
                break
        except ValueError:
            print('Por favor,insira um valor válido.\n')
        except IndexError:
            print('Por favor, insira um valor válido.\n')

    while True:
        try:
            #   Número de horas trabalhadas
            time = float(input('Insira qual foi o número de horas trabalhadas neste mês: '))
            if time >= 0:
                break
        except IndexError:
            print('Por favor, insira um número válido.\n')
        except ValueError:
            print('Por favor, insira um valor válido.\n')
    sal = time * mt_hora
    ir20 = 0.20 * sal
    ir10 = 0.10 * sal
    ir5 = 0.05 * sal
    ir = 0
    fgts = 0.11 * sal
    inss = 0.03 * sal
    descontos = 0
    ir_perc = 1
    if 15300 <= sal < 25501:
        ir_perc = '5%'
        ir = ir5
        descontos = ir5 + inss
    elif 25500 < sal < 42501:
        ir_perc = '10%'
        ir = ir10
        descontos = ir10 + inss
    elif sal > 42501:
        ir_perc = '20%'
        ir = ir20
        descontos = ir20 + inss

    print('''
{}
Salário Bruto: ({} * {})       :  {:.2f} mzn
(-) IR({}%)                    :  {:.2f} mzn
(-) INSS(3%)                   :  {:.2f} mzn
FGTS(11%)                      :  {:.2f} mzn
Total de descontos             :  \033[33m{}\033[m mzn

Salário Líquido                :  \033[36m{:.2f}\033[m mzn
{}    
    '''.format('-' * 70,
               time,
               mt_hora,
               sal,
               ir_perc,
               ir,
               inss,
               fgts,
               descontos,
               sal - descontos,
               '-' * 70
               ))


ex12()
