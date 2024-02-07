import random

#function roll() for generating randaom values between 1 to 6
def roll():  
    minvalue = 1
    maxvalue = 6
    roll = random.randint(minvalue,maxvalue)
    return roll

#asking user to enter number of players 
#which is between 2 - 4 players
#also checking condtions for valid input 

while True:
    players = input("enter the number of players between (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if (players >= 2) and (players <=4):
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, Try again.")

     
max_score = 50  # maximum score for player to win the game
player_score = [0 for i in range(players) ] #storing players score in list using list comprehencen

while max(player_score) < max_score:    # while players score is below maximum score 

    for player_idx in range(players):     
        print("player number",player_idx + 1,"turn has just started\n")
        print("your total score is:",player_score[player_idx],"\n")


        current_score =0

        while True:            #while true asking player to roll the dice and if he type y game continues
            should_roll = input("would you like to roll (y)? ")
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value == 1:    # if value is 1 den set the players current score to 0 and vreak the loop
                print("you rolled a 1! turn done!")
                current_score =0
                break
            else:             # else add the values of dice to players current score 
                current_score += value
                print("you rolled a: ",value)

            print("your current score is: ",current_score)

        player_score[player_idx] += current_score     # storing player score
        print("your total score is: ",player_score[player_idx])

max_score = max(player_score)    # 
winning_idx = player_score.index(max_score) # player with score of 50 and more at the end of last roll will be the winner
print("player number",winning_idx+1,
      "is the winner with a score of: ",max_score)
        





