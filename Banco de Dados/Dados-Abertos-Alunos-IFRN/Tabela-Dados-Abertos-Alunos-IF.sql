CREATE TABLE "cota_sistec"(
    "id_cota_sistec" SERIAL NOT NULL,
    "cota_sistec" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "cota_sistec" ADD PRIMARY KEY("id_cota_sistec");
CREATE TABLE "linha_pesquisa"(
    "id_linha_pesquisa" SERIAL NOT NULL,
    "linha_pesquisa" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "linha_pesquisa" ADD PRIMARY KEY("id_linha_pesquisa");
CREATE TABLE "nome_curso"(
    "id_curso" SERIAL NOT NULL,
    "nome_completo" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "nome_curso" ADD PRIMARY KEY("id_curso");
CREATE TABLE "Alunos"(
    "matricula" VARCHAR(255) NOT NULL,
    "matricula_regular" VARCHAR(255) NOT NULL,
    "nome_completo" VARCHAR(255) NOT NULL,
    "id_aluno" INTEGER NOT NULL,
    "id_situacao" TEXT NOT NULL,
    "id_curso" INTEGER NOT NULL,
    "id_cota_mec" TEXT NOT NULL,
    "id_cota_sistec" VARCHAR(255) NOT NULL,
    "curriculo_lattes" VARCHAR(255) NOT NULL,
    "situacao_sistemica" TEXT NOT NULL,
    "linha de pesquisa" BIGINT NOT NULL,
    "campus" TEXT NOT NULL
);
ALTER TABLE
    "Alunos" ADD PRIMARY KEY("matricula");
CREATE TABLE "situacao"(
    "id_situacao" SERIAL NOT NULL,
    "situacao" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "situacao" ADD PRIMARY KEY("id_situacao");
CREATE TABLE "cota_mac"(
    "id_cota_mec" SERIAL NOT NULL,
    "cota_mec" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "cota_mac" ADD PRIMARY KEY("id_cota_mec");
CREATE TABLE "campi"(
    "campus" VARCHAR(255) NOT NULL,
    "nome_completo" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "campi" ADD PRIMARY KEY("campus");
CREATE TABLE "situacao_sistemica"(
    "id_situacao_sistemica" SERIAL NOT NULL,
    "situacao_sistemica" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "situacao_sistemica" ADD PRIMARY KEY("id_situacao_sistemica");
ALTER TABLE
    "Alunos" ADD CONSTRAINT "alunos_id_curso_foreign" FOREIGN KEY("id_curso") REFERENCES "nome_curso"("id_curso");
ALTER TABLE
    "Alunos" ADD CONSTRAINT "alunos_id_cota_sistec_foreign" FOREIGN KEY("id_cota_sistec") REFERENCES "cota_sistec"("id_cota_sistec");
ALTER TABLE
    "Alunos" ADD CONSTRAINT "alunos_situacao_sistemica_foreign" FOREIGN KEY("situacao_sistemica") REFERENCES "situacao_sistemica"("id_situacao_sistemica");
ALTER TABLE
    "Alunos" ADD CONSTRAINT "alunos_id_cota_mec_foreign" FOREIGN KEY("id_cota_mec") REFERENCES "cota_mac"("id_cota_mec");
ALTER TABLE
    "Alunos" ADD CONSTRAINT "alunos_id_situacao_foreign" FOREIGN KEY("id_situacao") REFERENCES "situacao"("id_situacao");
ALTER TABLE
    "Alunos" ADD CONSTRAINT "alunos_campus_foreign" FOREIGN KEY("campus") REFERENCES "campi"("campus");
ALTER TABLE
    "Alunos" ADD CONSTRAINT "alunos_linha de pesquisa_foreign" FOREIGN KEY("linha de pesquisa") REFERENCES "linha_pesquisa"("id_linha_pesquisa");