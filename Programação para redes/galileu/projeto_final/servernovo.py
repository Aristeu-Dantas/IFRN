import socket, threading, requests

# https://api.telegram.org/bot6415104444:AAE18Xce8ydzgIMNJXOTxNhHDFIOmFEkkzs/getUpdates
TOKEN = '6415104444:AAE18Xce8ydzgIMNJXOTxNhHDFIOmFEkkzs'
SERVER = '0.0.0.0'
PORT = 5678

def cliInteraction(sockConn, addr):
    msg = b''
    name = sockConn.recv(512)
    allSocks[name] = sockConn
    # allSocks.append((sockConn, addr))
    while msg != b'!q':
        try:
            msg = sockConn.recv(512)
            broadCast(msg, name)
        except:
            msg = b'!q'
    sockConn.close()
    del allSocks[sockConn]

def broadCast(msg, name):
    msg = f"{name.decode('utf-8')} -> {msg.decode('utf-8')}"
    print(msg)
    for n in allSocks.keys():
        if n != name:
            allSocks[n].send(msg)

def unicast (name, msg):
    if msg.startswith('/m'):
        
        recipient = name[sockConn]
        msg = f"{recipient.decode('utf-8')} -> {msg.decode('utf-8')}"


def get_message(from_id_message):
    try:
        url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
        data = {'offset': from_id_message}
        response = requests.get(url, data=data)
        response_json = response.json()
        return response_json
    except Exception as e:
        print(f"Erro ao obter mensagens do Telegram: {e}")
        return None

def send_message(text, chat_id):
        url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
        data = {'chat_id':chat_id, 'text':text}
        response = requests.post(url, data=data)
        response = response.json()

def convertationTelegram(clientsTelegram, allSocks):
    # chat_id = None
    last_msg = 0

    while True:
        response_json = get_message(last_msg + 1)
        l = len(response_json['result'])

        if response_json:
            for i in range(l):
                update = response_json['result'][i]
                chat_id = update['message']['chat']['id']
                text = update['message']['text']
                first_name = update['message']['chat']['first_name']
                text = (f'{first_name}: {text}')
                last_msg = update['update_id']
                if chat_id not in clientsTelegram:
                    clientsTelegram[chat_id] = {'name': first_name}

                for chatid in clientsTelegram:
                    numeracao = chatid
                    if numeracao != chat_id:
                        send_message(text, numeracao)
                        print(text)


try:
    allSocks = {}
    clientsTelegram = {}
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SERVER, PORT))

    print("Listening in: ", (SERVER, PORT))
    sock.listen(5)

    threading.Thread(target=convertationTelegram, args=(clientsTelegram, allSocks)).start()
    while True:
        sockConn, addr = sock.accept()
        print("Connection from: ", addr)
        # name = sockConn.recv(512)
        # allSocks[name] = {'name': name}
        # allSocks.append((sockConn, addr))
        tClient = threading.Thread(target=cliInteraction, args=(sockConn, addr))
        tClient.start()
except Exception as e:
    print("Fail: ", e)
