while True:
    operaçoes_validas=['+', 'x', '-', '/']

    num_1=int(input('insira um numero:'))
    operacao=input("insira a operaçao desejada:'+' adição 'x' multiplicação '-' subtração '/' divisão ")
    if operacao not in operaçoes_validas or len(operacao)>1:
        print('operaçao invalida')
        break

    num_2=int(input('insira outro numero:'))
    
    operacao_add=operacao.startswith('+')
    operacao_mult=operacao.startswith('x')
    operacao_sub=operacao.startswith('-')
    operacao_div=operacao.startswith('/')

    if operacao_add==True :
        print(num_1+num_2)
    elif operacao_mult==True :
        print(num_1*num_2)
    elif operacao_sub==True :
        print(num_1-num_2)
    elif operacao_div==True :
        print(num_1/num_2)

    repetir=input('quer repetir ? [s]im:')
    repetir=repetir.lower()
    if repetir[0]=="s":
        continue
    else:
        print('saiu')
        break