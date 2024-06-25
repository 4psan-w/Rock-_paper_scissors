import random as r
# import string 

def Ai_side():
    
    C_game=["Rock","Paper","Scissor"]
    rfromlist=r.choice(C_game)
    return rfromlist    


def game_back():
    print("Enter your Action: ")
    uinp=input(">>")
    cinp=Ai_side()
    
    if((uinp.capitalize())=='Rock'):
        
        if(cinp=='Paper'):
            print(cinp)
            print("You Lost!!")
        elif(cinp=='Scissor'):
            print(cinp)
            print("You won!!")
        elif(cinp=='Rock'):
            print(cinp)
            print("It was A Draw")
            print("Press Y to Try again ")
            udes=input(">>>")
            if(udes.capitalize()=='Y'):
                game_back()

    elif(uinp.capitalize()=='Paper'):
        if(cinp=='Rock'):
            print(cinp)
            print("You Won!!")
        
        elif(cinp=='Paper'):
            print(cinp)
            print("It was A Draw")
            print("Press Y to Try again ")
            udes=input(">>>")
            if(udes.capitalize()=='Y'):
                game_back()
        
        elif(cinp=='Scissor'):
            print(cinp)
            print("You Lost!!")

    elif(uinp.capitalize()=='Scissor'):
        if(cinp=='Rock'):
            print(cinp)
            print("You Lost!!")
        elif(cinp=='Paper'):
            print(cinp)
            print("You Won!!")
        elif(cinp=='Scissor'):
            print("It was A Draw")
            print("Press Y to Try again ")
            udes=input(">>>")
            if(udes.capitalize()=='Y'):
                game_back()


def main_game():
    header="ROCK PAPER Scissor GAME"
    print(header.center(65))
    print("Description:")
    print("Traditional Rock paper Scissor game as a console game\n")
    game_back()

main_game()#Excecutes the main function which controls the other funcitons of the program!!