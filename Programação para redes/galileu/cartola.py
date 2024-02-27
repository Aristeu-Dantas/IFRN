import json

def ano_escolhido():
    while True:
        ano = input('Informe o ano em que se deseja acessar os dados do Cartola FC (2021 ou 2022): ')
        
        try:
            ano = int(ano)
        except ValueError:
            print('Resposta inválida. Vamos tentar novamente, digite um ano válido (2021 ou 2022).')
            continue
        
        if ano == 2021 or ano == 2022:
            print(f'Você escolheu o ano {ano}.')
            return ano 
        else:
            print('Ano inválido. Por favor, digite 2021 ou 2022.')
            continue

def abrir_arquivo(ano):
    dados_cartola = []

    if ano == 2021:
        with open('cartola_fc_2021.txt', 'r', encoding='utf-8') as arquivo:
            print('Abrindo arquivo do Cartola FC 2021...')
    elif ano == 2022:
        with open('cartola_fc_2022.txt', 'r', encoding='utf-8') as arquivo:
            print('Abrindo arquivo do Cartola FC 2022...')
    else:
        print('Ano inválido.')

    return dados_cartola


def obter_esquema_tatico():
    print("Esquemas táticos disponíveis:")
    print("1. 3-4-3 - 3 zagueiros, 4 meias, 3 atacantes")
    print("2. 3-5-2 - 3 zagueiros, 5 meias, 2 atacantes")
    print("3. 4-3-3 - 4 zagueiros, 3 meias, 3 atacantes")
    print("4. 4-4-2 - 4 zagueiros, 4 meias, 2 atacantes")
    print("5. 4-5-1 - 4 zagueiros, 5 meias, 1 atacante")
    print("6. 5-3-2 - 5 zagueiros, 3 meias, 2 atacantes")
    print("7. 5-4-1 - 5 zagueiros, 4 meias, 1 atacante")

    while True:
        try:
            escolha = int(input("Escolha o número correspondente ao esquema tático desejado: "))
            if escolha < 1 or escolha > 7:
                print("Escolha inválida. Por favor, escolha um número de 1 a 7.")
                continue
            else:
                return escolha
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    return

def selecionar_jogadores(esquema_escolhido, dados_jogadores):
    # Mapeamento entre esquema tático e quantidade de jogadores por posição
    esquemas = {
        1: {'zagueiro': 3, 'lateral': 0, 'meia': 4, 'atacante': 3},
        2: {'zagueiro': 3, 'lateral': 0, 'meia': 5, 'atacante': 2},
        3: {'zagueiro': 2, 'lateral': 2, 'meia': 3, 'atacante': 3},
        4: {'zagueiro': 4, 'lateral': 0, 'meia': 4, 'atacante': 2},
        5: {'zagueiro': 4, 'lateral': 0, 'meia': 5, 'atacante': 1},
        6: {'zagueiro': 5, 'lateral': 0, 'meia': 3, 'atacante': 2},
        7: {'zagueiro': 5, 'lateral': 0, 'meia': 4, 'atacante': 1}
    }

    esquema = esquemas.get(esquema_escolhido)
    if esquema is None:
        print("Esquema tático não encontrado.")
        return []

    jogadores_selecionados = []
    for posicao, quantidade in esquema.items():
        jogadores_posicao = [jogador for jogador in dados_jogadores if jogador['posicao'] == posicao]
        jogadores_posicao.sort(key=lambda x: x['pontuacao'], reverse=True)
        jogadores_selecionados.extend(jogadores_posicao[:quantidade])

    return jogadores_selecionados

def exibir_lista_jogadores(jogadores_selecionados):
    if not jogadores_selecionados:
        print("Nenhum jogador selecionado.")
        return

    print("Lista de Jogadores Selecionados:")
    for jogador in jogadores_selecionados:
        print(f"Nome: {jogador['nome']}")
        print(f"Posição: {jogador['posicao']}")
        print(f"Pontuação: {jogador['pontuacao']}")
        print(f"Time: {jogador['time']}")
        print(f"URL da Foto do Atleta: {jogador['url_foto_atleta']}")
        print(f"URL do Escudo do Time: {jogador['url_escudo_time']}")
        print("-" * 30)


def salvar_dados_em_arquivo(jogadores_selecionados, ano):
    # Nome do arquivo com base no ano informado
    nome_arquivo = f"selecao_cartola_fc_{ano}.txt"

    with open(nome_arquivo, "w") as arquivo:
        # Escreve a primeira linha com os cabeçalhos
        arquivo.write("posição;nome;url_foto_atleta;pontuação;time;url_escudo_time\n")

        for jogador in jogadores_selecionados:
            # Escreve os dados de cada jogador no arquivo separados por ponto e vírgula
            arquivo.write(f"{jogador['posicao']};{jogador['nome']};{jogador['url_foto_atleta']};"
                          f"{jogador['pontuacao']};{jogador['time']};{jogador['url_escudo_time']}\n")

# Exemplo de como chamar a função com a lista de jogadores selecionados e o ano
jogadores_selecionados = [
    {'nome': 'Jogador 1', 'posicao': 'Zagueiro', 'pontuacao': 8.5, 'time': 'Flamengo', 
     'url_foto_atleta': 'https://foto-jogador-1', 'url_escudo_time': 'https://escudo-flamengo'},
    {'nome': 'Jogador 2', 'posicao': 'Meia', 'pontuacao': 9.2, 'time': 'Corinthians', 
     'url_foto_atleta': 'https://foto-jogador-2', 'url_escudo_time': 'https://escudo-corinthians'},
    # ... adicione mais jogadores com suas informações
]

ano_desejado = ano_escolhido()  # Chama a função para obter o ano desejado
arquivo_dados = abrir_arquivo(ano_desejado)  # Abre o arquivo correspondente ao ano
if arquivo_dados is not None:
    esquema_tatico = obter_esquema_tatico()  # Obtém o esquema tático escolhido pelo usuário
    jogadores_selecionados = selecionar_jogadores(esquema_tatico, arquivo_dados)  # Seleciona os jogadores com base no esquema
    exibir_lista_jogadores(jogadores_selecionados)  # Exibe a lista de jogadores selecionados
    salvar_dados_em_arquivo(jogadores_selecionados, ano_desejado)  # Salva os dados dos jogadores em um arquivo
else:
    print("Não foi possível abrir o arquivo de dados para o ano selecionado.")