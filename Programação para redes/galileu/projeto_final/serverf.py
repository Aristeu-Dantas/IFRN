import socket, threading, requests
# https://api.telegram.org/bot6415104444:AAE18Xce8ydzgIMNJXOTxNhHDFIOmFEkkzs/getUpdates
TOKEN = '6415104444:AAE18Xce8ydzgIMNJXOTxNhHDFIOmFEkkzs'
clients = {}
clientsTelegram = {}

def send_message(text, chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id':chat_id, 'text':text}
    response = requests.post(url, data=data)
    response = response.json()
    if response['ok']:
        print('Mensagem enviada com sucesso!')
    else:
        if response['error']['message'] == 'chat_id is empty':
            print('Erro ao enviar mensagem: chat ID está vazio.')
        else:
            print('Erro ao enviar mensagem:', response['error']['message'])


def get_message(from_id_message):
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    data = {'offset':from_id_message}
    response = requests.get(url)
    response_json = response.json()



# def get_chat_id(cliente_socket):
#     global last_msg

#     # Atualiza o último ID de atualização recebido
#     last_msg += 1

#     # Obtém o pacote JSON da API do Telegram
#     response_json = get_message(last_msg)

#     # Obtém o chat ID do cliente
#     chat_id = response_json['result'][0]['message']['chat']['id']

#     return chat_id


def broadcast(message, sender_socket, clientsTelegram, chat_id, usertype):
    if usertype in clients.keys():
        for cliente_socket in clients.keys():
            if cliente_socket != sender_socket:
                try:
                    cliente_socket.send(message.encode('utf-8'))

                except:
                    #desconexões inesperadas
                    del clients[cliente_socket]
    else:
        for usertype in clientsTelegram.keys():
            if chat_id != chat_id:
                    try:
                        get_message(f'{first_name}: {text}', chat_id)

                    except:
                        #desconexões inesperadas
                        del clientsTelegram[cliente_socket]

def convertationTerminal(cliente_socket, nome_cliente):
    global clients
    broadcast(f'{nome_cliente} entrou!', cliente_socket)
    while True:
        try:
            message = cliente_socket.recv(1024).decode('utf-8')

            if message.startswith('/m'): #enviar mensagem a um usuário específico
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

def convertationTelegram ():
    chat_id = None
    # get_message()
    # update_id = 447914693
    last_msg = 0

    while True:
        recebendo_mensagens = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
        # enviando_mensagens = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

        response_json = get_message(last_msg+1)

        for update in response_json['result']:  #processa a atualização recebida
            chat_id = update['message']['chat']['id']  #atualiza o chat_id
            text = update['message']['text']
            last_msg = update['update_id']
            first_name = ['message']['first_name']




def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen(5)
    print("Servidor escutando na porta 12345")

    chat_id = None
    nome_cliente={}
    threading.Thread(target=convertationTelegram, args=(clientsTelegram, nome_cliente)).start()

    while True:
        cliente_socket, addr = server.accept()
        print(f"Conexão recebida de {addr}")

        #implantando as threads
        nome_cliente = f"Cliente-{len(clients)+1}"
        clients[cliente_socket] = nome_cliente
        cliente_socket.send(f"Você está conectado como {nome_cliente}".encode('utf-8'))
        threading.Thread(target=convertationTerminal, args=(cliente_socket, nome_cliente)).start()
        print(clients)
        print(nome_cliente)

if __name__ == "__main__":
    start_server()
