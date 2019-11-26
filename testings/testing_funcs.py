
file_name = 'map2.csv'
myFile = open(file_name, "r+")
myLines = list(myFile)
myFile.close()
print(myLines)
print(myLines[0])
print(myLines[0].rstrip())

print('-------=====================')
lists_with_lines = [] 
print(len(myLines))
for line in myLines:
    line = line.rstrip()
    lists_with_lines.append(line)
print(lists_with_lines)

strrrr = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
print(len(strrrr))

print('-------===================== HEEEERE')
boardie = []
board_large = []
for line in lists_with_lines:
    for elem in line:
        boardie.append(elem)
    board_large.append(elem)
print(boardie)
print(board_large)
print('-------===================== HEEEERE')
list_with_character_of_line = []
for row_index in range(len(lists_with_lines)):
    print(row_index)
    board = []
    for col_index in range(40):   # CHANGE 40 TO LEN(STH)
        lists_with_lines[row_index][col_index] = board[col_index]
print(board)

    # for character in line:
        # list_with_character_of_line.append(character.rstrip())

print(list_with_character_of_line)
print('-------=====================')

# ---------------------------------------------------------
txt = 'XXXXXXXX'
list_of_txt = txt.split()
print(list_of_txt)

list_of_x = []
list_of_x = ['X']
for elem in txt:
    list_of_x.append(elem)
    # list_of_x[0] += elem

print(list_of_x)
print('-------=====================')

# -------------------------
width = 40
height = 10

board = []

for row_index in range(height):
    row = []
    if row_index == 0 or row_index == height - 1:
        for i in range(width):
            row.append("X")
    else:
        row.append("X")
        for i in range(width - 2):
            row.append(".")
        row.append("X")
    board.append(row)

print(board)
print('-------=====================')

for row in board:
    # this one could be one line!!!!! :
    # print(''.join(row))
    for element in row:
        print(element, end="")
    print()