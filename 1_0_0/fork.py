
def play_fork():
    print("----Welcome to the Fork Game----")

    secret_word = "banana"

    forked = False

    hit = False

    while not forked and not hit:
        attempt = input("Type a character: ")
        print("Playing . . .")

        index = 0
        for character in secret_word:
            if attempt == character:
                print("I found the character {} at position {}.".format(character,index))
            index = index + 1

    print("End of the Game")

if __name__ == "__main__":
    play_fork()
