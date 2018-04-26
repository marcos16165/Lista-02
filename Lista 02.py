def questao1():
    return 5**2, 9*5, 15/12, 12/15, 15//12, 12//15, 5%2, 9%5, 15%12, 12%15, 6%6, 0%7

def questao2():
    return print('5 horas')

def  questao3():
    print('Entre com a hora atual: ')
    h = int(input())
    print('Quanto tempo deseja esperar: ')
    e = int(input())
    resto = (h + e) % 24
    return print('O depertador tocará ás', resto,'horas.')

def questao5():
    p1 = str('só')
    p2 = str('trabalho')
    p3 = str('sem')
    p4 = str('diversão')
    p5 = str('faz')
    p6 = str('de')
    p7 = str('João')
    p8 = str('em')
    p9 = str('chato')
    return('{} {} {} {} {} {} {} {} {}'.format(p1, p2, p3, p4, p5, p6, p7, p8, p9))


def questao6():
    return(6 * (1 - 2) )


def questao7():
    print('Entre com a quantidade de anos:')
    t = int(input())
    a = 10000 * (1 + (0.08/12))**(12*t)
    return print('O valor do jutos depois de', t,'é ', a,'.')


def questao8():
    print('Entre com o raio')
    raio = float(input())
    pi = 2 * 3.1415 * raio
    return print ('A área do círculo é: ', pi)


def questao9():
    print('Entre com a altura do retangulo.')
    al = float(input())
    print('Entre com a largura do retângulo')
    la = float(input())
    ar = al * la
    return print('A área do retângulo é:', ar)


def questao10():
    print ('Entre com o número de quilômetros percorridos: ')
    km = int(input())
    print('Entre com a quantidade de litros de gasolina consumidos: ')
    l = float(input())
    gasto = km / l 
    return print('O carro consume ', gasto, 'litros por km.')


def questao11():
    print('Entre com a temperatura em C')
    ce =int(input())
    return print(' A temperatura em fahrenheit é', ((ce * 9) / 5) + 32)


def questao12():
    print('Entre com a temperatura em F')
    fa=int(input())
    return print ('A temperatura em Celsius é', ((fa - 32) * 5) / 9)

        
