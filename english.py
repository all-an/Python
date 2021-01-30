import os

# My daughter also has blue eyes.
# Janitor , zelador
# Spills , derramou, entornou
# Waiter , garçom
# Plunder , pilhagem

word1 = "Butterscotch"
sentence1 = "He's rummaging through the cabinets and shelves inside the house."

def part2():
    attempt2 = input("Ele está vasculhando os armários e prateleiras dentro da casa. ")
    if attempt2 == sentence1:
        print("Congratulations!")
    else:
        print("Wrong, correct is >>>", sentence1)
        os.system('cls||clear')
        attempt3 = input("Vasculhando ?: ")
        if attempt3 == "Rummaging":
            print("Nice !")
        else:
            print("Try again !")
        part2() 

def game():
    attempt = input("Manteiga de Caramelo: ")
    if attempt == word1:
        print("Congratulations!")
        part2()
    else:
        print("Wrong, correct is Butterscotch")
        print("Try again")
        game()   

game()
