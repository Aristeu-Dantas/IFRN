import requests

data_cotacao=input('Informe a data referida a cotação no formato "mm-dd-aaaa": ')
res=requests.get(f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?%40dataCotacao='{data_cotacao}'")

print(res)