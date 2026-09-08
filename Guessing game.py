import random

def high_low_game() -> None:
    """
    High-Low Guessing Game 🎯
    
    The computer randomly selects a number between 1 and 100.
    The user tries to guess the number.
    
    Features:
    - Informs the user if the guess is too high or too low.
    - Rejects non-integer inputs and numbers outside 1–100.
    - Counts valid and invalid guesses.
    - Displays statistics (valid, invalid, total guesses) when the game ends.
    
    Returns:
        None
    """
    
    print("Welcome to the High-Low Guessing Game!")
    print("I'm thinking of a number between 1 and 100\n")

    secret_number: int = random.randint(1, 100)
    valid_guesses: int = 0
    invalid_guesses: int = 0

    while True:
        user_input: str = input("Enter your guess: ")

        # التحقق من أن الإدخال رقم صحيح
        try:
            guess: int = int(user_input)
        except ValueError:
            print("Invalid: Please enter a whole number.")
            invalid_guesses += 1
            continue

        # التحقق أن الرقم بين 1 و 100
        if guess < 1 or guess > 100:
            print("Invalid: Number must be between 1 and 100.")
            invalid_guesses += 1
            continue

        valid_guesses += 1

        # مقارنة التخمين مع الرقم السري
        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"Correct! The number was {secret_number}")
            break

    print(f"\nGame Over!")
    print(f"Valid guesses: {valid_guesses}")
    print(f"Invalid guesses: {invalid_guesses}")
    print(f"Total guesses: {valid_guesses + invalid_guesses}")

if __name__ == "__main__":
    high_low_game()