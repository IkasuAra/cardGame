import os
import time

print("Insira o nome dos Players")
nomePlayer1 = input("Player 1: ")
nomePlayer2 = input("Player 2: ")
nomePlayer3 = input("Player 3: ")
nomePlayer4 = input("Player 4: ")


def distribuiCartas(deck, cartasPlayer1, cartasPlayer2, cartasPlayer3, cartasPlayer4):
    while(deck > 0):
        if(cartasPlayer1 == 0):
            cartasPlayer1 += 1
            deck -= 1
        elif(cartasPlayer1 > cartasPlayer2):
            if(cartasPlayer2 == cartasPlayer3 == cartasPlayer4):
                cartasPlayer2 += 1
                deck -= 1
        elif(cartasPlayer2 > cartasPlayer3):
            if(cartasPlayer1 == cartasPlayer2 and cartasPlayer3 == cartasPlayer4):
                cartasPlayer3 += 1
                deck -= 1
        elif(cartasPlayer3 > cartasPlayer4):
            if(cartasPlayer1 == cartasPlayer2 == cartasPlayer3):
                cartasPlayer4 += 1
                deck -= 1
        elif(cartasPlayer4 == cartasPlayer1):
            cartasPlayer1 += 1
            deck -= 1
        exibePartida(deck, cartasPlayer1, cartasPlayer2,
                     cartasPlayer3, cartasPlayer4)
    quit()


def exibePartida(deck=48, cartasPlayer1=0, cartasPlayer2=0, cartasPlayer3=0, cartasPlayer4=0):
    while(deck >= 0):
        print(end='\n')
        print("Deck", deck)
        if(deck == 48):
            time.sleep(0.9)
        print(nomePlayer1, end=": ")
        print(cartasPlayer1)
        print(nomePlayer2, end=": ")
        print(cartasPlayer2)
        print(nomePlayer3, end=": ")
        print(cartasPlayer3)
        print(nomePlayer4, end=": ")
        print(cartasPlayer4)
        time.sleep(0.5)
        if(deck == 0):
            time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        distribuiCartas(deck, cartasPlayer1, cartasPlayer2,
                        cartasPlayer3, cartasPlayer4)


def main():
    exibePartida()
    return 0


main()
