def play_fork():
    print("----Welcome to the Fork Game----")

    palavra_secreta = "banana"
<<<<<<< HEAD
=======
    palavra_secreta = "python"
>>>>>>> 90117078253f061744ebaa73b6cda94da813f3c5

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
<<<<<<< HEAD
        index = 0
        chute = input("Qual letra ? ")
=======
>>>>>>> 90117078253f061744ebaa73b6cda94da813f3c5

        chute = input("Qual letra? ")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
<<<<<<< HEAD
                index = index + 1
                print("Encontrei a letra {} na posição {} " .format(letra, index))


    #print("jogando . . .")
=======
                print(" Encontrei a letra {} na posição {} ".format(letra, index))
            index = index + 1

            print("jogando . . .")

    print(" Fim ! ")
>>>>>>> 90117078253f061744ebaa73b6cda94da813f3c5

    #print("End of the Game")
if __name__ == "__main__":
    play_fork()
