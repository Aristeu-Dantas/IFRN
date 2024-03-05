import sys, os
from Entidades.conexao import *
from Entidades.constantes import *
from Entidades.ler_arquivos import *
from view.consultas import *

def main():
    # Lendo os dados do arquivo CSV
    arquivo_csv = os.path.join(APP_DIR, 'arquivo.csv')
    lido, retorno_dados = ler_arquivo(arquivo_csv)

    if not lido:
        sys.exit()

    # Conectando ao banco de dados
    conexao_db = DB_HOST, DB_NAME, DB_USER, DB_PASS

    if not conexao_db[0]:
        print(conexao_db[1])
        sys.exit()

    banco = conexao_db[1]
    while True:
        escolha = input('Escolha uma das opções: \n0 - Finalizar a execução do programa. \n1 - Adicionar informações ao banco de dados. \n2 - Pesquisar categorias de servidores por campus \n3 - Verificar docentes por área de estudo \n4 - Consultar a quantidade de docentes por áreas de estudo e campus')

        if escolha == '0':
            print("\nENCERRANDO O PROGRAMA!\n")
            banco.close()
            sys.exit()
        elif escolha == '1':
            inserir_dados()
        elif escolha == '2':
            servidoresCampus()
        elif escolha == '3':
            docentesDisciplina()
        elif escolha == '4':
            quantidadeDocentesDisciplinas()
        else:
            print("\nOpção invalida! Tente novamente...\n")

if __name__ == "__main__":
    main()
