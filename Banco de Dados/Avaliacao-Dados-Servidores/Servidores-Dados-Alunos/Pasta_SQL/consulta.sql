-- Consulta para obter a quantidade de servidores por campus e categoria
SELECT
    campus.nome_campus AS sigla,
    categoria.nome_categoria AS categoria,
    COUNT(servidor.matricula) AS qt_servidores
FROM
    servidor
INNER JOIN campus ON servidor.id_campus = campus.id_campus
INNER JOIN categoria ON servidor.id_categoria = categoria.id_categoria
GROUP BY
    campus.nome_campus,
    categoria.nome_categoria;
-- Esta consulta retorna a quantidade de servidores agrupados por campus e categoria.
-- Ela utiliza as tabelas 'servidor', 'campus' e 'categoria' e faz um INNER JOIN para relaciona-las.
-- Em seguida, o resultado e agrupado pelo nome do campus e categoria, e o COUNT e usado para contar a quantidade de servidores.

-- Consulta para obter os docentes por disciplina de ingresso no IFRN
SELECT
    servidor.nome,
    disciplina_ingresso.nome_disciplina AS disciplina
FROM
    servidor
INNER JOIN disciplina_ingresso ON servidor.id_disciplina = disciplina_ingresso.id_disciplina
INNER JOIN categoria ON categoria.id_categoria = servidor.id_categoria
WHERE
    categoria.nome_categoria = 'docente'
ORDER BY
    disciplina_ingresso.nome_disciplina;
-- Esta consulta retorna os docentes agrupados por disciplina de ingresso no IFRN.
-- Ela utiliza as tabelas 'servidor', 'disciplina_ingresso' e 'categoria' e faz um INNER JOIN para relaciona-las.
-- O resultado e filtrado para mostrar apenas os servidores da categoria 'docente'.
-- Por fim, os resultados sao ordenados por nome da disciplina de ingresso.

-- Consulta para obter a quantidade de docentes por disciplina de ingresso em cada campus
SELECT
    disciplina_ingresso.nome_disciplina AS disciplina,
    campus.nome_campus AS sigla,
    COUNT(servidor.matricula) AS qt_disciplinas
FROM
    servidor
INNER JOIN disciplina_ingresso ON servidor.id_disciplina = disciplina_ingresso.id_disciplina
INNER JOIN categoria ON categoria.id_categoria = servidor.id_categoria
INNER JOIN campus ON servidor.id_campus = campus.id_campus
WHERE
    categoria.nome_categoria = 'docente'
GROUP BY
    disciplina_ingresso.nome_disciplina,
    campus.nome_campus;
-- Esta consulta retorna a quantidade de docentes agrupados por disciplina de ingresso em cada campus do IFRN.
-- Ela utiliza as tabelas 'servidor', 'disciplina_ingresso', 'categoria' e 'campus' e faz um INNER JOIN para relaciona-las.
-- O resultado e filtrado para mostrar apenas os servidores da categoria 'docente'.
-- Em seguida, o resultado e agrupado pelo nome da disciplina de ingresso e pelo nome do campus,
-- e o COUNT e usado para contar a quantidade de docentes em cada disciplina e campus.
