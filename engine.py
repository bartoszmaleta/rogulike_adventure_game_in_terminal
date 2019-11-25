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
    myFile = open(file_name, "r+")
    myLines = list(myFile)
    myFile.close()
    # print(len(myLines))
    # print(myLines)
    
    board2 = []
    one_line_list = []
    counter = 0
    for line in myLines:
        for character in line:
            one_line_list.append(character)

        counter += 1
        board2.append(line)
    board = []
    board.append(board2)