def display_board(board):
    '''
    Displays complete game board on the screen


    Returns:
    Nothing 
    '''
    for row in board:
        # this one could be one line!!!!! :
        # print(''.join(row))
        for element in row:
            print(element, end="")
        print()