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


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print('Error! WARNING! WTF? '.format(message))


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print()
    print(title)
    for index, element in enumerate(list_options):
        print('    ({}) {}'.format(index + 1, element))
    print('    (0) {}'.format(exit_message))


def return_headline_for_menu_title_(head):
    head_centered = head.center(60)
    headlne2 = '\033[1;34;49m {} \033[0;37;49m'.format(head_centered)
    blank_line()
    return headlne2


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>
    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    print()
    print(title)
    inputs = []
    for label in list_labels:
        print(label)
        user_input = input()
        inputs.append(user_input)
    return inputs


def print_enumerate_table(table):
    for i, item in enumerate(table, 1):
        print('{}. {}'.format(i, item))


def find_longest_width(table, title_list):
    width_list = []
    for title in title_list:
        width_list.append(len(title))
    for line in table:
        for num, col in enumerate(line):
            if len(str(col)) > width_list[num]:
                width_list[num] = len(str(col))
    return width_list


def copy_table(table):
    copied_table = []
    copied_line = []
    ID_POSITION = 0
    
    for index, record in enumerate(table):
        copied_line = record[:]
        copied_line[ID_POSITION] = str(index+1)
        copied_table.append(copied_line)
    return copied_table


def sum_list_of_nums(list_to_sum):
    count = 0
    for num in list_to_sum:
        count += num
    
    return count


def print_table_beauty(table, title_list):
    """
    Prints table with data.
    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/
    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers
    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    table_copy = copy_table(table) 
    width_list = find_longest_width(table_copy, title_list)
    top = '-' * (sum_list_of_nums(width_list)+len(width_list)*2+len(width_list)+1-2)
    spacer = top + 2 * '-' 
    print(f'/{top}\\')
    print('|', end='')
    for num, title in enumerate(title_list):
        print(f"{title.center(width_list[num]+2)}|", end='')
    print()
    print(spacer)
    for record in table_copy:
        print('|', end='')
        for col in range(len(record)):
            print(f"{str(record[col]).center(width_list[col]+2)}|", end='')
        if table_copy.index(record) == len(table_copy)-1:
            print()
            print(f'\\{top}/')
        else:
            print()
            print(spacer)  