import helpers as helpers
import graphics as graphics
import os
import time


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
            else:
                print('\033[0;37;49m{}'.format(element), end="")
        print()
# \033[0;34m    -------------->  blue
# \033[0;34;44m -------------->  blue + background blue
# \033[0;33m    -------------->  yellow, almost brown
# \033[0;35m    -------------->  magenta
# \033[0;32m    -------------->  green
# \033[1;31m    -------------->  red
# \033[1;31m    -------------->  red
# \033[1;31;41m -------------->  red + background red
# \033[1;30m    -------------->  black font
# \033[0;40m    -------------->  black background
# \033[0;42m    -------------->  green background
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

def print_character_info(asciiart, info):
    print(asciiart)
    print()
    print_introduction_screen(info)
    print()
    input("[Enter anything to go back]: ")

def show_assassin_info():
    asciiart = graphics.get_assassin_asciiart()
    info = "jakis asciiart\njakis info o assassin tutaj"
    print_character_info(asciiart, info)

def show_warrior_info():
    asciiart = graphics.get_warrior_asciiart()
    info = "jakis asciiart\njakis info o warrior tutaj"
    print_character_info(asciiart, info)

def show_wizard_info():
    asciiart = graphics.get_wizard_asciiart()
    info = "jakis asciiart\njakis info o wizard tutaj"
    print_character_info(asciiart, info)

def print_introduction_screen(text, title="", speed=0.05):
    display_text = ""
    for letter in text:
        display_text += letter
        time.sleep(speed)
        os.system("clear")
        print(display_text)
    
def class_selection_screen():
    os.system("clear")
    print(graphics.character_creation_screen())
    choice = input("What's your choice?: ")

    if choice == "1":
        return "1"
    elif choice == "2":
        return "2"
    elif choice == "3":
        return "3"
    elif choice == "4":
        show_wizard_info()
        class_selection_screen()
    elif choice == "5":
        show_warrior_info()
        class_selection_screen()
    elif choice == "6":
        show_assassin_info()
        class_selection_screen()
    else:
        class_selection_screen()
