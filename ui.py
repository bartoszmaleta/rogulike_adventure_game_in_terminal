import helpers as helpers
import graphics as graphics
import os
import time
import operator
import engine as engine
from collections import OrderedDict




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
            elif element == "^":
                print('\033[0;32;42m{}'.format(element), end="")
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
# \033[0;32;42m    -------------->  green background
# 
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
    print(asciiart, info)
    print()
    # print_introduction_screen(info)
    print()
    input("[Enter anything to go back]: ")

def show_assassin_info():
    asciiart = graphics.get_assassin_asciiart()
    info ='''
    Assassin is a silent killer, he has an ability to sneak and to kill enemy out of hiding. He usually wears
    light clothes, which are blending with the surroundings and a carries a dagger as his weapon. '''
    print("")
    print_character_info(asciiart, info)

def show_warrior_info():
    asciiart = graphics.get_warrior_asciiart()
    info = '''
    Warrior is a strong, solid character, centered around strenght and physical health. He is known for his
    powerful attacks. Warrior often wears heavy armor alongside swords. '''
    print("")
    print_character_info(asciiart, info)

def show_wizard_info():
    asciiart = graphics.get_wizard_asciiart()
    info = '''
    Wizard is a complex character, his greatest power is his wisdom. He has an ability to spell casts and drink potions
    Wizards usually wear long robes and have magic wands as a weapon. '''
    print("")
    print_character_info(asciiart, info)

def print_introduction_screen(text, speed=0.05):
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
        show_wizard_info()
        class_selection_screen()
    elif choice == "3":
        return "3"
    elif choice == "4":
        show_warrior_info()
        class_selection_screen()
    elif choice == "5":
        return "5"
    elif choice == "6":
        show_assassin_info()
        class_selection_screen()
    else:
        class_selection_screen()

# print_introduction_screen(graphics.introduction_screen())  # to main

# Initial commit
# Initial commit


def print_how_to_show_inventory():
    inventory_ascii = graphics.inventory_ascii()
    print(inventory_ascii)

def print_inventory_and_wait(player_inv):
    os.system("clear")
    print_table(player_inv)
    input("ENTER to go back")

def add_to_string(string, to_add):
    return string + to_add + "\n"

def print_table(player_inv, count=None):
    longest_left = len("item") + 2
    longest_right = len("count") + 3

    if count == "count,desc":
        player_inv = OrderedDict(player_inv)

    for key in player_inv:
        value = player_inv[key]
        item_name_length = len(key)
        item_count_length = len(str(value))
        if item_name_length > longest_left:
            longest_left = item_name_length + 2
        if item_count_length > longest_right:
            longest_right = item_count_length + 3
    
    main_middle_length = longest_left + longest_right + 2
    
    separator_main = "=" * main_middle_length
    separator_top = "/" + separator_main + "\\"
    separator_mid = "|" + separator_main + "|"
    separator_bot = "\\" + separator_main.replace("=","-") + "/"

    table_string = ""
    table_string = add_to_string(table_string, separator_top)
    table_string = add_to_string(table_string, "|" + "˜”*°• INVENTORY •°*”˜".center(main_middle_length) + "|")
    table_string = add_to_string(table_string, separator_mid)
    table_string = add_to_string(table_string, "|" + "ITEM".center(longest_left) + "||" + "COUNT".center(longest_right) + "|")
    table_string = add_to_string(table_string, separator_mid)
    for key in player_inv:
        value = player_inv[key]
        table_string = add_to_string(table_string, "|" + key.center(longest_left) + "||" + str(value).center(longest_right) + "|")
    table_string = add_to_string(table_string, separator_bot)

    for sign in table_string:
        if sign == "=":
            print('\033[1;31m{}'.format(sign), end="")
            print('\033[0;37;49m', end="")
        elif sign == "|":
            print('\033[1;31m{}'.format(sign), end="")
            print('\033[0;37;49m', end="")
        elif sign == "-":
            print('\033[1;31m{}'.format(sign), end="")
            print('\033[0;37;49m', end="")
        elif sign == "/":
            print('\033[1;31m{}'.format(sign), end="")
            print('\033[0;37;49m', end="")
        elif sign == "\\":
            print('\033[1;31m{}'.format(sign), end="")
            print('\033[0;37;49m', end="")
        elif sign == "•":
            print('\033[0;35m{}'.format(sign), end="")
            print('\033[0;37;49m', end="")
        elif sign == "*":
            print('\033[0;35m{}'.format(sign), end="")
            print('\033[0;37;49m', end="")
        elif sign == "°":
            print('\033[0;35m{}'.format(sign), end="")
            print('\033[0;37;49m', end="")
        elif sign == "˜":
            print('\033[0;35m{}'.format(sign), end="")
            print('\033[0;37;49m', end="")
        elif sign == "”":
            print('\033[0;35m{}'.format(sign), end="")
            print('\033[0;37;49m', end="")
        elif sign.isalpha():
            print('\033[0;34m{}'.format(sign), end="")
            print('\033[0;37;49m', end="")
        elif sign.isdigit():
            print('\033[0;32m{}'.format(sign), end="")
            print('\033[0;37;49m', end="")
        elif sign == "\n":
            print()
        else:
            print(sign, end="")



def blank_line():
    print()


# Initial commit


def print_text(plain_string):
    print(plain_string)


def print_score_of_player(score_of_player):       # NEW, NOT USED
    # player_score = player["score"]
    # print('SCORE: ', player_score)
    print('SCORE: ', score_of_player)


def display_choosing_characters(board):
    helpers.clear_screen()
    for row in board:
        print(''.join(row)) 
        
def display_wizard(board):
    # helpers.clear_screen()

    for row in board:
        print(''.join(row))


def display_warrior(board):
    # helpers.clear_screen()

    for row in board:
        print(''.join(row))


def display_assasin(board):
    # helpers.clear_screen()

    for row in board:
        print(''.join(row))


def display_alien_boss(board):
    # helpers.clear_screen()

    for row in board:
        print(''.join(row))


# ---------------------- Character and bosses --------------------------------
def display_wizard_and_alien_boss(board):
    # helpers.clear_screen()

    for row in board:
        print(''.join(row))


def display_warrior_and_alien_boss(board):
    # helpers.clear_screen()

    for row in board:
        print(''.join(row))


def display_assassin_and_alien_boss(board):
    # helpers.clear_screen()

    for row in board:
        print(''.join(row))


def display_fight(character_type):
    FILE_PATH_OF_ASSASSIN_AND_ALIEN_BOSS = "assassin_and_alien_boss.txt"
    FILE_PATH_OF_WIZARD_AND_ALIEN_BOSS = "wizard_and_alien_boss.txt"
    FILE_PATH_OF_WARRIOR_AND_ALIEN_BOSS = "warrior_and_alien_boss.txt"

    # wizard_and_alien_boss_board = engine.create_board_out_of_file(FILE_PATH_OF_WIZARD_AND_ALIEN_BOSS)

    # warrior_and_alien_boss_board = engine.create_board_out_of_file(FILE_PATH_OF_WARRIOR_AND_ALIEN_BOSS)

    # assassin_and_alien_boss_board = engine.create_board_out_of_file(FILE_PATH_OF_ASSASSIN_AND_ALIEN_BOSS)

    if character_type == "wizard":
        
        fight_graphic = engine.create_board_out_of_file(FILE_PATH_OF_WIZARD_AND_ALIEN_BOSS)
        for row in fight_graphic:
            print(''.join(row))   
    elif character_type == "warrior":
        fight_graphic = engine.create_board_out_of_file(FILE_PATH_OF_WARRIOR_AND_ALIEN_BOSS)
        for row in fight_graphic:
            print(''.join(row))  
    elif character_type == "assassin":
        fight_graphic = engine.create_board_out_of_file(FILE_PATH_OF_ASSASSIN_AND_ALIEN_BOSS)
        for row in fight_graphic:
            print(''.join(row))          


def display_heath(health_of_player):
    print('HEALTH: ', health_of_player)


def put_emoji_on_board(board):
    board[19][13] = "\U0001F333"
    board[19][14] = "\U0001F333"
    board[19][15] = "\U0001F333"
    board[19][16] = "\U0001F333"
    board[19][17] = "\U0001F333"
    board[19][18] = "\U0001F333"
    board[19][19] = "\U0001F333"
    board[19][20] = "\U0001F333"
    board[19][21] = "\U0001F333"
    board[19][22] = "\U0001F333"
    board[19][23] = "\U0001F333"
    board[19][24] = "\U0001F333"
    board[19][25] = "\U0001F333"
    board[19][26] = "\U0001F333"
    board[19][27] = "\U0001F333"
    board[19][28] = "\U0001F333"
    board[19][29] = "\U0001F333"
    board[19][30] = "\U0001F333"
    board[19][31] = "\U0001F333"
    board[19][32] = "\U0001F333"
    board[19][33] = "\U0001F333"
    board[19][34] = "\U0001F333"
    board[19][35] = "\U0001F333"
    board[19][36] = "\U0001F333"
    board[19][37] = "\U0001F333"
    board[19][38] = "\U0001F333" 
    board[2][60] = "\U0001F319"
    board[8][16] = "\U0001F4A5"
    board[17][7] = "\U0001F4A5"
    board[9][49] = "\U0001F4A5"
    board[10][54] = "\U0001F4A5"
    board[17][62] = "\U0001F4A5"
    board[7][82] = "\U0001F4A5"