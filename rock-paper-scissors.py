import random  # Import the 'random' module to generate computer choices.

# Define a function to get the user's choice.
def get_user_choice():
    """
    Get the user's choice of Rock, Paper, or Scissors.
    """
    while True:  # Use a while loop to ensure a valid choice.
        user_choice = input("Enter your choice (Rock, Paper, Scissors): ").strip().capitalize()  # Get user input and capitalize it.
        if user_choice in ["Rock", "Paper", "Scissors"]:  # Check if the input is valid.
            return user_choice  # Return the valid choice.
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")  # Display an error message for invalid input.

# Define a function to generate the computer's choice.
def get_computer_choice():
    """
    Generate a random choice for the computer (Rock, Paper, or Scissors).
    """
    return random.choice(["Rock", "Paper", "Scissors"])  # Use 'random.choice' to pick a random choice for the computer.

# Define a function to determine the winner of the game and display the result.
def determine_winner(user_choice, computer_choice):
    """
    Determine the winner of the game and display the result.
    """
    print(f"You chose {user_choice}.")  # Print the user's choice.
    print(f"The computer chose {computer_choice}.")  # Print the computer's choice.

    if user_choice == computer_choice:  # Check for a tie.
        print("It's a tie!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Scissors" and computer_choice == "Paper")
        or (user_choice == "Paper" and computer_choice == "Rock")
    ):
        print("You win!")
    else:
        print("Computer wins!")

# Define the main function to play the game.
def play_game():
    """
    Main function to play the game.
    """
    print("Welcome to Rock, Paper, Scissors!")

    while True:  # Use a while loop to allow multiple rounds.
        user_choice = get_user_choice()  # Get the user's choice.
        computer_choice = get_computer_choice()  # Generate the computer's choice.
        determine_winner(user_choice, computer_choice)  # Determine and display the winner.

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()  # Ask if the user wants to play again.
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break  # Exit the game if the user doesn't want to play again.

# Check if the script is being run as the main program.
if __name__ == "__main__":
    play_game()  # Call the main function to start the game.

# This code starts the game by calling the 'play_game()' function when the script is run.
