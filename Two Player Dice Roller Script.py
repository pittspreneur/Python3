'''
Two Player Dice Roll Script
'''


import random



def dice_roll():#Randomizer Fcn
    diceRoll = random.randint(1, 6)
    return diceRoll
    
 

#Main Function
def main_function():

    #Game Variables
    playerOne = 0
    playerTwo = 0
    playerOneWins = 0
    playerTwoWins = 0
    rounds = 1

    #Game Loop
    while rounds != 11:#Start of Round

        print("Round " + str(rounds))
        playerOne = dice_roll()
        playerTwo = dice_roll()
        print("Player One Roll: " + str(playerOne))
        print("Player Two Roll: " + str(playerTwo))


        
        if playerOne == playerTwo:#Check for Round Winner
            print("Tie Game")
        elif playerOne > playerTwo:
            playerOneWins += 1
            print("Player One Wins The Match!")
        else:
            playerTwoWins += 1
            print("Player Two Wins The Match!")

        rounds += 1
        print()
        print()

    print("Game Over!")
    print("...")
    print("...")
    print("...")
    
    if playerOneWins == playerTwoWins:#Checks for
        print("Game Over! Tie Game")
    elif playerOneWins > playerTwoWins:
        print("Player One Wins With " + str(playerOneWins) + " Wins!")
    else:
        print("Player Two Wins With " + str(playerTwoWins) + " Wins!")

        

#Action Code
main_function()




'''

@pittspreneur

'''
