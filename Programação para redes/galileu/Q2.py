from hashlib import sha256      #da biblioteca hashlib pego somente a função sha265
from time import time
from struct import pack

def findnounce(data_To_Hash, bitsToBeZero, start_nonce=0):      #crio a função findnounce com tres parametros: data_to_hash(via pegar a frase, bitsToBezero(vai pegar o núm
    print(f"Iniciando a buca por hash de '{data_To_Hash}' que inicia com {bitsToBeZero} zeros ")
    timestart = time()  #defino o inicio do hash.
    while True:
        hashbinario = sha256()
        hashbinario.update(pack("<i", start_nonce) + data_To_Hash.encode("utf-8"))
        hashbinario = hashbinario.digest()
        hashhexa = ''.join([f'{i:02x}' for i in hashbinario])
        hashtextobinario = ''.join([f'{i:08b}' for i in hashbinario])
        if hashtextobinario.startswith("0"*bitsToBeZero): #a string começa a partir do numero que eu definio no bitsToBeZero quando encontrado o valor eu paro com o break
            break
        start_nonce += 1
    print(f"Minerar '{data_To_Hash}', bits em zero: {bitsToBeZero}, Nonce: {start_nonce}, demorou {time()-timestart:.2f} segundos.")
    print(f"hash:{hashhexa}\n{'-'*40}")

findnounce("Esse é fácil", 8)
findnounce("Esse é fácil", 10)
findnounce("Esse é fácil", 15)
findnounce("Texto maior muda o tempo?", 8)
findnounce("Texto maior muda o tempo?", 10)
findnounce("Texto maior muda o tempo?", 15)
findnounce("É possivel calcular esse?", 18)
findnounce("É possivel calcular esse?", 19)
findnounce("É possivel calcular esse?", 20)
