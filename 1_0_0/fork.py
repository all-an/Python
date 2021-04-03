def play_fork():
    print("----Welcome to the Fork Game----")

    palavra_secreta = "banana"
    palavra_secreta = "python"

    enforcou = False
    acertou = False

    while not enforcou and not acertou:

        chute = input("Qual letra? ")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print(" Encontrei a letra {} na posição {} ".format(letra, index))
            index = index + 1

            print("jogando . . .")

    print(" Fim ! ")

if __name__ == "__main__":
    play_fork()
