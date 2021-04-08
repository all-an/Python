def play_fork():
    print("----Welcome to the Fork Game----")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    erros = 6

    while not enforcou and not acertou:

        index = 0
        chute = input("Qual letra ? ")
        chute = chute.strip()

        if(chute.upper() in palavra_secreta.upper()):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1
            print("Acertou uma letra.")
        else:
            erros -= 1
            print("Errou ! Você tem mais {} tentativas. ".format(erros))

        # print("Acertou uma letra.")

        enforcou = erros == 0
        print('  '.join(letras_acertadas))

    print(" Fim ! ")
if __name__ == "__main__":
    play_fork()
