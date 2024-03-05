from Dao.biblioteca import *
from Entidades.ler_arquivos import *

# Função para conectar ao banco de dados
def conectar_banco():
    # Configurações do banco de dados
    server = 'localhost'
    database = 'Avaliacao-Dados-Servidores'
    dbuser = 'postgres'
    userpwd = 'postgres'

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
        descricao_campus = dados['campus']  # Coloque aqui a chave correta para a descrição do campus no CSV
        resultado, id_retorno = campus_dao.inserir_campus(descricao_campus)

        if resultado:
            print(f"Campus '{descricao_campus}' inserido com sucesso! (ID: {id_retorno})")
        else:
            print(f"Erro ao inserir campus '{descricao_campus}'.")

    desconectar_banco(conexao_db)

# Exibe os resultados da consulta de tipos de servidores por campus
def servidoresCampus():
    conexao_db = conectar_banco()
    if not conexao_db:
        return

    print('\nConsultando tipos de servidores por campus\n')
    dao = ServidoresCampusDAO(conexao_db.conexao)
    retorno = dao.consultar_servidores_campus()
    if retorno:
        for i in retorno:
            print(f"Campus: {i[0]:5} Tipo de servidor: {i[1]:<25} Quantidade: {i[2]:<1}")
    else:
        print("Erro ao realizar a consulta.")

    desconectar_banco(conexao_db)

# Exibe os resultados da consulta de docentes por disciplina
def docentesDisciplina():
    conexao_db = conectar_banco()
    if not conexao_db:
        return

    print('\nConsultando docentes por disciplina\n')
    dao = ServidoresCampusDAO(conexao_db.conexao)
    retorno = dao.consultar_docentes_disciplina()
    if retorno:
        for i in retorno:
            print(f"Docente: {i[0]:<45} Disciplina: {i[1]}")
    else:
        print("Erro ao realizar a consulta.")

    desconectar_banco(conexao_db)

# Exibe os resultados da consulta de quantidade de docentes por disciplina e por campus
def quantidadeDocentesDisciplinas():
    conexao_db = conectar_banco()
    if not conexao_db:
        return

    print('\nConsultando quantidade de docentes por disciplinas e por campus\n')
    dao = ServidoresCampusDAO(conexao_db.conexao)
    retorno = dao.consultar_quantidade_docentes_disciplinas()
    if retorno:
        for i in retorno:
            print(f"Disciplina: {i[0]:<60} Campus: {i[1]:<5} Quantidade: {i[2]:<1}")
    else:
        print("Erro ao realizar a consulta.")

    desconectar_banco(conexao_db)
