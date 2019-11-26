import helpers as helpers
from graphics import *

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
            print(element, end="")
        print()



def print_introduction_screen(text, title=""):
    display_text = ""
    for letter in text:
        display_text += letter
        sleep(0.05)
        system("clear")
        print(display_text)


print_introduction_screen(introduction_screen())