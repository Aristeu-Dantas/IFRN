# --------- CONSTANTES -----------------


PORT_CLIENT  = 5678
PORT_SERVER  = 5678
IP_CLIENTE   = 'localhost'
IP_SERVER    = '0.0.0.0'
PROMPT       = 'Digite sua msg (/q para terminar) > '
CODE_PAGE    = 'utf-8'
BUFFER_MSG   = 1024
COMAND_LIST  = ['/q','/l','/m','/b','/h','/f','/d','/u','/w','/rss','/?']
COMAND_ERROR = '\n\
---------------------------------------------------------------------------------------------------------- \n\
\t\tCOMANDOS DISPONÍVEIS:\t\
\n---------------------------------------------------------------------------------------------------------- \n \
/q → sair do cliente;\n \
/l → listar o IP:porta dos clientes conectados no servidor;\n \
/m:ip_destino:porta:mensagem → Enviar uma mensagem a um determinado cliente conectado no servidor\n \
/b:mensagem → Enviar uma mensagem para todos os clientes conectados no servidor\n \
/h → listar as mensagens já enviadas ao servidor pelo usuário (histórico);\n \
/f → listar os arquivos (nome e tamanho) contidos na pasta /server_files (do servidor);\n \
/d:nome_arquivo → efetuar o “download” do arquivo especificado para a pasta /download (do cliente);\n \
/u:nome_arquivo →efetuar o “upload” de um arquivo para a pasta /server_files (do servidor);\n \
/w:url →efetuar o download do arquivo fornecido na url para a pasta /server_files (do servidor);\n \
/rss:palavra_chave →listar as 10 notícias mais recentes que contenham a palavra_chave. Deverá ser habilitado pelo menos 10 URLs que forneçam conteúdo em formato RSS;\n \
/? → exibir uma ajuda (listar as opções contidas nesse roteiro).'
