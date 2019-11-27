import helpers as helpers
import engine as engine
import ui as ui
import graphics as graphics
# import operator
import inventory_controller as inventory_controller
import chest as chest
import time
import copy
# import map_manager as map_manager

# # TODO:
#  Right now:
#  - adding score                                                                   DONE
#  - showing score all the time                                                     DONE
#  - after gaining score 10 showing 'congrats' and changing to labirynth            DONE
#  - dollar sign disappearing after leaving spot of dollar sign                     DONE
#  - constant position in new level!                                                DONE

# # TODO:
#  Further:
#  - choosing character by image of character and changing colour of "@" based on choosed character
#  - fighting game with boss
#  - ifinite game
#  - ascii art 


PLAYER_ICON = '@'
PLAYER_START_X = 4
PLAYER_START_Y = 12
PLAYER_INV = {'rope': 0, 'torch': 0, 'gold coin': 0, 'dagger': 0, 'arrow': 0, 'bow': 0}
PLAYER_SCORE = 0

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
    # player["score"] = PLAYER_SCORE       # NEW, NOT USED
    return player


def change_player_position(board, player, key, PLAYER_SCORE):
    player_x = player["x"]
    player_y = player["y"]
    player_inv = player["inventory"]

    if key in "wsad":
        if key == "w" or key == "s":
            x_or_y_coord = "y"
        elif key == "a" or key == "d":
            x_or_y_coord = "x"

        if key == "w" or key == "a":
            adjustment = -1
        elif key == "d" or key == "s":
            adjustment = 1
        
        player_new_x_or_y_position = player[x_or_y_coord] + adjustment
        player_old_x_or_y_position = player[x_or_y_coord]

        if key == "w" or key == "s":
            new_board = board[player_new_x_or_y_position][player_x]
            old_board = board[player_old_x_or_y_position][player_x]
        elif key == "a" or key == "d":
            new_board = board[player_y][player_new_x_or_y_position]
            old_board = board[player_y][player_old_x_or_y_position]

        if key == "w" or key == "s":
            board_y = player_old_x_or_y_position
            board_x = player_x
        elif key == "a" or key == "d":
            board_y = player_y
            board_x = player_old_x_or_y_position

        if new_board == "X":
            return player, board, PLAYER_SCORE
        elif new_board == "o":
            return player, board, PLAYER_SCORE
        elif new_board == "O":
            return player, board, PLAYER_SCORE
        elif new_board == "'":
            return player, board, PLAYER_SCORE
        elif new_board == "=":
            return player, board, PLAYER_SCORE
        elif new_board == "$":
            player[x_or_y_coord] = player[x_or_y_coord] + adjustment
            inventory_controller.add_to_inventory(player_inv, chest.chest_inventory)
            PLAYER_SCORE += 1
            if old_board == "@":
                board[board_y][board_x] = "."
            return player, board, PLAYER_SCORE
        elif new_board == ".":
            player[x_or_y_coord] = player[x_or_y_coord] + adjustment
            if old_board == "$":
                board[board_y][board_x] = "."
            elif old_board == "@":
                board[board_y][board_x] = "."
            elif old_board == "^":
                PLAYER_SCORE += 10
            return player, board, PLAYER_SCORE
        elif new_board == "|":
            player[x_or_y_coord] = player[x_or_y_coord] + adjustment
            if old_board == "$":
                board[board_y][board_x] = "."
            elif old_board == "^":
                PLAYER_SCORE += 10
            return player, board, PLAYER_SCORE
        return player, board, PLAYER_SCORE

    return player, board, PLAYER_SCORE


def copy_board(board):      # NEW, NOT USED
    board = board.copy()
    return board


def const_position(player, player_x_position, player_y_position):

    player["x"] = player_x_position
    player["y"] = player_y_position

    return player


def main():

    #ui.print_introduction_screen(graphics.introduction_screen(), speed=0.05)
    time.sleep(1)
    #ui.print_introduction_screen(graphics.logo_of_game(), speed=0.005)

    # print(PLAYER_SCORE)
    # PLAYER_SCORE += 1
    # print(PLAYER_SCORE)

    choosen_character_number = ui.class_selection_screen()
    PLAYER_SCORE = 0

    FILE_PATH = "map_visual.txt"
    FILE_PATH_OF_LABIRYNTH = "labirynth2.txt"       
    # FILE_PATH_OF_LABIRYNTH = "labirynth2.txt"       # "labirynth2.txt" to shortcut to exit
    player = create_player()
    player_inv = player["inventory"]
    is_running = True

    board_from_file = engine.create_board_out_of_file(FILE_PATH)              # ACTUAL VERSION ---> WORKS, BUT IT IS FROM FILE, AND DONT HIDE DOLLAR SIGN
    # >>> b = copy.deepcopy(a)
    
    # to show game without pressing key
    # board = engine.create_board_out_of_file(FILE_PATH)
    # ui.display_board(board)
    board = copy.deepcopy(board_from_file) 
    
    # board = copy_board(board_out_of_file)       # NEW, NOT USED
    while is_running:
        input_ask = input('Do you want to start a game? (y/n): ')

        if input_ask == 'q':
            is_running = False

        else:
            key = helpers.key_pressed()
            if key == 'q':
                is_running = False
            else:
                is_running_first_lvl = True
                while is_running_first_lvl:
                    key = helpers.key_pressed()
                    if key == 'q':
                        is_running = False
                    else:
                        if PLAYER_SCORE < 2:
                            # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)        # OLD VERSION ---> simple rectangle board out of algorithm
                            # board = engine.create_board_out_of_file(FILE_PATH_OF_LABIRYNTH)           # TO GET LABIRYNTH VERSION, JUST UNCOMMENT THIS LINE, AND COMMENT LINE 169
                            # board = engine.create_board_out_of_file(FILE_PATH)              # ACTUAL VERSION ---> WORKS, BUT IT IS FROM FILE, AND DONT HIDE DOLLAR SIGN
                            player, board, PLAYER_SCORE  = change_player_position(board, player, key, PLAYER_SCORE)
                            board = engine.put_player_on_board(board, player)
                            ui.display_board(board)
                            ui.print_table(player_inv, 'count,desc')
                            ui.print_score_of_player(PLAYER_SCORE)       # NEW, NOT USED
                        else:
                            is_running_first_lvl = False

                is_running_second_lvl = True
                # position of player in second lvl:
                PLAYER_START_X = 6
                PLAYER_START_Y = 15
                player = const_position(player, PLAYER_START_X, PLAYER_START_Y)                
                while is_running_second_lvl:
                    key = helpers.key_pressed()
                    if key == 'q':
                        is_running = False
                    else:                    
                        if PLAYER_SCORE < 4:
                            board = engine.create_board_out_of_file(FILE_PATH_OF_LABIRYNTH)
                            player, board, PLAYER_SCORE = change_player_position(board, player, key, PLAYER_SCORE)
                            board = engine.put_player_on_board(board, player)
                            ui.display_board(board)
                            ui.print_score_of_player(PLAYER_SCORE)       # NEW, NOT USED
                            # ui.print_table(player_inv, 'count,desc')          # dont know if in this lvl should show inventory!!!
                        else:
                            is_running_second_lvl = False
                
                # PLAYER_SCORE = 0
                ui.print_text('You win')
                # time.sleep(2)
                # continue


if __name__ == '__main__':
    main()