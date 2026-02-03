lista_de_compras = []

while True:
    
    comando = input("[i]nserir [a]pagar [l]istar [s]air: ")

    if comando.startswith('i'):
        elemento = (input("oque deseja inserir na lista?: "))
        lista_de_compras.append(elemento)

    elif comando.startswith('a'):
        for i, nome in enumerate(lista_de_compras):
            print(i, nome)
        apagar = input("qual é o numero do elemento que deseja apagar da lista?: ")
        apagar = int(apagar)
        if apagar>len(lista_de_compras):
            print("numero invalido")
            continue
        lista_de_compras.pop(apagar)

    elif comando.startswith("l"):
        
        for i, nome in enumerate(lista_de_compras):
            print(i, nome)
    
    elif comando.startswith("s"):
        print("saiu")
        break