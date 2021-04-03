def play_fork():
    print("----Welcome to the Fork Game----")

<<<<<<< HEAD
    palavra_secreta = "banana"
=======
    palavra_secreta = "python"
>>>>>>> fa057bd07eae419333c5ac22d42b7e173045ef6f

    enforcou = False
    acertou = False

    while not enforcou and not acertou:

<<<<<<< HEAD
        chute = input("Qual letra? ")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print(" Encontrei a letra {} na posição {} ".format(letra, index))
            index = index + 1
=======
    print("jogando . . .")
>>>>>>> fa057bd07eae419333c5ac22d42b7e173045ef6f

        print("Jogando . . .")

    print(" Fim ! ")

if __name__ == "__main__":
    play_fork()
