import helpers as helpers
import engine as engine
import ui as ui
import map_manager as map_manager
import csv

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

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
    return player


def change_player_position(board, player, key):
    player_x = player["x"]
    player_y = player["y"]
    
    if key in "wasd":
        if key == "w":
            player_new_y_position = player["y"] - 1

            if board[player_new_y_position][player_x] == "X":
                return player
            elif board[player_new_y_position][player_x] == ".":  
                player["y"] = player["y"] - 1

        elif key == "s":
            player_new_y_position = player["y"] + 1

            if board[player_new_y_position][player_x] == "X":
                return player
            elif board[player_new_y_position][player_x] == ".":
                player["y"] = player["y"] + 1

        elif key == "a":
            player_new_x_position = player["x"] - 1

            if board[player_y][player_new_x_position] == "X":
                return player
            elif board[player_y][player_new_x_position] == ".":
                player["x"] = player["x"] - 1

        elif key == "d":
            player_new_x_position = player["x"] + 1

            if board[player_y][player_new_x_position] == "X":
                return player
            elif board[player_y][player_new_x_position] == ".":
                player["x"] = player["x"] + 1
    
    return player


def create_map(file_name):
    # board = []
    # # -------------------------------------    CSV
    # file_name2 = "map2.csv"
    # crimefile = open(file_name2, 'r')
    # reader = csv.reader(crimefile)
    # allRows = [row for row in reader]
    # print(allRows)
    # print('-------------------------------------')
    # for elem in allRows:
        # print(elem)
    print('------------------------------------- should print file_obj')
    print()
    myFile = open(file_name, "r+")
    myLines = list(myFile)
    myFile.close()
    # print(len(myLines))
    # print(myLines)
    
    board2 = []
    small_list = []
    counter = 0

    for line in myLines:
        board2.append(line)

    list_of_map = []
    list_of_map.append(board2)
    print('-------=====================')
    print(board2)  # wrong, lists with lines
    print('-------=====================')
    print(list_of_map)      # list with lists with lines
    print('-------=====================')
    for row in board2:
    # this one could be one line!!!!! :
    # print(''.join(row))
        for element in row:
            print(element, end="")
    print()

    print('-------=====================')
    # with open(file_name) as file_obj:
    #     list_of_file = file_obj.readlines()

    #     print(type(list_of_file))
    #     print(list_of_file)

    #     for line in list_of_file:
    #         print(len(line))
    #         for row_index in range(len(line)):
    #             board = []
    #             for col_index in range(len(line)):
    #                 board.append(line[col_index])
    #                 # board[row_index][col_index] = line[col_index]

    # print(board)        

    # print()
        # for row_index in range(len(file_obj)):
            # board = []
            # for character in line:
                # board.append(character)
            # print(line, end='')
    # print('-------------------------------------')
    # -------------------------------------    
    # with open(file_name) as file_obj:
        # for line in file_obj:
            # for character in line:
                # board.append(character)
            # print(line, end='')
    # print('-------------------------------------')
    # print(type(board))
    
    # for elem in board:
        # print(elem, end='')
    # # print(board)


def main():
    # ---------------------------------------------------------
    FILE_PATH = "map.txt"
    # map_to_play = create_map(FILE_PATH)
    # ---------------------------------------------------------
    player = create_player()

    is_running = True
    
    while is_running:
        key = helpers.key_pressed()
        if key == 'q':
            is_running = False

        # else:
        #     print(key)
        # if key == 'z':
        #     helpers.clear_screen()

        else:
            board = create_map(FILE_PATH)

            # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
            player = change_player_position(board, player, key)
            board = engine.put_player_on_board(board, player)
            ui.display_board(board)


if __name__ == '__main__':
    main()