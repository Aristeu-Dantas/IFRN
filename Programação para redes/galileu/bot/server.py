import requests, socket
# https://api.telegram.org/bot6415104444:AAE18Xce8ydzgIMNJXOTxNhHDFIOmFEkkzs/getUpdates
TOKEN = '6415104444:AAE18Xce8ydzgIMNJXOTxNhHDFIOmFEkkzs'

def send_message(text, chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id':chat_id, 'text':text}
    response = requests.post(url, data=data)
    response = response.json()
    if response['ok']:
        print('Mensagem enviada com sucesso!')
    else:
        print('Erro ao enviar mensagem:')
        print(response['description'])

def get_message(from_id_message):
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    data = {'offset':from_id_message}
    response = requests.post(url, data=data)
    response_json = response.json()
    return response_json

def info(chat_id):
    #pega ip
    ip = socket.gethostbyname(socket.gethostname())
    send_message(f'IP:{ip}',chat_id)
    # pega a máscara
    for family, _, _, _, sockaddr in socket.getaddrinfo(ip, None):
        netmask = sockaddr[1]
        break
    send_message(f'Máscara de rede:{netmask}',chat_id)
    send_message('Gateway não implementado', chat_id)

def ping():
    send_message('Não implementado.', chat_id)

def active_ip(ip):
    #verifica se o ip está respondendo
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Define um timeout de 1 segundo
            s.connect((ip, 80))  # Tenta conectar na porta 80
            send_message(f"O IP {ip} está respondendo.", chat_id)
    except socket.error as e:
        send_message(f"O IP {ip} não está respondendo: {e}", chat_id)

def service():
    send_message('Não implementado.', chat_id)

def download():
    send_message('Não implementado.', chat_id)

def scan():
    send_message('Não implementado.', chat_id)

if __name__=='__main__':
    chat_id = None
    # get_message()
    # update_id = 447914693
    last_msg = 0

    while True:
        response_json = get_message(last_msg+1)

        for update in response_json['result']:  #processa a atualização recebida
            chat_id = update['message']['chat']['id']  #atualiza o chat_id
            text = update['message']['text']
            # print(update)
            last_msg = update['update_id']
            # print(last_msg)
            # text = input('Digite uma mensagem: ')
            if text.startswith('/'):
                if text == '/info':
                    info(chat_id)
                elif text == '/ping':
                    ping()
                elif text == '/active ip':
                    send_message("Digite o IP que deseja verificar: ", chat_id)
                    response_json = get_message()
                    ip = response_json['result'][0]['message']['text']
                    active_ip(ip)
                elif text == '/service':
                    service()
                elif text == '/download url_image':
                    download()
                elif text == '/scan host':
                    scan()
            else:
                send_message('Nada haver.', chat_id)
