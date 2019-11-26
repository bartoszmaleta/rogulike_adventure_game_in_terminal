def create_board(width, height):
    '''
    Creates game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board  
    '''
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

    return board


def put_player_on_board(board, player):
    '''
    Puts the player icon on the board on player coordinates.

    Args:
    list: The game board
    dictionary: The player information - the icon and coordinates

    Returns:
    list: The game board with the player sign on it
    '''
    player_icon = player["icon"]
    player_x = player["x"]
    player_y = player["y"]

    board[player_y][player_x] = player_icon

    return board


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


# TEST VERSION
# def create_board_out_of_file(file_name):
#     myFile = open(file_name, "r+")
#     myLines = list(myFile)
#     myFile.close()
#     # print(len(myLines))
#     # print(myLines)
    
#     board2 = []
#     one_line_list = []
#     counter = 0
#     for line in myLines:
#         for character in line:
#             one_line_list.append(character)

#         counter += 1
#         board2.append(line)
#     board = []
#     board.append(board2)
