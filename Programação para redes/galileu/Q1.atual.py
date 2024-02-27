# Leitura dos parâmetros
input_file = input("Digite o nome do arquivo de origem: ")
password = input("Digite a palavra-passe: ")
output_file = input("Digite o nome do arquivo de destino: ")

try:
    # Leitura do arquivo de origem
    with open(input_file, 'rb') as file:
        input_data = file.read()

    password_length = len(password)
    encrypted_data = bytearray()

    # Aplicação do XOR byte a byte
    for i in range(len(input_data)):
        password_byte = ord(password[i % password_length])
        encrypted_byte = input_data[i] ^ password_byte
        encrypted_data.append(encrypted_byte)

    # Escrita do arquivo de destino
    with open(output_file, 'xb') as output_file:
        output_file.write(encrypted_data)

    print("Arquivo criptografado com sucesso!")
except FileNotFoundError:
    print("Arquivo de origem não encontrado.")
except FileExistsError:
    print("Arquivo de destino já existe. Por favor, escolha outro nome para o arquivo de destino.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")