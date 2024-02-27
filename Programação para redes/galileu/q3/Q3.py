from json import loads
from os import listdir

# essa parte vai verificar os arquivos que podem ser usados
while True:
    anos = []
    for conteudo in listdir():
        if conteudo.startswith("cartola_fc_") and conteudo.endswith(".txt"):
            anos.append(conteudo)
    ano = input("Digite o Ano do arquivo: ")
    if f"cartola_fc_{ano}.txt" in anos:
        break
    else:
        print(f"Identificado os arquivos {anos} \n(para mais adicione arquivos com o formato cartola_fc_nnnn.txt onde nnnn é o ano)")

# aqui ler o arquivo escolhido e coloca no formato json
with open(f"cartola_fc_{ano}.txt", "r", encoding="utf-8") as file:
    dados = loads(file.read())

# aqui server para mapear os jogadores em sua função(pos_id) para facilitar a escolha depois
posições = {"zagueiro": [], "lateral": [], "meia": [], "atacante": [], "goleiro": [], "técnico": []}
for atleta in dados["atletas"]:
    pontuação = atleta["media_num"] * atleta["jogos_num"]
    atleta.update({"pontuação": pontuação})
    if atleta["posicao_id"] == 1:
        posições["zagueiro"].append(atleta)
    elif atleta["posicao_id"] == 2:
        posições["lateral"].append(atleta)
    elif atleta["posicao_id"] == 3:
        posições["meia"].append(atleta)
    elif atleta["posicao_id"] == 4:
        posições["atacante"].append(atleta)
    elif atleta["posicao_id"] == 5:
        posições["goleiro"].append(atleta)
    elif atleta["posicao_id"] == 6:
        posições["técnico"].append(atleta)
# dessa forma fica mais simples realizar o sorted via pontuação futuramente.

# mapeamento de nome e esquema para mostrar e facilitar a escolha
posições_nome = ["zagueiro", "lateral", "meia", "atacante", "goleiro", "técnico"]
esquemas = {"3-4-3": [3, 0, 4, 3, 1, 1],
            "3-5-2": [3, 0, 5, 2, 1, 1],
            "4-3-3": [2, 2, 3, 3, 1, 1],
            "4-4-2": [2, 2, 4, 2, 1, 1],
            "4-5-1": [2, 2, 5, 1, 1, 1],
            "5-3-2": [3, 2, 3, 2, 1, 1],
            "5-4-1": [3, 2, 4, 1, 1, 1]}
print(" ESQUEMA |          Quantidade de Jogadores:")
# dessa forma fica simples adicionar novos esquemas e mostrados via laço for
for esquema, qtd_jogadores in esquemas.items():
     print(f"  {esquema}  | {qtd_jogadores[0]} zagueiros / {qtd_jogadores[1]} laterais / {qtd_jogadores[2]} meias / {qtd_jogadores[3]} atacantes")

# Menu para escolha do esquema
while True:
    esquema_selec = input("Digite seu esquema:")
    if esquema_selec in esquemas.keys():
        break
    else:
        print("Esquema errado digite um esquema acima ex:3-4-3")

# abertura do arquivo para salvar as infomaçoes sobre os jogadores
file = open(f"selecao_cartola_fc{ano}.txt", "w")
file.write("posição;nome;url_foto_atleta;pontuação;time;url_escudo_time\n")

# laço responsavel por mostrar os dados e salva no arquivo acima
for nome_posicao, quantidade in zip(posições_nome, esquemas[esquema_selec]):
    # nesse loop ele vai pegar a lista de posição de jogadores e vai realizar o sorted e vai pegar a quantidade
    # da posição escolhida ex zagueiro, 3 ele vai sortear e pegar os 3 zagueiros com melhor pontuação.
    for j in sorted(posições[nome_posicao], key=lambda dic: dic["pontuação"], reverse=True)[0:quantidade]:
        # aqui ele vai obter dados sobre o time do jogador.
        time_jogador = dados["clubes"][f"{j['clube_id']}"]
        # aqui ele vai mostrar os dados do jogador para o usuario
        print(f"nome: {j['apelido_abreviado']} - time: {time_jogador['nome_fantasia']} - pontuação:{j['pontuação']:.2f}")
        # aqui ele vai gravar os dados do jogador para o arquivo selecao_cartola_fc{ano}.txt
        file.write(f"{j['posicao_id']};{j['nome']};{j['foto']};{j['pontuação']:.2f};{time_jogador['nome_fantasia']};{time_jogador['escudos']['60x60']}\n")

#por fim avisar o salvamento do arquivo e fechamento do arquivo.
print(f"Formação salva com sucesso verifique o arquivo selecao_cartola_fc{ano}.txt")
file.close()
