list_of_lists_with_lines_as_string = []                            #Create an empty list for the main array
for line in open('map2.csv'):    #Open the file and read all the lines
    line_without_next_line = line.rstrip()             #Strip the \n from each line
    list_of_lists_with_lines_as_string.append(line_without_next_line.split(','))      #Split each line into a list and add it to the
                                #Multidimensional array
print(list_of_lists_with_lines_as_string)

board = []
# list_with_character_of_line = []
for row_index in range(len(list_of_lists_with_lines_as_string)):
    print(row_index)
    one_line = []
    list_with_one_line = list_of_lists_with_lines_as_string[row_index]
    print(list_with_one_line[0])

    print('list with one line', list_with_one_line)
    print('list with one line[0]', list_with_one_line[0])
    print('list with one line[0][0]', list_with_one_line[0][0])         # list with one line[0][0] X

    line = list_with_one_line[0]    # list with one line[0] XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    print(len(line))        # = 40
    # print(line)
    # print(len(list_with_one_line[0]))
    for col_index in range(len(line)):   # CHANGE 40 TO LEN(STH)
        one_line.append(line[col_index])
    print(one_line)
    board.append(one_line)

print(board)

for row in board:
    # this one could be one line!!!!! :
    # print(''.join(row))
    for element in row:
        print(element, end="")
    print()