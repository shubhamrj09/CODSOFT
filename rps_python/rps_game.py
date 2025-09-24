import random

def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'User'
    else:
        return 'Computer'

def display_choices(user_choice, computer_choice):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

def display_result(winner):
    if winner == 'Tie':
        print("It's a tie!")
    elif winner == 'User':
        print("You win!")
    else:
        print("You lose!")

def main():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        display_choices(user_choice, computer_choice)
        winner = determine_winner(user_choice, computer_choice)
        display_result(winner)

        # Update scores
        if winner == 'User':
            user_score += 1
        elif winner == 'Computer':
            computer_score += 1

        print(f"\nScores:\nYou: {user_score}\nComputer: {computer_score}")

        # Ask if user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Final scores:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            break

if __name__ == "__main__":
    main()