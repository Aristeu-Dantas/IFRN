from Dao.biblioteca import *
from Entidades.ler_arquivos import *

# Função para conectar ao banco de dados
def conectar_banco():
    # Configurações do banco de dados
    server = 'seu_servidor'
    database = 'seu_banco_de_dados'
    dbuser = 'seu_usuario'
    userpwd = 'sua_senha'

    # Conectando ao banco de dados
    conexao_db = BancoDados(server, database, dbuser, userpwd)
    conexao_db.conectar()

    if not conexao_db.conexao:
        print("Erro ao conectar ao banco de dados.")
        return None

    return conexao_db

# Função para desconectar do banco de dados
def desconectar_banco(conexao_db):
    if conexao_db:
        conexao_db.desconectar()

# Função para ler os dados do arquivo CSV e inserir os campi no banco de dados
def inserir_dados():
    # Configuração do caminho do arquivo CSV
    arquivo_csv = 'dados_extraidos_recursos_servidores.csv'

    conexao_db = conectar_banco()
    if not conexao_db:
        return

    # Lendo os dados do arquivo CSV
    lido, retorno_dados = ler_arquivo(arquivo_csv)

    if not lido:
        print("Erro ao ler o arquivo CSV.")
        desconectar_banco(conexao_db)
        return

    campus_dao = CampusDAO(conexao_db.conexao)

    for matricula, dados in retorno_dados.items():
        descricao_campus = dados['id_campus']
        resultado, id_retorno = campus_dao.inserir_campus(descricao_campus)

        if resultado:
            print(f"Campus '{descricao_campus}' inserido com sucesso! (ID: {id_retorno})")
        else:
            print(f"Erro ao inserir campus '{descricao_campus}'.")

    desconectar_banco(conexao_db)

if __name__ == "__main__":
    inserir_dados()
