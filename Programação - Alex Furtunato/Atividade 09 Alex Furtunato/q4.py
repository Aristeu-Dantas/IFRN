# Faça um script para criptografar uma string passada pelo usuário 
# (somente caracteres) usando para isso a criptografia "Cesar":
# Nota 1: A cifragem de César, ficou conhecida assim porque Julius Caesar 
# a utilizava em suas correspondências privadas. A codificação Caesar 
# consiste em fazer um deslocamento de cada caractere substituindo-os por 
# caracteres algumas posições abaixo na tabela ASCII. Por exemplo, 
# em um deslocamento de 3, cada letra é substituída por uma letra 3 posições abaixo. 
# No caso da letra D, ela seria substituída pela letra A.
# Nota 2: Em Python, utiliza-se a built-in ord('x') para descobrir o código 
# ASCII (número inteiro) de um caractere. E utiliza-se a built-in chr(inteiro) para 
# encontrar o caractere correspondente ao código (número inteiro) passado como parâmetro.
# Nota 3: A cifragem deve substituir as letras conforme a cifragem e o espaço 
# pelo caractere '$'. pontuações não devem ser substituídas. 
# Nota 4: Tabela ASCII:
# Caracteres              Códigos
# A – Z                       65 – 90
# a – z                       97 – 122

frase=input('Digite uma frase: ')
t=''
passo= -3

for i in frase:
    cod=ord(i)
    if (65<=cod<=90)or(97<=cod<=122):
        cod_t=cod+passo
        if (cod_t<65)or(90<cod_t<97):
            cod_t=cod_t+26
        t=t+chr(cod_t)
    else:
        t=t+chr(cod)

print(f'Frase original: {frase}')
print(f'Frase cifrada: {t}')