# Faça um programa que implementa o jogo "Pedra-Papel-Tesoura" entre o usuário e o computador.
# O programa pede a opção do usuário e a opção do computador é escolhida aleatoriamente.
# O jogo continua até que o usuário escolha sair. Ao sair, o programa imprime o resultado final das partidas.
import random
lista = ['pedra', 'papel', 'tesoura']
usuario = input('Pedra, Papel ou Tesoura: ').lower().strip()
pc = random.choice(lista)
print(f'O pc escolheu {pc}.')
count=0
rep = 's'
while rep == 's':
    count+=1
    if usuario == pc:
        print('Empate!')
        rep = input('Deseja continuar?(s/n) ')
        
    if (usuario == 'pedra' and pc == 'papel') or (usuario == 'papel' and pc == 'tesoura') or (usuario == 'tesoura' and pc == 'pedra'):
        print('O computador venceu!')
        rep = input('Deseja continuar?(s/n) ')
        
    if (usuario == 'papel' and pc == 'pedra') or (usuario == 'tesoura' and pc == 'papel') or (usuario == 'pedra' and pc == 'tesoura'):
        print('O usuario venceu!')
        rep = input('Deseja continuar?(s/n) ')        
else:
    print('Jogo encerrado.')
    #print(f'Partidas {count}\nPlacar {cont_usuario} usuário x {cont_pc} pc.')