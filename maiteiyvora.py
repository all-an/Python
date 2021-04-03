import os

# My daughter also has blue eyes.
# Janitor , zelador
# Spills , derramou, entornou
# Waiter , garçom
# Plunder , pilhagem

word1 = "Yvypora"
frase1 = "Ñande Yvy"
frase2 = "Ñanderuvusú"

def part2():
    attempt2 = input("Nossa terra ?")
    if attempt2 == frase1:
        print("Parabéns")
    else:
        print("Errado, o correto é >>>", frase1)
        os.system('cls||clear')
        attempt3 = input("Gente ?: ")
        if attempt3 == word1:
            print("Legal !")
        else:
            print("Tente Novamente !")
        part2() 

def game():
    attempt = input("O primeiro ? ")
    if attempt == frase2:
        print("Parabéns")
        part2()
    else:
        print("Wrong, correct is ", frase2)
        print("Tente Novamente !")
        game()   

game()
