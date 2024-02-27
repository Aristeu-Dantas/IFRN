import socket, threading

# Dicionário para armazenar conexões de clientes e seus respectivos nomes
clients = {}

def main(cliente_socket, nome_cliente):
    global clients
    while True:
        try:
            message = cliente_socket.recv(1024).decode('utf-8')

            #nome do cliente
            if message.startswith('!u'):
                _, name = message.split(' ', 1)
                clients[cliente_socket] = name.strip()
            elif message == '!l': #listar os clientes conectados
                cliente_socket.send(str(clients.values()).encode('utf-8'))
            elif message.startswith('!m'): #enviar mensagem a um usuário específico
                _, recipient, msg = message.split(' ', 2)
                recipient = recipient.strip()
                msg = msg.strip()

                for socket, name in clients.items():
                    if name == recipient:
                        socket.send(f"{nome_cliente}: {msg}".encode('utf-8'))

            else:
                #Repassa a mensagem para todos os clientes
                broadcast(f"{nome_cliente}: {message}", cliente_socket)

        except ConnectionResetError:
            #desconexões inesperadas
            del clients[cliente_socket]
            broadcast(f"{nome_cliente} saiu do chat.", cliente_socket)
            break

def broadcast(message, sender_socket):
    for cliente_socket in clients.keys():
        if cliente_socket != sender_socket:
            try:
                cliente_socket.send(message.encode('utf-8'))
            except:
                #desconexões inesperadas
                del clients[cliente_socket]

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen(5)
    print("Servidor escutando na porta 12345")

    while True:
        cliente_socket, addr = server.accept()
        print(f"Conexão recebida de {addr}")

        #implantando as threads
        nome_cliente = f"Cliente-{len(clients)+1}"
        clients[cliente_socket] = nome_cliente
        cliente_socket.send(f"Você está conectado como {nome_cliente}".encode('utf-8'))
        threading.Thread(target=main, args=(cliente_socket, nome_cliente)).start()

if __name__ == "__main__":
    start_server()
