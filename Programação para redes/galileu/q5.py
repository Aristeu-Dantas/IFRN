import os
import requests
import json

def main():
    # Solicite ao usuário o nome do diretório
    diretorio = input("Digite o nome do diretório da foto: ")

    # Lista de todas as imagens JPEG no diretório
    imagens = []
    cidades = {}

    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(".jpeg"):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            imagens.append(caminho_arquivo)

    # Itere sobre todas as imagens JPEG
    for imagem in imagens:
        # Leia os metadados
        metadados = ler_metadados(imagem)

        # Exiba as informações da imagem
        exibir_info(metadados)

        # Obtenha a cidade da foto
        cidade = obter_cidade(metadados)

        # Atualize o contador de cidades
        if cidade not in cidades:
            cidades[cidade] = 1
        else:
            cidades[cidade] += 1

    # Exiba o número de fotos por cidade
    for cidade, qtd in cidades.items():
        print(f"{cidade}: {qtd}")

def ler_metadados(imagem):
    # Abra o arquivo da imagem
    with open(imagem, "rb") as f:
        # Leia os primeiros 2 bytes do arquivo
        magic_bytes = f.read(2)

        # Verifique se o arquivo é uma imagem JPEG
        if magic_bytes != b"\xFF\xD8\xFF\xE1":
            return None

        # Leia os metadados da imagem
        metadados = {}
        f.seek(2)
        while True:
            # Leia o identificador do metadado
            id = f.read(2)

            # Se o fim do arquivo foi atingido, termine
            if id == b"":
                break

            # Leia o tipo do metadado
            t = f.read(2)

            # Leia o número de repetições
            n = f.read(4)

            # Leia o valor do metadado
            v = f.read(4)

            # Adicione o metadado ao dicionário
            metadados[id] = (t, n, v)

    return metadados

def exibir_info(metadados):
    # Exiba a largura e a altura da imagem
    print(f"Largura: {metadados[0x0100][2]}")
    print(f"Altura: {metadados[0x0101][2]}")

    # Exiba o fabricante da câmera
    print(f"Fabricante: {metadados[0x010F][2]}")

    # Exiba o modelo da câmera
    print(f"Modelo: {metadados[0x0110][2]}")

    # Exiba a data e a hora da captura
    print(f"Data e hora: {metadados[0x9003][2]}")

    # Exiba a latitude e a longitude
    latitude = metadados[0x8825][2]
    longitude = metadados[0x8826][2]
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

def obter_cidade(metadados):
    # Obtenha a latitude e a longitude da foto
    latitude = metadados[0x8825][2]
    longitude = metadados[0x8826][2]

    # Faça uma requisição ao serviço Nominatim
    local = requests.get(
        "https://nominatim.openstreetmap.org/"
        + "reverse?"
        + f"lat={latitude}&lon={longitude}"
        + "&format=json"
    )

    # Converta a resposta em um dicionário
    local = json.loads(local.text)

    # Obtenha o nome da cidade
    cidade = local["address"]["city"]

    # Verifique se a cidade é válida
    if cidade not in local["address"]:
        cidade = "Desconhecido"

    return cidade

if __name__ == "__main__":
    main()
