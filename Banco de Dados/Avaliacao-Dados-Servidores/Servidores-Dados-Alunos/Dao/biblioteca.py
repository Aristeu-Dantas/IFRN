import psycopg2
# Classe para gerenciar a conexão com o banco de dados PostgreSQL
class BancoDados:
    def __init__(self, server, database, dbuser, userpwd):
        self.server = server
        self.database = database
        self.dbuser = dbuser
        self.userpwd = userpwd
        self.conexao = None

    def conectar(self):         # Tenta estabelecer a conexão com o banco
        try:
            self.conexao = psycopg2.connect(
                f'dbname={self.database} user={self.dbuser} host={self.server} password={self.userpwd}'
            )
        except:
            self.conexao = None

    def desconectar(self):        # Fecha a conexão com o banco, se estiver aberta
        if self.conexao:
            self.conexao.close()

# Classe para realizar consultas relacionadas às tabelas 'servidor' e 'campus'
class ServidoresCampusDAO:
    def __init__(self, conexao):        # Inicializa a conexão com o banco
        self.conexao = conexao

    def consultar_servidores_campus(self):
        try:
            cursor = self.cursor()
            string_sql = "SELECT campus.nome_campus as sigla, categoria.nome_categoria as categoria, " \
                     "COUNT(servidor.matricula) AS qt_servidores " \
                     "FROM servidor " \
                     "INNER JOIN campus ON servidor.id_campus = campus.id_campus " \
                     "INNER JOIN categoria ON servidor.id_categoria = categoria.id_categoria " \
                     "GROUP BY campus.nome_campus, categoria.nome_categoria;"
            cursor.execute(string_sql)
            return cursor.fetchall()
        except:
            return []

    def consultar_docentes_disciplina(self):
        try:
            cursor = self.conexao.cursor()
            strSQL = "SELECT servidor.nome, disciplina_ingresso.nome_disciplina AS disciplina " \
                    "FROM servidor " \
                    "INNER JOIN disciplina_ingresso ON servidor.id_disciplina = disciplina_ingresso.id_disciplina " \
                    "WHERE servidor.categoria = 'docente' " \
                    "ORDER BY disciplina_ingresso.nome_disciplina;"
            cursor.execute(strSQL)
            return cursor.fetchall()
        except:
            return []


def consultar_quantidade_docentes_disciplinas(self):
    try:
        cursor = self.conexao.cursor()
        strSQL = "SELECT disciplina_ingresso.nome_disciplina AS disciplina, " \
                 "campus.nome_campus AS sigla, " \
                 "COUNT(servidor.matricula) AS qt_disciplinas " \
                 "FROM servidor " \
                 "INNER JOIN disciplina_ingresso ON servidor.id_disciplina = disciplina_ingresso.id_disciplina " \
                 "INNER JOIN campus ON servidor.id_campus = campus.id_campus " \
                 "WHERE servidor.categoria = 'docente' " \
                 "GROUP BY disciplina_ingresso.nome_disciplina, campus.nome_campus " \
                 "ORDER BY disciplina_ingresso.nome_disciplina;"
        cursor.execute(strSQL)
        return cursor.fetchall()
    except:
        return []

class CampusDAO:
    def __init__(self, conexao):
        # Inicia a conexão com o banco
        self.conexao = conexao

    def inserir_campus(self, descricao):
        # Insere um novo campus na tabela 'campus'
        try:
            cursor = self.conexao.cursor()
            strSQL = f"INSERT INTO campus (nome_campus) VALUES ('{descricao}') RETURNING id_campus;"
            cursor.execute(strSQL)
            id_retorno = cursor.fetchone()[0]
            self.conexao.commit()
            return True, id_retorno
        except:
            self.conexao.rollback()
            return False, None

    def listar_campus(self):
        # Lista todos os campi cadastrados na tabela 'campus'
        try:
            cursor = self.conexao.cursor()
            strSQL = "SELECT * FROM campus;"
            cursor.execute(strSQL)
            return cursor.fetchall()
        except:
            return []
