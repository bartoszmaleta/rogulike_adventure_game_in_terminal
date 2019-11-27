import helpers as helpers
import graphics as graphics
import os
import time
import operator


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


def print_introduction_screen(text, title=""):
    display_text = ""
    for letter in text:
        display_text += letter
        time.sleep(0.05)
        os.system("clear")
        print(display_text)


# print_introduction_screen(graphics.introduction_screen())

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


# Initial commit

def print_text(plain_string):
    print(plain_string)


def print_score_of_player(score_of_player):       # NEW, NOT USED
    # player_score = player["score"]
    # print('SCORE: ', player_score)
    print('SCORE: ', score_of_player)