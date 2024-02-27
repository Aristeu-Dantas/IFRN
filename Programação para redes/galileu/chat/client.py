import socket, threading

def receive_messages(cliente_socket):
    while True:
        try:
            message = cliente_socket.recv(1024).decode('utf-8')
            print(message)
        except ConnectionResetError:
            print("Conexão com o servidor perdida.")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))

    #nome do cliente
    name = input("Digite seu nome: ")
    print(f'{name} Entrou!')
    client.send(f"!u {name}".encode('utf-8'))

    #implanta as threads
    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        message = input()
        #nome do cliente para identifica-lo
        client.send(f"{name}: {message}".encode('utf-8'))


if __name__ == "__main__":
    main()
