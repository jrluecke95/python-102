# row = ["--", "--", "--"]

# width = 3
# height = 3

# for i in range(height):
#     row[1] = "X"
#     print(row)

space = ["--"]

width = 3
height = 3

row1 =[]
row2 =[]
row3 =[]
board = [row1, row2, row3]

for i in range(width):
    for j in range(height):
        row1.append(space)
        
print(board)
