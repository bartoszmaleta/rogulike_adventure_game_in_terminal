import helpers as helpers
import engine as engine
import ui as ui
import graphics as graphics
# import operator
import inventory_controller as inventory_controller
import chest as chest
import time
import copy
import turn_game as turn_game
# import map_manager as map_manager

# # TODO:
#  Right now:
#  - adding score                                                                   DONE
#  - showing score all the time                                                     DONE
#  - after gaining score 10 showing 'congrats' and changing to labirynth            DONE
#  - dollar sign disappearing after leaving spot of dollar sign                     DONE
#  - constant position in new level!                                                DONE
#  - Icons of attacks in turn game                                                  NOT DONE
#  - delete one loop                                                                NOT DONE
#  - HEALTH                                                                         NOT DONE
#  - case sensitive

# # TODO:
#  Further:
#  - choosing character by image of character and changing colour of "@" based on choosed character     DONE
#  - fighting game with boss                                                                            DONE
#  - ifinite game                                                                                       NOT DONE
#  - ascii art                                                                                          NOT DONE
#  - writing to file highscores                                                                         NOT DONE
#  - quiting the game                                                                                   NOT DONE
#  - menu showing                                                                                       NOT DONE
#  - another chest to grab                                                                              NOT DONE
#  - change appearence of inventory to beaty                                                            NOT DONE
#  - timer                                                                                              NOT DONE


PLAYER_START_X = 4
PLAYER_START_Y = 12
PLAYER_INV = {'rope': 0, 'torch': 0, 'gold coin': 0, 'dagger': 0, 'arrow': 0, 'bow': 0}
PLAYER_SCORE = 0
WIZARD_ICON = "\U0001F9D9"
WARRIOR_ICON = "\U0001F482"
ASSASSIN_ICON = "\U0001F9D5"

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
    player["icon"] = ''
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
            if old_board == "\U0001F9D9":
                board[board_y][board_x] = "."
            elif old_board == "\U0001F482":
                board[board_y][board_x] = "."
            elif old_board == "\U0001F9D5":
                board[board_y][board_x] = "."
            return player, board, PLAYER_SCORE
        elif new_board == "^":
            player[x_or_y_coord] = player[x_or_y_coord] + adjustment
            PLAYER_SCORE += 10
            if old_board == "@":
                board[board_y][board_x] = "."
            return player, board, PLAYER_SCORE
        elif new_board == ".":
            player[x_or_y_coord] = player[x_or_y_coord] + adjustment
            if old_board == "$":
                board[board_y][board_x] = "."
            elif old_board == "\U0001F9D9":
                board[board_y][board_x] = "."
            elif old_board == "\U0001F482":
                board[board_y][board_x] = "."
            elif old_board == "\U0001F9D5":
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

    # ui.print_introduction_screen(graphics.introduction_screen(), speed=0.05)
    # ui.print_introduction_screen(graphics.logo_of_game(), speed=0.005)

    # print(PLAYER_SCORE)
    # PLAYER_SCORE += 1
    # print(PLAYER_SCORE)

    #choosen_character_number = graphics.choosing_character()
    
    choosen_character_number = ui.class_selection_screen()
    PLAYER_SCORE = 0
    HEALTH = 5

    FILE_PATH = "map_visual.txt"
    FILE_PATH_OF_LABIRYNTH = "labirynth2.txt"       
    # FILE_PATH_OF_LABIRYNTH = "labirynth2.txt"       # "labirynth2.txt" to shortcut to exit
    player = create_player()
    
    if choosen_character_number == "1":
        character = 'wizard'
        player["icon"] = WIZARD_ICON
    elif choosen_character_number == "3":
        character = 'warrior'
        player["icon"] = WARRIOR_ICON
    elif choosen_character_number == "5":
        character = 'assasssin'
        player["icon"] = ASSASSIN_ICON
        
    player_inv = player["inventory"]
    is_running = True

    board_from_file = engine.create_board_out_of_file(FILE_PATH)              # ACTUAL VERSION ---> WORKS, BUT IT IS FROM FILE, AND DONT HIDE DOLLAR SIGN
    # >>> b = copy.deepcopy(a)
    
    # to show game without pressing key
    # board = engine.create_board_out_of_file(FILE_PATH)sd
    # ui.display_board(board)

    board = copy.deepcopy(board_from_file) 
    #board[10][3] = "\U0001F4A5"
    #board[21][21] = "\U0001F47D"
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
    #board = copy_board(board_out_of_file)       # NEW, NOT USED
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
                        if PLAYER_SCORE < 2 and HEALTH > 1:
                            # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)        # OLD VERSION ---> simple rectangle board out of algorithm
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
                        if PLAYER_SCORE < 6:
                            board = engine.create_board_out_of_file(FILE_PATH_OF_LABIRYNTH)
                            player, board, PLAYER_SCORE = change_player_position(board, player, key, PLAYER_SCORE)
                            board = engine.put_player_on_board(board, player)
                            ui.display_board(board)
                            ui.print_score_of_player(PLAYER_SCORE)       # should show????
                            # ui.print_table(player_inv, 'count,desc')          # dont know if in this lvl should show inventory!!!
                        else:
                            is_running_second_lvl = False
                
                is_running_third_lvl = True
                while is_running_third_lvl:
                    helpers.clear_screen()
                    # GRAPHICS WITH BOSS
                    if choosen_character_number == "1":
                        FILE_PATH_OF_WIZARD = "wizard.txt"
                        wizard_board = engine.create_board_out_of_file(FILE_PATH_OF_WIZARD)
                        ui.display_warrior(wizard_board)
                    elif choosen_character_number == "3":
                        FILE_PATH_OF_WIZARD = "warrior.txt"
                        warrior_board = engine.create_board_out_of_file(FILE_PATH_OF_WIZARD)
                        ui.display_warrior(warrior_board)
                    elif choosen_character_number == "5":
                        FILE_PATH_OF_ASSASIN = "assassin.txt"
                        assasin_board = engine.create_board_out_of_file(FILE_PATH_OF_ASSASIN)
                        ui.display_warrior(assasin_board)
                    
                    ui.print_text('Do you want to fight the boss (y/n)')
                    key = helpers.key_pressed()

                    if key == "y":
                        helpers.clear_screen()

                        # HOW TO PLAY                        
                        turn_game.how_to_play()
                        
                        is_running_fight = True
                        while is_running_fight:
                            turn_game.fighting_boss(character)
                            is_running_fight = False
                    elif key == 'n':
                        is_running_third_lvl = False
                    is_running_third_lvl = False
                

                # CREDITS
                ui.print_text('You win!!!!!!!!!!!!!!!!!!!!!!! Congrats')
                ui.print_text("Produced by .....")


if __name__ == '__main__':
    main()