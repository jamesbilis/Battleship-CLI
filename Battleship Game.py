import numpy as np
import random


# Function to check hits or misses
def check_hit_or_miss(board, x, y, ships_remaining):
    if board[y, x] == 'S':
        board[y, x] = 'X'
        ships_remaining -= 1
        if ships_remaining == 1:
            return f"HIT! ONLY {ships_remaining} SHIP LEFT!", ships_remaining
        elif ships_remaining > 1:
            return f"HIT! ONLY {ships_remaining} SHIPS LEFT!", ships_remaining
        else:
            return f"HIT! {ships_remaining} SHIPS LEFT!", ships_remaining
    elif board[y, x] == '.':
        board[y, x] = 'O'
        return "MISS", ships_remaining
    return "ALREADY GUESSED", ships_remaining


# Function to check if game is over
def is_game_over(board):
    return 'S' not in board


# Function to print the board based on difficulty
def print_board(board, reveal_ships):
    print("   ", end="")
    for col_num in range(10):
        print(f"{col_num} ", end="")
    print()
    for row in range(10):
        print(f"{row}  ", end="")
        for col in range(10):
            cell = board[row, col]
            if cell == 'S' and not reveal_ships:
                print(". ", end="")
            else:
                print(f"{cell} ", end="")
        print()


# Main game function
def main():
    print("\nWelcome to Battleship! Good luck and have fun!")

    # Ask for difficulty mode
    while True:
        difficulty = input("Choose your difficulty (Easy or Hard): ").strip().lower()
        if difficulty in ["easy", "hard"]:
            reveal_ships = difficulty == "easy"
            break
        else:
            print("Invalid option. Please type 'Easy' or 'Hard'.")

    # Create the board and place ships
    board = np.full((10, 10), '.')
    ships_remaining = 5
    placed = 0
    while placed < ships_remaining:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if board[y, x] == '.':
            board[y, x] = 'S'
            placed += 1

    # Show board before first guess
    print("\nHere's the board before your first guess:")
    print_board(board, reveal_ships)

    # Game loop
    while not is_game_over(board):
        try:
            x_guess = int(input("Please guess the column (0–9): "))
            y_guess = int(input("Please guess the row (0–9): "))
        except ValueError:
            print("Invalid response. Please enter numbers only.")
            continue

        if not (0 <= x_guess < 10) or not (0 <= y_guess < 10):
            print("Out of bounds. Please try again.")
            continue

        result, ships_remaining = check_hit_or_miss(board, x_guess, y_guess, ships_remaining)
        print(result)
        print_board(board, reveal_ships)

    # Game Over message
    print("\nFinal Board:")
    print_board(board, True)  # Always reveal final board


# Function to handle multiple attempts
def run_again():
    try_again = input("Game Over! Would you like to try again? Please type Yes or No: ")
    if try_again.lower() == "yes":
        main()
        run_again()
    elif try_again.lower() == "no":
        print("Alright, see you next time!")
    else:
        wrong_response()


# Function for invalid response
def wrong_response():
    print("Invalid response. Please try again.")
    run_again()


# Start the game
main()
run_again()
