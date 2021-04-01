def play_fork():
    print("----Welcome to the Fork Game----")

    palavra_secreta = "python"

    enforcou = False

    acertou = False

    while not enforcou and not acertou:
        chute = input("Qual letra ? ")

        for letra in palavra_secreta:
            if(chute == letra):
                print(chute)

    print("jogando . . .")

    print("End of the Game")

if __name__ == "__main__":
    play_fork()
