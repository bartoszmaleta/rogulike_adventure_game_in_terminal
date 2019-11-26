def display_board(board):
    '''
    Displays complete game board on the screen


    Returns:
    Nothing
    '''
    # helpers.clear_screen()

    for row in board:
        # this one could be one line!!!!! :
        # print(''.join(row))
        for element in row:
            if element == "$":
                print('\033[1;32;49m{}'.format(element), end="")
            elif element == "O":
                print('\033[0;34;44m{}'.format(element), end="")
            elif element == "o":
                print('\033[0;34;44m{}'.format(element), end="")
            elif element == "=":
                print('\033[0;33;49m{}'.format(element), end="")
            elif element == "|":
                print('\033[0;35;49m{}'.format(element), end="")
            elif element == ".":
                print('\033[0;32;49m{}'.format(element), end="")
            elif element == "X":
                print('\033[1;31;41m{}'.format(element), end="")
                # print('\033[1;31;49m{}'.format(element), end="")
                print('\033[0;37;49m', end="")
            elif element == "-":
                print('\033[1;30;40m{}'.format(element), end="")
                print('\033[0;37;49m', end="")
            elif element == "*":
                print('\033[1;30;40m{}'.format(element), end="")
                print('\033[0;37;49m', end="")
            elif element == "^":
                print('\033[0;32;42m{}'.format(element), end="")
                print('\033[0;37;49m', end="")
            else:
                print('\033[0;37;49m{}'.format(element), end="")
        print()


def create_board_out_of_file(file_name):
    # file_name = 'map.txt'
    list_of_lists_with_lines_as_string = []                                               # Create an empty list for the main array
    # for line in open('map2.csv'):      # both works                                     # Open the file and read all the lines
    for line_in_string in open(file_name):                                                # Open the file and read all the lines
        line_without_next_line = line_in_string.rstrip()                                  # Strip the \n from each line
        list_of_lists_with_lines_as_string.append(line_without_next_line.split(','))      # Split each line into a list and add it to the Multidimensional array

    board = []
    for row_index in range(len(list_of_lists_with_lines_as_string)):
        one_row_line = []
        list_with_one_line = list_of_lists_with_lines_as_string[row_index]

        INDEX_OF_FIRST_ELEMENT_OF_ITERATED_LINE = 0

        line = list_with_one_line[INDEX_OF_FIRST_ELEMENT_OF_ITERATED_LINE]
        for col_index in range(len(line)):
            one_row_line.append(line[col_index])
        board.append(one_row_line)

    return board


labirynth = "labirynth.txt"

labirynth_map = create_board_out_of_file(labirynth)
display_board(labirynth_map)