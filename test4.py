list_of_lists_with_lines_as_string = []                                               # Create an empty list for the main array
# for line in open('map2.csv'):      # both works                                     # Open the file and read all the lines
for line_in_string in open('map_visual.txt'):                                                          # Open the file and read all the lines
    line_without_next_line = line_in_string.rstrip()                                            # Strip the \n from each line
    list_of_lists_with_lines_as_string.append(line_without_next_line.split(','))      # Split each line into a list and add it to the Multidimensional array
board = []
for row_index in range(len(list_of_lists_with_lines_as_string)):
    one_line = []
    list_with_one_line = list_of_lists_with_lines_as_string[row_index]
    INDEX_OF_FIRST_ELEMENT_OF_ITERATED_LINE = 0
    line = list_with_one_line[INDEX_OF_FIRST_ELEMENT_OF_ITERATED_LINE]
    for col_index in range(len(line)):
        one_line.append(line[col_index])
    board.append(one_line)


print('Best board in the world - board to return ')
print()
print(board)
print()
print('Best board in the world - board from file: ')
print()


for row in board:
    # ONE LINER:
    # print(''.join(row))
    # THREE LINER:
    for element in row:
        print(element, end="")
    print()


# board = create_board_out_of_file()
# print_board(board)