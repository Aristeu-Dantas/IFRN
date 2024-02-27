# Faça um programa que lê um arquivo com um texto (Arquivo "ex08-exemplo-texto.txt" fornecido em anexo)
# e deve salvar o conteúdo alterado em um novo arquivo denominado "texto_a_maiuscula.txt". 
# A alteração aplicada no novo arquivo deverá ser todas as letras "a" das palavras devem ser escritas
# em maiúsculas mantendo o restante de todas as letras em minúsculas.

with open('ex08-exemplo-texto.txt', 'r', encoding="utf-8") as novo_arquivo:
    ler=novo_arquivo.read()
print(ler)

with open('texto_a_maiuscula.txt', 'w')as arquivo_m:
    novo_arquivo.replace('a','A')
    arquivo_m.write(novo_arquivo)
print(arquivo_m)