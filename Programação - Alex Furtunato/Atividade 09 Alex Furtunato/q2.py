# Faça uma função que recebe um número IPV4 e retorna 
# True ou False se o número IP é válido ou não.

def main():
    ip=input('Informe o IP: ')
    numeros=ip.split('.')
    valido=True
    if len(numeros)!=4:
        valido = False
    else:
        for numero in numeros:
            if int(numero)>255 or int(numero)<0:
                valido = False
    print(valido)

if __name__ == '__main__':
    main()