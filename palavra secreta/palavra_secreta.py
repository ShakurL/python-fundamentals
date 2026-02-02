import os
tentativas = 0
palavra_secreta = "python"
letras_acertadas = ""

while True:
    palavra_formada = ""
    letra_palpite = input("insira uma letra: ")
    tentativas += 1
    if len(letra_palpite) > 1:
        print("insira apenas uma letra")
        continue
    
    if letra_palpite in palavra_secreta:
        letras_acertadas += letra_palpite
    
    for char in palavra_secreta:
        if char in letras_acertadas:
            palavra_formada += char
        
        else:
            palavra_formada += "*"

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f'Você acertou a palavra secreta "{palavra_secreta}" em {tentativas} tentativas')
        break