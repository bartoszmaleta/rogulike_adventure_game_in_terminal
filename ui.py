import helpers as helpers
import graphics as graphics
import os
import time
import operator
import engine as engine


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
    Warrior is a strong, solid character, centered around strenght and physical health. On the beginning of the game, 
    warrior has more lifes than the others. Warrior often wears heavy armor alongside swords. '''
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


def print_table(player_inv, order=None):
    space = ' '
    vertical_line = '|'
    dash = '-'
    longest_string_in_inv = max(len(longest_string) for longest_string in player_inv)  # =9

    number_of_dashes = longest_string_in_inv + 3 + len('count')
    dashes = dash * number_of_dashes  # =17
    
    # if order is issubclass(int, str):
    #     print('asqwe')

    # if order is not None:
    #     print('Choose order. You can choose between ascending and descending.')
    #     print("To display ascending table write: 'print_table(inv, 'count,asc')")
    #     print("To display descending table write: 'print_table(inv, 'count,desc')")
    #     print('\n Your inventory: \n')

    if order is None:
        print('You does not enter order. You can choose between ascending and descending.')
        print("To display ascending table write: 'print_table(inv, 'count,asc')")
        print("To display descending table write: 'print_table(inv, 'count,desc')")
        print('Right now the table will be printed without order!')
        # inv = order
        # asc_sorted_inv = sorted(inv.items(), key=operator.itemgetter(-1))
        print(dashes)
        print("{:<10} {:<15}".format('item_name |', 'count'))
        print(dashes)
        for keys, values in player_inv.items():
            # count = values
            
            number_of_whitespaces_before_item_name = longest_string_in_inv - len(keys)
            whitespaces_before_item_name = ' ' * number_of_whitespaces_before_item_name
            keys_with_spaces_and_line = whitespaces_before_item_name + keys + space + vertical_line
            
            values_str = str(values)
            length_of_count = len('count')
            number_of_whitespaces_before_count = length_of_count - len(values_str)
            whitespaces_before_count = ' ' * number_of_whitespaces_before_count
            count_with_spaces = whitespaces_before_count + values_str

            print("{:<0} {:<15}".format(keys_with_spaces_and_line, count_with_spaces))
        
        print(dashes)
        print()
        # display_total_number_of_inventory()  
        
    if order == 'count,desc':
        desc_sorted_inv = order
        desc_sorted_inv = sorted(player_inv.items(), key=operator.itemgetter(-1), reverse=True)
        print(dashes)
        print("{:<10} {:<15}".format('item_name |', 'count'))
        print(dashes)
        for keys, values in desc_sorted_inv:
            # count = values
            
            number_of_whitespaces_before_item_name = longest_string_in_inv - len(keys)
            whitespaces_before_item_name = ' ' * number_of_whitespaces_before_item_name
            keys_with_spaces_and_line = whitespaces_before_item_name + keys + space + vertical_line
            
            values_str = str(values)
            length_of_count = len('count')
            number_of_whitespaces_before_count = length_of_count - len(values_str)
            whitespaces_before_count = ' ' * number_of_whitespaces_before_count
            count_with_spaces = whitespaces_before_count + values_str

            print("{:<0} {:<15}".format(keys_with_spaces_and_line, count_with_spaces))
        
        print(dashes)
        print()
        # display_total_number_of_inventory()
    
    elif order == 'count,asc':
        asc_sorted_inv = order
        asc_sorted_inv = sorted(player_inv.items(), key=operator.itemgetter(-1))
        print(dashes)
        print("{:<10} {:<15}".format('item_name |', 'count'))
        print(dashes)
        for keys, values in asc_sorted_inv:
            # count = values
            
            number_of_whitespaces_before_item_name = longest_string_in_inv - len(keys)
            whitespaces_before_item_name = ' ' * number_of_whitespaces_before_item_name
            keys_with_spaces_and_line = whitespaces_before_item_name + keys + space + vertical_line
            
            values_str = str(values)
            length_of_count = len('count')
            number_of_whitespaces_before_count = length_of_count - len(values_str)
            whitespaces_before_count = ' ' * number_of_whitespaces_before_count
            count_with_spaces = whitespaces_before_count + values_str

            print("{:<0} {:<15}".format(keys_with_spaces_and_line, count_with_spaces))
        
        print(dashes)
        print()


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
