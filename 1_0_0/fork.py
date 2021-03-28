
def play_fork():
    print("----Welcome to the Fork Game----")

<<<<<<< HEAD
    secret_word = "banana"
=======
    palavra_secreta = "python"
>>>>>>> 6e2048662d7ba52942093dffd4d9eb8b4dbeab68

    enforcou = False

    acertou = False

<<<<<<< HEAD
    while not forked and not hit:
        attempt = input("Type a character: ")
        print("Playing . . .")
=======
    while not enforcou and not acertou:
        chute = input("Qual letra ? ")

        for letra in palavra_secreta:
            if(chute == letra):
                print(chute)

        print("jogando . . .")
>>>>>>> 6e2048662d7ba52942093dffd4d9eb8b4dbeab68

        index = 0
        for character in secret_word:
            if attempt == character:
                print("I found the character {} at position {}.".format(character,index))
            index = index + 1

    print("End of the Game")

if __name__ == "__main__":
    play_fork()

