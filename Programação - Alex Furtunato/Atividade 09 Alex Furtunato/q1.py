# Crie uma função que recebe uma palavra e retorna um dicionário onde as chaves
# são as letras únicas encontradas e a quantidade de vezes que a letra apareceu
# na palavra como o valor referente a respectiva chave.

def main():
    # palavra=input('Informe uma palavra: ')
    # for i in palavra:
    #     c=len(palavra[i])
    #     if c==1:
    #         palavra=dict(key=i)
    #     else:
    #         palavra=dict
    # print(palavra)
    letras = {}
    palavra = input('Digite a palavra: ')
    for letra in palavra:
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1
    print(letras)


if __name__ == '__main__':
    main()
