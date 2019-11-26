import operator

PLAYER_ICON = '@'
PLAYER_START_X = 4
PLAYER_START_Y = 9
PLAYER_INV = {'rope': 0, 'torch': 0, 'gold coin': 0, 'dagger': 0, 'arrow': 0, 'bow': 0}  

# BOARD_WIDTH = 80
# BOARD_HEIGHT = 30

BOARD_WIDTH = 40
BOARD_HEIGHT = 10


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {}
    player["x"] = PLAYER_START_X
    player["y"] = PLAYER_START_Y
    player["icon"] = PLAYER_ICON
    player["inventory"] = PLAYER_INV
    return player


def print_table(inventory, order=None):
    space = ' '
    vertical_line = '|'
    dash = '-'
    longest_string_in_inv = max(len(longest_string) for longest_string in player_inv)  # =9

    number_of_dashes = longest_string_in_inv + 3 + len('count')
    dashes = dash * number_of_dashes  # =17
    
    # if order is issubclass(int, str):
    #     print('asqwe')

    if order is not None:
        print('Choose order. You can choose between ascending and descending.')
        print("To display ascending table write: 'print_table(inv, 'count,asc')")
        print("To display descending table write: 'print_table(inv, 'count,desc')")
        print('\n Your inventory: \n')

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
        # display_total_number_of_inventory()        


player = create_player()
print()
print(player)
print()
print(player["inventory"])
print()
player_inv = player["inventory"]

print()
print('++++++++++++++++')
# print('No order: ')
print()
print_table(player_inv, 'count,desc')