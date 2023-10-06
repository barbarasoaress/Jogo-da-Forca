import random

# Lista de palavras para o jogo
palavras = ["python","programação","algoritmo","desenvolvedor"]

# Função para escolher uma palavra aleatória da lista
def escolher_palavra():
    return random.choice(palavras)

# Função para inicializar o jogo
def iniciar_jogo():
    palavra = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 6  # O jogador tem 6 chances
    palavra_misteriosa = "_" * len(palavra)

    print("Bem-vindo ao jogo da forca!")
    print(palavra_misteriosa)

    while True:
        letra = input("Adivinhe uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já adivinhou essa letra. Tente novamente.")
            continue

        if letra not in palavra:
            tentativas -= 1

        letras_adivinhadas.append(letra)

        palavra_misteriosa = atualizar_palavra_misteriosa(palavra, letras_adivinhadas)

        print(palavra_misteriosa)
        print(f"Tentativas restantes: {tentativas}")

        if palavra_misteriosa == palavra:
            print("Parabéns! Você venceu!")
            break

        if tentativas == 0:
            print(f"Game over! A palavra era: {palavra}")
            break

# Função para atualizar a palavra misteriosa com letras adivinhadas
def atualizar_palavra_misteriosa(palavra, letras_adivinhadas):
    palavra_misteriosa = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            palavra_misteriosa += letra
        else:
            palavra_misteriosa += "_"
    return palavra_misteriosa

if __name__ == "__main__":
    iniciar_jogo()