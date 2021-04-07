def play_fork():
    print("----Welcome to the Fork Game----")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while not enforcou and not acertou:

        index = 0
        chute = input("Qual letra ? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                index = index + 1
                print("Encontrei a letra {} na posição {} " .format(letra, index))

        print("jogando . . .")

    print(" Fim ! ")
if __name__ == "__main__":
    play_fork()
