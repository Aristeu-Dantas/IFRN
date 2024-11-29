import socket, json

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    data = json.dumps({"message": "Hello, server!"}).encode()
    s.sendto(data, (HOST, PORT))

    response, addr = s.recvfrom(1024)
    print("Resposta do servidor:", json.loads(response.decode()))
