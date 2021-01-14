size = 3
board = []

# prints raw lists that we need for board
for y in range(size):
    board.append([])
    for x in range(size):
        board[y].append("[%d][%d]" % (y, x))

# formats the board
for row in board:
    for column in row:
        print("%s " % column, end="")
    print("\n")

print("\n\nPlayer X is moving. \n\n")

