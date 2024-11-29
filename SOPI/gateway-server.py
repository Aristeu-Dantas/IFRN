import socket, json

HOST = '127.0.0.1'
PORT = 65432

# Cria um socket UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("Servidor UDP iniciado em", HOST, PORT)

    while True:
        data, addr = s.recvfrom(1024)
        try:
            json_data = json.loads(data.decode())
            result = process_json(json_data)
            response = json.dumps(result).encode()
            s.sendto(response, addr)

        except json.JSONDecodeError:
            print("Erro ao decodificar o JSON:", data)

def process_json(data):
    data["processed"] = True
    return data
