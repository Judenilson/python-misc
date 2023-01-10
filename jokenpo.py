import os
import random

jokenpo = ["", "Pedra", "Papel", "Tesoura"]


def result(placar, player, cpu, r):
    os.system("cls")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("           Você jogou:", jokenpo[player])
    print("           O PC jogou:", jokenpo[cpu])
    if r == 0:
        print()
        print("             Jogo Empatado!")
    elif r == -1:
        placar[0] += 1
        print()
        print("              Você Perdeu!")
    else:
        placar[1] += 11
        print()
        print("          !!! Você Ganhou !!!")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


def instructions():
    os.system("cls")
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("                !! JOKENPO !!")
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("Escolha um número de acordo com sua opção desejada.")
    print("     1 - Pedra   |   2 - Papel   |   3 - Tesoura")
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::")

def inNumber():
    i = input("Digite sua opção aqui-> ")
    integer = ord(i[0])-48
    return integer 


def game(placar):
    player = inNumber()
    cpu = random.randint(1, 3)

    if (player < 1 or player > 3):
        while True:
            print("Escolha um valor possível!")
            player = inNumber()
            if (player > 0 and player < 4):
                break            

    if player == 1:
        if cpu == 1:
            result(placar, player, cpu, 0)
        elif cpu == 2:
            result(placar, player, cpu, -1)
        else:
            result(placar, player, cpu, 1)
    elif player == 2:
        if cpu == 2:
            result(placar, player, cpu, 0)
        elif cpu == 3:
            result(placar, player, cpu, -1)
        else:
            result(placar, player, cpu, 1)
    else:
        if cpu == 3:
            result(placar, player, cpu, 0)
        elif cpu == 1:
            result(placar, player, cpu, -1)
        else:
            result(placar, player, cpu, 1)


def main():
    placar = [0, 0]
    instructions()
    while 1:
        game(placar)
        print("Deseja jogar novamente?")
        playAgain = input("Para SIM igite 'S' -> ").lower()
        if playAgain != 's':
            break

    os.system("cls")    
    print("-----------------------------------")
    print("O jogo terminou com o resultado de:") 
    print(placar[1], "Pontos para o Jogador e ")
    print(placar[0], "Pontos para a CPU")
    print("-----------------------------------")
    print("    Obrigado por jogar Jokenpo!")
    print("            Até logo...")
    print("-----------------------------------")


main()
