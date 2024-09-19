#ATENÇÃO!! PARA INTEGRAR O SCRIPT NA VM É NECESSÁRIO BAIXAR ALGUMAS BIBLIOTECAS DE INTEGRAÇÃO DO WINDOWS PARA UBUNTU.

import csv, agi, time

def main():
    agi = agi.AGI()

    # Reproduzir mensagem de boas-vindas
    agi.exec("Playback", bem_vindo)

    # Menu principal
    agi.exec("Playback", iniciar_ou_resultados)
    agi.exec("Read", "opcao")

    # Processar a opção escolhida
    if agi.get_variable("opcao") == "1":
        iniciar_enquete(agi)
    elif agi.get_variable("opcao") == "2":
        mostrar_resultados(agi)
    else:
        agi.exec("Playback", opcao_invalida)

def iniciar_enquete(agi):
    # Lista para armazenar as respostas do usuário
    respostas = []

    # Perguntas e opções
    perguntas = [
        {"pergunta": satisfacao, "opcoes": ["sim", "não"]},
        {"pergunta": pagar_terceirizar, "opcoes": ["sim", "não"]},
        {"pergunta": qual_area, "opcoes": ["sim", "não"]}
    ]

    # Fazer as perguntas
    for pergunta in perguntas:
        agi.exec("Playback", pergunta["pergunta"])
        for i, opcao in enumerate(pergunta[digite_a_tecla_1_para_sim]):
            agi.exec("Playback", f"{i+1}. {opcao}")

        # Ler a resposta e aguardar 5 segundos
        agi.exec("Read", "resposta", "")
        time.sleep(5)  # Aguarda 5 segundos
        resposta = agi.get_variable("resposta")
        respostas.append(resposta)

    # Salvar as respostas em um arquivo CSV
    with open('resultados.csv', 'a', newline='') as csvfile:
        fieldnames = ['satisfacao_marcas', 'preferencia_servico', 'area_tecnologia']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(dict(zip(fieldnames, respostas)))

def mostrar_resultados(agi):
    # Carregar os dados do arquivo CSV e calcular os resultados
    import collections
    with open('resultados.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        resultados = {}
        for row in reader:
            for key, value in row.items():
                resultados.setdefault(key, collections.Counter())[value] += 1

if __name__ == "__main__":
    main()
