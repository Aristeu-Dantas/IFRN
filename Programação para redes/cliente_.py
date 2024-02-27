import socket, threading
from constantes import *
    
def servInteraction():

    # mensagem com espaço para entrar no loop enquanto a mensagem não for vazia
    msg = b' '
    while msg != b'':
        try:
            # recebendo dados do servidor
            msg = sockClient.recv(BUFFER_MSG)
            # exibindo a mensagem
            print ("\n"+msg.decode(CODE_PAGE)+"\n")
        except Exception as e:
            print(f'ERROR em servInteraction: {e}')
            msg = b''
    closeSocket()

def userInteraction():
    msg = ''
    while msg != '/q':
        try:
            # se msg diferente que comando de saída, envie a mensagem para o servidor
            msg = input(PROMPT)
            if msg != '': sockClient.send(msg.encode(CODE_PAGE))

        except Exception as e:
            print(f'ERROR em userInteraction: {e}')
            msg = '/q'
    closeSocket()

def closeSocket():
    try:
        sockClient.close()
        print('fechando conexão...')
    except Exception as e: 
        print('ERROR in closeSocket:', e)

try:
    sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockClient.connect((IP_CLIENTE, PORT_CLIENT))
    
    # Obtém o tipo de comunicação, Se UDP ou TCP
    if sockClient.type == 1:
        print(f'\nTipo de conexão TCP!\n')
    else: 
        print(f'\nTipo de conexão UDP!\n')

    print ("Conectado a: ", (IP_CLIENTE, PORT_CLIENT))
    tServer = threading.Thread(target=servInteraction)
    tUser = threading.Thread(target=userInteraction)

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()
# Se error no client, finalize o socket e exiba o error
except Exception as e:
    print ("Falha ", e)

