import socket
import threading
import requests
import json

# Configurações do Telegram
TELEGRAM_TOKEN = '6415104444:AAE18Xce8ydzgIMNJXOTxNhHDFIOmFEkkzs'
TELEGRAM_CHAT_ID = 'SEU_CHAT_ID_DO_TELEGRAM'

# Dicionário para armazenar os clientes terminais
clients = {}

# Função para enviar mensagens para clientes terminais
def send_terminal_message(message, sender_socket):
    for terminal_socket in clients.keys():
        if terminal_socket != sender_socket:
            try:
                terminal_socket.send(message.encode('utf-8'))
            except:
                # desconexões inesperadas
                del clients[terminal_socket]

def process_telegram_message(message, sender_chat_id):
    # Converte o objeto JSON em um dicionário
    message_dict = json.loads(message)

    # Verifica se a mensagem é uma mensagem de entrada
    if message_dict['message_type'] == 'message':
        # Verifica se o remetente é um usuário conhecido
        if sender_chat_id in clients:
            # Envia a mensagem para todos os clientes terminais
            send_terminal_message(message_dict['text'], None)

# Função principal para tratar clientes terminais
def handle_terminal(client_socket, client_address):
    name = f"Cliente-{client_address}"
    clients[client_socket] = name

    # Aqui você pode enviar mensagens de boas-vindas ou fazer outras coisas necessárias
    client_socket.send(f"Bem-vindo, {name}!".encode('utf-8'))

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')

            # Se a mensagem começa com '!m', é uma mensagem para outro cliente
            if message.startswith('!m'):
                _, recipient, msg = message.split(' ', 2)
                recipient = recipient.strip()
                msg = msg.strip()

                # Envia a mensagem para o destinatário
                if recipient in clients:
                    clients[recipient].send(f"{name}: {msg}".encode('utf-8'))
                else:
                    # O destinatário não está conectado
                    client_socket.send(f"Usuário '{recipient}' não encontrado.".encode('utf-8'))
            else:
                # Envia a mensagem para todos os clientes terminais
                send_terminal_message(message, client_socket)

        except ConnectionResetError:
            # Desconexão inesperada
            del clients[client_socket]
            send_terminal_message(f"{name} saiu do chat.", None)
            break

# Função para tratar mensagens do Telegram
def handle_telegram():
    last_update_id = 0

    while True:
        try:
            updates = requests.get(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates?offset={last_update_id}').json()

            for update in updates.get('result', []):
                chat_id = update['message']['chat']['id']
                text = update['message']['text']

                # Processa a mensagem
                process_telegram_message(text, chat_id)

                # Atualiza o ID da última mensagem processada
                last_update_id = update['update_id'] + 1

        except Exception as e:
            print(f"Erro ao obter atualizações do Telegram: {e}")

# Função principal para iniciar o servidor
def start_server():
    # Inicia a thread para lidar com mensagens do Telegram
    threading.Thread(target=handle_telegram, daemon=True).start()

    # Configura o servidor para clientes terminais
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen(5)
    print("Servidor escutando na porta 12345")


