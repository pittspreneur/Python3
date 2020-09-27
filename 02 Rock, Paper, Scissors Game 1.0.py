import random

'''This is a classic game of Rock, Paper, Scissors'''

comp_wins = 0#..................................................variable for computer's wins
player_wins = 0#................................................variable for player's wins

def choose_option():#...........................................fcn defined to collect yser option
    user_choice = input("Choose Rock, Paper, or Scissors: ")#...user's input
    if user_choice in ["Rock", "rock", "R", "r"]:#..............if statement for rock
        user_choice = "r"#......................................defines rock as user choice
    elif user_choice in ["Paper", "paper", "P", "p"]:#..........else if statement for paper
        user_choice = "p"#......................................defines paper as user choice
    elif user_choice in ["Scissors", "scissors", "S", "s"]:#....else if statement for scissors
        user_choice = "s"#......................................defines scissors as user choice
    else:#......................................................final else statement
        print("Wrong choice. (Rock, Paper, or Scissors)")#......error message
        chose_option()#.........................................embeds choose_option fcn
    return user_choice#.........................................pulls out the user coice input

def computer_option():#.........................................fcn defined to randomize comp_choice
    comp_choice = random.randint(1,3)#..........................makes comp_choice random between 1-3
    if comp_choice == 1:#.......................................if statement that defines 1
        comp_choice = "r"#......................................1 = r payload
    elif comp_choice == 2:#.....................................else if that defines 2
        comp_choice = "p"#......................................2 = p payload
    else:#......................................................else that defines 3
        comp_choice = "s"#......................................3 = s payload
    return comp_choice



while True:
    print("")
    user_choice = choose_option()
    comp_choice = computer_option()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("You choose rock. The computer choose rock. Tie game.")
        elif comp_choice == "p":
            print("You chose rock. The computer choose paper. You lost :(")
            comp_wins += 1
        elif comp_choice == "s":
            print("You chose rock. The computer choose scissors. You won!")
            player_wins += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print("You choose paper. The computer choose rock. You won!")
            player_wins += 1
        elif comp_choice == "p":
            print("You chose paper. The computer choose paper. Tie game.")
        elif comp_choice == "s":
            print("You chose paper. The computer choose scissors. You lost :(")
            comp_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print("You choose scissors. The computer choose rock. You lost :(")
            comp_wins += 1
        elif comp_choice == "p":
            print("You chose scissors. The computer choose paper. You won!")
            player_wins += 1
        elif comp_choice == "s":
            print("You chose scissors. The computer choose scissors. Tie game.")

    print("")
    print("Player Wins: " + str(player_wins))
    print("Computer Wins: " + str(comp_wins))
    print("")

    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break
    
    
        
                       
    
            

















            
            
    
