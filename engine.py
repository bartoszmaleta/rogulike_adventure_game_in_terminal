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

    # for row_index in range(height):
    #     row = []        
        
    #     if row_index == 0 or row_index == (height - 1):
    #         for i in range(20):
    #             row.append("X")
    #     else:
    #         row.append("X")
    #         for row_index in range(width - 2):
    #             row.append(".")
    #         row.append("X")
    #     board.append(row)
    
    #     return board
    
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


# def change_position(pos_x, pos_y, board, player):
#     print(player["x"])
#     player_icon = player["icon"]
#     player_x = player["x"]
#     player_y = player["y"]
    
#     player_y = player_y - pos_y

#     # player["x"] = player["x"] - pos_y
    
#     return player