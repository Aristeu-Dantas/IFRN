import socket, threading

def receive_messages(cliente, nome_cliente):
    while True:
        try:
            message = cliente.recv(1024).decode('utf-8')
            print(message)
        except ConnectionResetError:
            # Envie uma mensagem para o servidor informando que o cliente está se desconectando
            cliente.send(f"!s {nome_cliente}".encode('utf-8'))
            print(f"{nome_cliente} saiu")
            break

    # Envia uma mensagem via broadcast informando que o cliente entrou
    cliente.send(f"!i {nome_cliente}".encode('utf-8'))

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('127.0.0.1', 12345))

    # Nome do cliente
    name = input("Digite seu nome: ")
    print(f'{name} Conectado!')

    # Implanta as threads
    threading.Thread(target=receive_messages, args=(cliente, name)).start()

    while True:
        message = input()
        # Nome do cliente para identificá-lo
        cliente.send(f"{name}: {message}".encode('utf-8'))

if __name__ == "__main__":
    main()
