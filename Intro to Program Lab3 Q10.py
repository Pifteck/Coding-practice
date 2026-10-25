black_king = chr(9812)
black_queen = chr(9813)
black_rook = chr(9814)
black_bishop = chr(9815)
black_knight = chr(9816)
black_pawn = chr(9817)
black_pieces = [black_king,black_queen,black_rook,black_bishop,black_knight,black_pawn]

white_king = chr(9818)
white_queen = chr(9819)
white_rook = chr(9820)
white_bishop = chr(9821)
white_knight = chr(9822)
white_pawn = chr(9823)
white_pieces = [white_king,white_queen,white_rook,white_bishop,white_knight,white_pawn]

#print(white_pieces)
#print(black_pieces)

board = [
    [black_rook, black_knight, black_bishop, black_queen, black_king, black_bishop, black_knight, black_rook],
    [black_pawn] * 8,
    [" "] * 8,
    [" "] * 8,
    [" "] * 8,
    [" "] * 8,
    [white_pawn] * 8,
    [white_rook, white_knight, white_bishop, white_queen, white_king, white_bishop, white_knight, white_rook]
]
# Function to print the board neatly in the terminal
def print_board(b):
    for row_idx, row in enumerate(b):
        rank = 8 - row_idx  # Chess ranks go from 8 down to 1
        print(f"{rank}| " + " ".join(row))
    print(" +----------------")
    print("   a b c d e f g h")
print_board(board)