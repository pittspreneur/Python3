'''This program functions acts as a dice roller game'''


import random#.....................................X_X


def main():#.......................................main program fcn
     player1 = 0#..................................player1 input as an integer
     player1wins = 0
     player2 = 0#..................................player2 input as
     player2wins = 0
     rounds = 1#...................................X_X

     while rounds != 4:#...........................while function that displays Round Count
         print("Round " + str(rounds))#............displays Current number of rounds
         player1 = dice_roll()#....................runs primary dice roll fcn with player1
         player2 = dice_roll()#....................runs primary dice roll fcn with player2
         print("Player 1 Roll: " + str(player1))#..prints player1's roll
         print("Player 2 Roll: " + str(player2))#..prints player2's roll 
         
         if player1 == player2:#...................if statement that decides is match a draw
             print("It's a Draw!")#................if statement payload
         elif player1 > player2:#..................else if statement that decides player 1 greater than
             player1wins = player1wins + 1#........adds wins
             print("Player 1 Wins the Match!")#....else if payload
         else:#....................................all if and elif's end with a final else statement
             player2wins = player2wins + 1 #.......adds wins 
             print("Player 2 Wins the Match!")#....else's payload
        
         rounds = rounds + 1#......................round counter
         print()#..................................creates space
         
     if player1wins == player2wins:#...............if statment that decides the draw
          print("Game Over! Its a Draw!")#.........if statement payload
     elif player1wins > player2wins:#..............else if statement that decides if player1wins is greater
          print("Game Over! Player 1 Wins The Game - " + str(player1wins) + " Wins!")#else if payload
     else:#........................................else statement that decides if player2wins is greater
          print("Game Over! Player 2 Wins The Game - " + str(player2wins) + " Wins!")#else statement payload



def dice_roll():#..................................primary Dice Roll Function
    diceRoll = random.randint(1, 6)#...............random.randint creates a random integer|(1, 6)
    return diceRoll#...............................returns the randon.randint(1, 6) as the 'diceRoll' variable

main()#............................................execution of main fcn



#CREATE GUI


