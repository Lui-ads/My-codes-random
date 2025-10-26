# Jumanji

import time
import os
import random

# Posições dos jogadores
pos_jogador1 = 0
pos_jogador2 = 0
pos_jogador3 = 0
pos_jogador4 = 0

dado1 = [1, 2, 3, 4, 5, 6]
dado2 = [1, 2, 3, 4, 5, 6]

jogador1 = ''
jogador2 = ''
jogador3 = ''
jogador4 = ''

time.sleep(0.9)
os.system('clear')
print('\nJumanji')
time.sleep(0.9)
os.system('clear')

print('\nNo mínimo 2 e no máximo 4')

quantos_jogadores = int(input('\nQuantos jogadores serão: '))
while quantos_jogadores < 2 or quantos_jogadores > 4:
    print('\nNúmero inválido! O jogo só permite de 2 a 4 jogadores.')
    quantos_jogadores = int(input('\nQuantos jogadores serão: '))

personagens = ['Elefante', 'Rinoceronte', 'Jacaré', 'Primata']
for i in range(quantos_jogadores):
    os.system('clear')
    print('\nJumanji')
    time.sleep(0.9)
    os.system('clear')
    time.sleep(0.9)
    print('\nQuem você quer ser:\n')
    print(', '.join(personagens))  # Mostra só os nomes, separados por vírgula
    escolha = input('\n')
    while escolha not in personagens:
        print('Escolha inválida. Tente novamente.')
        escolha = input('\n')
    if jogador1 == '':
        jogador1 = escolha
    elif jogador2 == '':
        jogador2 = escolha
    elif jogador3 == '':
        jogador3 = escolha
    else:
        jogador4 = escolha
    personagens.remove(escolha)

os.system('clear')
print('\nJumanji')
time.sleep(0.9)
os.system('clear')
time.sleep(0.9)

# O jogo tem 30 casas no total
conts = 0
lista_desafio = ['Que bom, você andou, e agora a sua nova casa chegou']

while pos_jogador1 < 30 and pos_jogador2 < 30 and pos_jogador3 < 30 and pos_jogador4 < 30:
    if quantos_jogadores == 4:
        for i in range(1, 5):
            if i == 1:
                nome = jogador1
            elif i == 2:
                nome = jogador2
            elif i == 3:
                nome = jogador3
            else:
                nome = jogador4
            print(f'\n{nome}, jogue os dados!')
            input('\nDê enter para jogar os dados: ')
            time.sleep(1)
            dados1 = random.choice(dado1)
            dados2 = random.choice(dado2)
            casas = dados1 + dados2
            print(f'\nVocê tirou {dados1} e {dados2}, isso dá {casas}!\n')
            print(random.choice(lista_desafio))
            if i == 1:
                pos_jogador1 += casas
                if pos_jogador1 >= 30:
                    break
            elif i == 2:
                pos_jogador2 += casas
                if pos_jogador2 >= 30:
                    break
            elif i == 3:
                pos_jogador3 += casas
                if pos_jogador3 >= 30:
                    break
            else:
                pos_jogador4 += casas
                if pos_jogador4 >= 30:
                    break
            input('\nDê enter para continuar: ')
            os.system('clear')
            print('\nJumanji')
            time.sleep(0.9)
            os.system('clear')
            time.sleep(0.9)
        if pos_jogador1 >= 30 or pos_jogador2 >= 30 or pos_jogador3 >= 30 or pos_jogador4 >= 30:
            break
    elif quantos_jogadores == 3:
        for i in range(1, 4):
            if i == 1:
                nome = jogador1
            elif i == 2:
                nome = jogador2
            else:
                nome = jogador3
            print(f'\n{nome}, jogue os dados!')
            input('\nDê enter para jogar os dados: ')
            time.sleep(1)
            dados1 = random.choice(dado1)
            dados2 = random.choice(dado2)
            casas = dados1 + dados2
            print(f'\nVocê tirou {dados1} e {dados2}, isso dá {casas}!\n')
            print(random.choice(lista_desafio))
            if i == 1:
                pos_jogador1 += casas
                if pos_jogador1 >= 30:
                    break
            elif i == 2:
                pos_jogador2 += casas
                if pos_jogador2 >= 30:
                    break
            else:
                pos_jogador3 += casas
                if pos_jogador3 >= 30:
                    break
            input('\nDê enter para continuar: ')
            os.system('clear')
            print('\nJumanji')
            time.sleep(0.9)
            os.system('clear')
            time.sleep(0.9)
        if pos_jogador1 >= 30 or pos_jogador2 >= 30 or pos_jogador3 >= 30:
            break
    else:
        for i in range(1, 3):
            if i == 1:
                nome = jogador1
            else:
                nome = jogador2
            print(f'\n{nome}, jogue os dados!')
            input('\nDê enter para jogar os dados: ')
            time.sleep(1)
            dados1 = random.choice(dado1)
            dados2 = random.choice(dado2)
            casas = dados1 + dados2
            print(f'\nVocê tirou {dados1} e {dados2}, isso dá {casas}!\n')
            print(random.choice(lista_desafio))
            if i == 1:
                pos_jogador1 += casas
                if pos_jogador1 >= 30:
                    break
            else:
                pos_jogador2 += casas
                if pos_jogador2 >= 30:
                    break
            input('\nDê enter para continuar: ')
            os.system('clear')
            print('\nJumanji')
            time.sleep(0.9)
            os.system('clear')
            time.sleep(0.9)
        if pos_jogador1 >= 30 or pos_jogador2 >= 30:
            break

os.system('clear')
print('\nJumanji')
time.sleep(0.9)
os.system('clear')
time.sleep(0.9)

if pos_jogador1 >= 30:
    print(f'\nParabéns {jogador1}! Você ganhou!')
elif pos_jogador2 >= 30:
    print(f'\nParabéns {jogador2}! Você ganhou!')
elif pos_jogador3 >= 30 and quantos_jogadores >= 3:
    print(f'\nParabéns {jogador3}! Você ganhou!')
elif pos_jogador4 >= 30 and quantos_jogadores == 4:
    print(f'\nParabéns {jogador4}! Você ganhou!')
else:
    print('Erro')
input('\nFim de jogo: ')
os.system('clear')
time.sleep(1)