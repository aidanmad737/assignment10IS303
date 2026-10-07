import random

#Determining player choice function
def get_player_choice():
    choice = input("Enter rock, paper, scissors: ").lower()
    while choice != "rock" and choice != "paper" and choice != "scissors":
        print(f"Sorry, {choice} is not a valid choice. Please try again.")
        choice = input("Enter rock, paper, scissors: ").lower()
    return choice

#Determining winner function
def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif player == "rock" and computer == "scissors":
        return "win"
    elif player == "paper" and computer == "rock":
        return "win"
    elif player == "scissors" and computer == "paper":
        return "win"
    else:
        return "loss"

#Rounds played function
def play_rounds(rounds):
    player_score = 0
    computer_score = 0
    rounds_played = 0

    while rounds_played < rounds:
        player_choice = get_player_choice()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"The computer chose {computer_choice}.")

        result = determine_winner(player_choice, computer_choice)
        if result == "win":
            print("You won!")
            player_score += 1
            rounds_played += 1
        elif result == "loss":
            print("You lost!")
            computer_score += 1
            rounds_played += 1
        else:
            print("Tie! Play again.")

    return player_score, computer_score

#Round number selection and game start
print("Welcome to Rock Paper Scissors!")
rounds = int(input("How many rounds would you like to play: "))
while rounds % 2 == 0 or rounds <= 0:
    rounds = int(input("Sorry, the number must be an odd number. Please try again: "))
#This is a tuple, bc it returns two values,
#player_score and computer_score which are to be used
#in the following code
player_score, computer_score = play_rounds(rounds)

#End of game results

print(f"Score — You: {player_score} | Computer: {computer_score}")
if player_score > computer_score:
    print("You win!")
else:
    print("The computer wins!")
print("Thanks for playing!")
