import random

def get_player_choice():
    """Gets a valid player choice (Rock, Paper, Scissors)"""
    while True:
        choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid input. Please try again.")

def determine_winner(player1_choice, player2_choice):
    """Determines the winner based on game rules"""
    if player1_choice == player2_choice:
        return None  # It's a tie
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
         (player1_choice == "scissors" and player2_choice == "paper") or \
         (player1_choice == "paper" and player2_choice == "rock"):
         return 1  # Player 1 wins
    else:
         return 2  # Player 2 wins

def get_computer_choice():
    """Generates a random choice for the computer"""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def play_round():
    """Plays a single round of Rock-Paper-Scissors"""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    print(f"Computer chose {computer_choice}")  # Show the computer's choice

    winner = determine_winner(player_choice, computer_choice)

    if winner is None:
        print("It's a tie!")
    elif winner == 1:  # Player wins
        print("You win!")
    else:  # Computer wins
        print("Computer wins!")

def main():
    """Main game loop"""
    while True:
        play_round()
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()