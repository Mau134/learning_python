import random

def play_game():
    user_wins = 0
    computer_wins = 0

    while True:
        user_choice = input("Enter 'rock', 'paper', 'scissors', or 'done' to quit: ").lower()
        
        if user_choice == 'done':
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please enter 'rock', 'paper', 'scissors', or 'done'.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chooses {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

    print(f"User wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")

if __name__ == "__main__":
    play_game()
