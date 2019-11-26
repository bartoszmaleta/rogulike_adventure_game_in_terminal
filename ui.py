import helpers as helpers


def display_board(board):
    '''
    Displays complete game board on the screen


    Returns:
    Nothing 
    '''
    helpers.clear_screen()
        
    for row in board:
        # this one could be one line!!!!! :
        # print(''.join(row))
        for element in row:
            if element == "$":
                print('\033[1;32;49m{}'.format(element), end="")
            else:
                print('\033[0;37;49m{}'.format(element), end="")
        print()


# -------------------------------------------------
# TESTING COLOURS

# welcome_text = '\033[1;33;49m Welcome in the HANGMAN!'
# welcome_text_alignment = welcome_text.center(100)
# copyrights_text = '\033[1;32;49m Michał Z., Bartosz M., Przemysław B.'
# copyrights_alignment = copyrights_text.center(100)
# print(welcome_text_alignment)
# print(copyrights_alignment)
# print('\033[0;37;49m \n')

# print('\033[1;32;49m asasdas' + '\033[0;37;49m qweqweqweqwe')
# # print('\033[1;32;49m asasdas' + '\033[0;37;49mqweqweqweqwe') without space
# print()