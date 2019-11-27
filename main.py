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
#  - writing to file highscores                                                     NOT DONE
#  - quiting the game                                                               NOT DONE
#  - menu showing                                                                   NOT DONE
#  - another chest to grab                                                          NOT DONE
#  - change appearence of inventory to beaty                                        NOT DONE
#  - timer                                                                          NOT DONE

# # TODO:
#  Further:
#  - choosing character by image of character and changing colour of "@" based on choosed character         NOT DONE
#  - fighting game with boss                                                                                NOT DONE
#  - ifinite game                                                                                           NOT DONE
#  - ascii art                                                                                              NOT DONE


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

    if key in "wasd":
        if key == "w":
            player_new_y_position = player["y"] - 1
            player_old_y_position = player["y"]

            if board[player_new_y_position][player_x] == "X":
                return player, board, PLAYER_SCORE
            elif board[player_new_y_position][player_x] == "o":
                return player, board, PLAYER_SCORE
            elif board[player_new_y_position][player_x] == "O":
                return player, board, PLAYER_SCORE
            elif board[player_new_y_position][player_x] == "'":
                return player, board, PLAYER_SCORE
            elif board[player_new_y_position][player_x] == "$":
                player["y"] = player["y"] - 1
                inventory_controller.add_to_inventory(player_inv, chest.chest_inventory)
                PLAYER_SCORE += 1
                if board[player_old_y_position][player_x] == "@":
                    board[player_old_y_position][player_x] = "."
                return player, board, PLAYER_SCORE
            elif board[player_new_y_position][player_x] == ".":
                player["y"] = player["y"] - 1
                if board[player_old_y_position][player_x] == "$":
                    board[player_old_y_position][player_x] = "."
                elif board[player_old_y_position][player_x] == "@":
                    board[player_old_y_position][player_x] = "."
                elif board[player_old_y_position][player_x] == "^":
                    PLAYER_SCORE += 10
                return player, board, PLAYER_SCORE
            elif board[player_new_y_position][player_x] == "|":
                player["y"] = player["y"] - 1
                if board[player_old_y_position][player_x] == "$":
                    board[player_old_y_position][player_x] = "."
                elif board[player_old_y_position][player_x] == "^":
                    PLAYER_SCORE += 10
                return player, board, PLAYER_SCORE
            elif board[player_new_y_position][player_x] == "=":
                player["y"] = player["y"] - 1
                if board[player_old_y_position][player_x] == "$":
                    board[player_old_y_position][player_x] = "."
                elif board[player_old_y_position][player_x] == "^":
                    PLAYER_SCORE += 10
                return player, board, PLAYER_SCORE
            return player, board, PLAYER_SCORE

        elif key == "s":
            player_new_y_position = player["y"] + 1
            player_old_y_position = player["y"]

            if board[player_new_y_position][player_x] == "X":
                return player, board, PLAYER_SCORE
            elif board[player_new_y_position][player_x] == "o":
                return player, board, PLAYER_SCORE
            elif board[player_new_y_position][player_x] == "O":
                return player, board, PLAYER_SCORE
            elif board[player_new_y_position][player_x] == "'":
                return player, board, PLAYER_SCORE
            elif board[player_new_y_position][player_x] == "$":
                player["y"] = player["y"] + 1
                inventory_controller.add_to_inventory(player_inv, chest.chest_inventory)
                PLAYER_SCORE += 1
                if board[player_old_y_position][player_x] == "@":
                    board[player_old_y_position][player_x] = "."
                return player, board, PLAYER_SCORE
            elif board[player_new_y_position][player_x] == ".":
                player["y"] = player["y"] + 1
                if board[player_old_y_position][player_x] == "$":
                    board[player_old_y_position][player_x] = "."
                elif board[player_old_y_position][player_x] == "@":
                    board[player_old_y_position][player_x] = "."
                elif board[player_old_y_position][player_x] == "^":
                    PLAYER_SCORE += 10
                return player, board, PLAYER_SCORE      
            elif board[player_new_y_position][player_x] == "|":
                player["y"] = player["y"] + 1
                if board[player_old_y_position][player_x] == "$":
                    board[player_old_y_position][player_x] = "."
                elif board[player_old_y_position][player_x] == "^":
                    PLAYER_SCORE += 10
                return player, board, PLAYER_SCORE 
            elif board[player_new_y_position][player_x] == "=":
                player["y"] = player["y"] + 1
                if board[player_old_y_position][player_x] == "$":
                    board[player_old_y_position][player_x] = "."
                return player, board, PLAYER_SCORE               
            elif board[player_new_y_position][player_x] == "^":
                player["y"] = player["y"] + 1
                PLAYER_SCORE += 10
                return player, board, PLAYER_SCORE
            return player, board, PLAYER_SCORE

        elif key == "a":
            player_new_x_position = player["x"] - 1
            player_old_x_position = player["x"]

            if board[player_y][player_new_x_position] == "X":
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == "o":
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == "O":
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == "'":
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == "$":
                player["x"] = player["x"] - 1
                inventory_controller.add_to_inventory(player_inv, chest.chest_inventory)
                PLAYER_SCORE += 1
                if board[player_y][player_old_x_position] == "@":
                    board[player_y][player_old_x_position] = "."                
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == ".":
                player["x"] = player["x"] - 1
                if board[player_y][player_old_x_position] == '$':
                    board[player_y][player_old_x_position] = '.'
                elif board[player_y][player_old_x_position + 2] == "=" and board[player_y - 2][player_old_x_position] == "." and board[player_y + 1][player_old_x_position] == "=":
                    board[player_y][player_old_x_position] = "="
                elif board[player_y][player_old_x_position + 2] == "=" and board[player_y - 2][player_old_x_position] == "." and board[player_y - 1][player_old_x_position] == "=":
                    board[player_y][player_old_x_position] = "="
                elif board[player_y][player_old_x_position] == "@":
                    board[player_y][player_old_x_position] = "."
                elif board[player_y][player_old_x_position] == "^":
                    PLAYER_SCORE += 10
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == "|":
                player["x"] = player["x"] - 1
                if board[player_y][player_old_x_position] == '$':
                    board[player_y][player_old_x_position] = '.'
                elif board[player_y][player_old_x_position] == "^":
                    PLAYER_SCORE += 10
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == "=":
                player["x"] = player["x"] - 1
                # if board[player_y][player_old_x_position] == '$':
                #     board[player_y][player_old_x_position] = '.'
                # elif board[player_y][player_old_x_position] == "^":
                #     PLAYER_SCORE += 10
                if board[player_y][player_old_x_position] == '$':
                    board[player_y][player_old_x_position] = '.'
                elif board[player_y][player_old_x_position] == '|':
                    board[player_y][player_old_x_position] = '.'        # here change to when there will be copy_board
                elif board[player_y][player_old_x_position] == "@" and board[player_y - 1][player_old_x_position] == "." and board[player_y - 1][player_old_x_position - 3] == "o" and board[player_y - 2][player_old_x_position + 10] == "#":
                    board[player_y][player_old_x_position] = "."
                elif board[player_y][player_old_x_position] == "@" and board[player_y - 1][player_old_x_position] == "." and board[player_y + 1][player_old_x_position] == "." and board[player_y - 2][player_old_x_position - 3] == "o":
                    board[player_y][player_old_x_position] = "."
                elif board[player_y][player_old_x_position] == "@":
                    board[player_y][player_old_x_position] = "="
                elif board[player_y][player_old_x_position] == "^":
                    PLAYER_SCORE += 10
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == "\U0001F600":
                PLAYER_SCORE += 1
            return player, board, PLAYER_SCORE

        elif key == "d":
            player_new_x_position = player["x"] + 1
            player_old_x_position = player["x"]

            if board[player_y][player_new_x_position] == "X":
            # if board[player_y][player_new_x_position] == "X" or "o" or "O" or "-" or "/" or "\\" or "#" or "*":
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == "o":
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == "O":
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == "'":
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == "$":
                if board[player_y][player_old_x_position] == "@":
                    board[player_y][player_old_x_position] = "."
                player["x"] = player["x"] + 1
                inventory_controller.add_to_inventory(player_inv, chest.chest_inventory)
                PLAYER_SCORE += 1
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == ".":
                player["x"] = player["x"] + 1
                if board[player_y][player_old_x_position] == '$':
                    board[player_y][player_old_x_position] = '.'
                elif board[player_y][player_old_x_position - 2] == "=" and board[player_y - 2][player_old_x_position] == "." and board[player_y + 1][player_old_x_position] == "=":
                    board[player_y][player_old_x_position] = "="
                elif board[player_y][player_old_x_position - 2] == "=" and board[player_y - 2][player_old_x_position] == "." and board[player_y - 1][player_old_x_position] == "=":
                    board[player_y][player_old_x_position] = "="
                elif board[player_y][player_old_x_position] == '@':
                    board[player_y][player_old_x_position] = '.'
                elif board[player_y][player_old_x_position] == "^":
                    PLAYER_SCORE += 10
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == "|":
                player["x"] = player["x"] + 1
                if board[player_y][player_old_x_position] == '$':
                    board[player_y][player_old_x_position] = '.'
                elif board[player_y][player_old_x_position] == "^":
                    PLAYER_SCORE += 10      # here doing
                elif board[player_y][player_old_x_position] == "@":
                    board[player_y][player_old_x_position] = "."
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == "=":
                player["x"] = player["x"] + 1
                if board[player_y][player_old_x_position] == '$':
                    board[player_y][player_old_x_position] = '.'
                elif board[player_y][player_old_x_position] == '|':
                    board[player_y][player_old_x_position] = '.'        # here change to when there will be copy_board
                elif board[player_y][player_old_x_position] == "@" and board[player_y - 1][player_old_x_position] == "." and board[player_y + 1][player_old_x_position] == "o":
                    board[player_y][player_old_x_position] = "."
                elif board[player_y][player_old_x_position] == "@" and board[player_y - 1][player_old_x_position] == "." and board[player_y + 1][player_old_x_position] == ".":
                    board[player_y][player_old_x_position] = "."
                elif board[player_y][player_old_x_position] == "@":
                    board[player_y][player_old_x_position] = "="
                elif board[player_y][player_old_x_position] == "^":
                    PLAYER_SCORE += 10
                return player, board, PLAYER_SCORE
            elif board[player_y][player_new_x_position] == "\U0001F600":
                PLAYER_SCORE += 1
            return player, board, PLAYER_SCORE
        elif key == "i":
            is_running_inventory = True
            while is_running_inventory:
                key = helpers.key_pressed()
                
                helpers.clear_screen()
                ui.print_table(player_inv, 'count,desc')
                ui.print_text('Press e for exit')
                if key == "e":
                    is_running_inventory = False
                else:
                    pass
    return player, board, PLAYER_SCORE


def copy_board(board):      # NEW, NOT USED
    board = board.copy()
    return board


def const_position(player, player_x_position, player_y_position):

    player["x"] = player_x_position
    player["y"] = player_y_position

    return player


def main():

    # ui.print_introduction_screen(graphics.introduction_screen(), speed=0.05)
    # ui.print_introduction_screen(graphics.logo_of_game(), speed=0.005)

    # print(PLAYER_SCORE)
    # PLAYER_SCORE += 1
    # print(PLAYER_SCORE)

    # choosen_character_number = ui.class_selection_screen()
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
    board[10][3] = "\U0001F600" 
    board[10][31] = "\U0001F41F"
    
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
                    elif key == "i":
                        is_running_inventory = True
                        while is_running_inventory:
                            key = helpers.key_pressed()
                            
                            helpers.clear_screen()
                            ui.print_table(player_inv, 'count,desc')
                            ui.print_text('Press e for exit')
                            if key == "e":
                                is_running_inventory = False
                        
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