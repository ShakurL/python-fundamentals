lista_de_compras = []

while True:
    
    comando = input("[i]nserir [a]pagar [e]ditar [l]istar [s]air: ")

    if comando.startswith('i'):
        elemento = (input("oque deseja inserir na lista?: "))
        lista_de_compras.append(elemento)

    elif comando.startswith("e"):
        for i, nome in enumerate(lista_de_compras):
            print (i, nome)
        editar = input("qual item deseja editar na lista?: ")
        editar = int(editar)
        if editar>len(lista_de_compras):
            print("numero invalido")
            continue
        edição = input("insira a edição desejada: ")
        lista_de_compras.insert(editar, edição)

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

    else:
        print("comando inexistente")
