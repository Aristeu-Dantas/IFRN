-- Tabela servidor
CREATE TABLE servidor (
    matricula BIGINT NOT NULL PRIMARY KEY,
    nome TEXT NOT NULL,
    categoria VARCHAR(255) NOT NULL,
    cargo BIGINT NOT NULL,
    curriculo_lattes VARCHAR(255) NOT NULL,
    url_foto_75x100 VARCHAR(255) NOT NULL,
    id_setor BIGINT NOT NULL,
    id_disciplina BIGINT NOT NULL,
    id_funcao BIGINT NOT NULL,
    id_jornada BIGINT NOT NULL,
    id_campus BIGINT NOT NULL,
    id_telefones BIGINT NOT NULL,
    FOREIGN KEY (id_setor) REFERENCES setor_suap (id_setor),
    FOREIGN KEY (id_disciplina) REFERENCES disciplina_ingresso (id_disciplina),
    FOREIGN KEY (id_funcao) REFERENCES funcao (id_funcao),
    FOREIGN KEY (id_jornada) REFERENCES jornada_trabalho (id_jornada),
    FOREIGN KEY (id_campus) REFERENCES campus (id_campus),
    FOREIGN KEY (id_telefones) REFERENCES telefone_institucionais (id_telefone)
);

-- Tabela jornada_trabalho
CREATE TABLE jornada_trabalho (
    id_jornada BIGINT NOT NULL PRIMARY KEY,
    JornadaTrabalho VARCHAR(255) NOT NULL
);

-- Tabela setor_suap
CREATE TABLE setor_suap (
    id_setor BIGINT NOT NULL PRIMARY KEY,
    nome_setor VARCHAR(255) NOT NULL
);

-- Tabela campus
CREATE TABLE campus (
    id_campus BIGINT NOT NULL PRIMARY KEY,
    nome_campus VARCHAR(255) NOT NULL
);

-- Tabela telefone_institucionais
CREATE TABLE telefone_institucionais (
    id_telefone BIGINT NOT NULL PRIMARY KEY,
    ramal BIGINT NOT NULL,
    numero_telefone BIGINT NOT NULL
);

-- Tabela funcao
CREATE TABLE funcao (
    id_funcao BIGINT NOT NULL PRIMARY KEY,
    nome_funcao BIGINT NOT NULL
);

-- Tabela disciplina_ingresso
CREATE TABLE disciplina_ingresso (
    id_disciplina BIGINT NOT NULL PRIMARY KEY,
    nome_disciplina VARCHAR(255) NOT NULL
);
