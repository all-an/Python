import random


def carrega_palavra():
    arquivo = open("palavra.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

def play_fork():

    mensagem_abertura()

    carrega_palavra()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = len(palavras[numero])
    fimMensagem = "Vocẽ perdeu !"
    advinhe1 = "Adivinhe a palavra: >>  "
    print(advinhe1, '  '.join(letras_acertadas))

    while not enforcou and not acertou:

        index = 0
        chute = input("Chute uma letra ? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
            print("Acertou uma letra. Lembre-se digite a penas uma letra.")
        else:
            erros -= 1
            print("Errou ! Você tem mais {} tentativas. ".format(erros))

        # print("Acertou uma letra.")

        enforcou = erros == 0
        acertou = "_" not in letras_acertadas
        print(advinhe1, '  '.join(letras_acertadas))

    if erros > 0:
        fimMensagem = " Parabéns !"
    print(" Fim do Jogo !", fimMensagem)
if __name__ == "__main__":
    play_fork()

def mensagem_abertura():
    print("----Welcome to the Fork Game----")
