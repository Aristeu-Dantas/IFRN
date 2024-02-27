# Write a program that reads the first 6 bytes of the attached JPEG image. In the
# positions 4 and 5 there is a value that specifies the size of the metadata present in this
# image. Get this number (call it app1DataSize). Close the file.
# • Open the file again, read 4 bytes and ignore them. Now read the number of
# bytes in app1DataSize for app1Data. In position 16 of app1Data there is
# 2 bytes that indicate how much metadata this image has. Discover it and report back.
# • From position 18 of app1Data there is actually metadata. Each
# metadata has the format:
# • 2bytes - what is the metadata. You can get the entire list here:

# https://exiftool.org/TagNames/EXIF.html

# • 2bytes - the type of metadata. Possible values ​​are ( 1- unsigned
# byte; 2 – string; 3 – unsigned short; 4 – unsigned long, ...)
# • 4 bytes - the number of repetitions this metadata has. Example:

# It has an integer type, but it is repeated 5 times.

# • 4 bytes - the metadata value. If more than 4 bytes are needed,
# indicates the offset in the file where the value is, counted from
# starting from position 12 (that is, you must add 12 to reach
# actual position).

# Identify from the metadata the height and width of this image. O
# metadata for height is 0x0101 and for width 0x0100.

import struct

# Abre o arquivo da imagem JPEG
with open("imagem.jpg", "rb") as file:
    # Lê os primeiros 6 bytes
    data = file.read(6)

    # Obtém o tamanho dos metadados (app1DataSize) nas posições 4 e 5
    app1_data_size = (data[4] << 8) | data[5]

# Abre o arquivo novamente
with open("imagem.jpg", "rb") as file:
    # Pula os primeiros 10 bytes (4 bytes ignorados e 6 bytes lidos anteriormente)
    file.read(10)

    # Lê o número de bytes em app1DataSize para app1Data
    app1_data = file.read(app1_data_size)

    # Lê o número de metadados
    num_metadados = (app1_data[16] << 8) | app1_data[17]

    # Inicializa dicionários para armazenar os metadados
    metadados = {}

    # Loop para ler os metadados
    offset = 18
    for _ in range(num_metadados):
        metadado = (app1_data[offset] << 8) | app1_data[offset + 1]
        tipo_metadado = (app1_data[offset + 2] << 8) | app1_data[offset + 3]
        num_repeticoes = struct.unpack('>I', app1_data[offset + 4:offset + 8])[0]
        valor_offset = (app1_data[offset + 8] << 24) | (app1_data[offset + 9] << 16) | (app1_data[offset + 10] << 8) | app1_data[offset + 11]

        # Verifica se o valor do metadado é armazenado no arquivo ou diretamente
        if tipo_metadado == 1:
            valor = struct.unpack('B', app1_data[valor_offset + 12:valor_offset + 13])[0]
        elif tipo_metadado == 3:
            valor = (app1_data[valor_offset + 12] << 8) | app1_data[valor_offset + 13]
        else:
            # Se o tipo do metadado não for suportado, pule para o próximo
            offset += 20
            continue

        metadados[metadado] = valor
        offset += 20

    # Verifica a altura (0x0101) e a largura (0x0100) da imagem nos metadados
    altura = metadados.get(0x0101)
    largura = metadados.get(0x0100)

    # Exibe a altura e a largura da imagem
    print(f"Altura da imagem: {altura}")
    print(f"Largura da imagem: {largura}")
