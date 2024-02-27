message = 'jon: /m ana ola ana'
message[2:].split()[0]

print(message)
_, parametro, recipient, *msg = message.split(' ')
print(_)
print(parametro)
print(recipient)
print(msg)
print(message)
