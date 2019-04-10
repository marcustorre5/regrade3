from time import sleep

def r3():

    print('='*50)
    print('progama de regra de tres v1')
    print('='*50)
    sleep(2)

    n1 = float(input('digite o primeiro valor >\n '))
    n2 = float(input('digite o segundo valor >\n '))
    n3 = float(input('digite o terceiro valor >\n '))

    mult1 = n1*n3
    divisao = mult1/n2
    result = divisao

    print('o resultado é : {}'.format(result))

r3()

def restart():

    while True:
        quest = int(input('deseja fazer mais alguma operação ?\n[0] para sim\n[1]para não\n'))
        if quest == 0:
            r3()

        if quest ==1:
            print('saindo ...')
            sleep(2)
            break

restart()

