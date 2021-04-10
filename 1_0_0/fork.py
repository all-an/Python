def play_fork():
    print("----Welcome to the Fork Game----")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    erros = 6
    fimMensagem = "Vocẽ perdeu !"

    while not enforcou and not acertou:

        index = 0
        chute = input("Qual letra ? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
            print("Acertou uma letra.")
        else:
            erros -= 1
            print("Errou ! Você tem mais {} tentativas. ".format(erros))

        # print("Acertou uma letra.")

        enforcou = erros == 0
        acertou = "_" not in letras_acertadas
        print('  '.join(letras_acertadas))

    if erros > 0:
        fimMensagem = " Parabéns !"
    print(" Fim do Jogo !", fimMensagem)
if __name__ == "__main__":
    play_fork()
