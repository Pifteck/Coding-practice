import random

board = [" "] * 9

print("Player is [O] and computer is [X]")

while True:
    # Display the board
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

    # Player's move
    move = input("# Make your move ! [1-9] : ")

    if not move.isdigit() or int(move) < 1 or int(move) > 9:
        print(">> Invalid number ! Try again !")
        continue

    move = int(move) - 1

    if board[move] != " ":
        print(">> Position taken ! Try again !")
        continue

    board[move] = "O"

    # Check if player wins
    if (board[0] == board[1] == board[2] == "O" or
        board[3] == board[4] == board[5] == "O" or
        board[6] == board[7] == board[8] == "O" or
        board[0] == board[3] == board[6] == "O" or
        board[1] == board[4] == board[7] == "O" or
        board[2] == board[5] == board[8] == "O" or
        board[0] == board[4] == board[8] == "O" or
        board[2] == board[4] == board[6] == "O"):

        print("*** Congratulations ! You won ! ***")
        break

    if " " not in board:
        print("*** It's a draw ! ***")
        break

    # Computer's random move
    while True:
        computer = random.randint(1, 9)

        if board[computer - 1] == " ":
            board[computer - 1] = "X"
            break

    # Check if computer wins
    if (board[0] == board[1] == board[2] == "X" or
        board[3] == board[4] == board[5] == "X" or
        board[6] == board[7] == board[8] == "X" or
        board[0] == board[3] == board[6] == "X" or
        board[1] == board[4] == board[7] == "X" or
        board[2] == board[5] == board[8] == "X" or
        board[0] == board[4] == board[8] == "X" or
        board[2] == board[4] == board[6] == "X"):

        print("*** Computer wins ! ***")
        break

    if " " not in board:
        print("*** It's a draw ! ***")
        break
