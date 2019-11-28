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
import sys
# import map_manager as map_manager

# # TODO:
#  Right now:
#  - adding score                                                                   DONE
#  - showing score all the time                                                     DONE
#  - after gaining score 10 showing 'congrats' and changing to labirynth            DONE
#  - dollar sign disappearing after leaving spot of dollar sign                     DONE
#  - constant position in new level!                                                DONE
#  - Icons of attacks in turn game                                                  NOT DONE
#  - delete one loop                                                                NOT DONE OR NOT! MAYBE ANOTHER SCREEN
#  - HEALTH                                                                         NOT DONE, ALMOST!! NOT FOR BATTLE
#  - Goodbye screen!!!!                                                             NOT DONE! priority
#  - case sensitive                                                                 NOT DONE

# # TODO:
#  Further:
#  - choosing character by image of character and changing colour of "@" based on choosed character     DONE
#  - fighting game with boss                                                                            DONE
#  - ifinite game                                                                                       DONE, ALMOST! EXCEPT FIGHTING
#  - ascii art colour                                                                                   NOT DONE
#  - writing to file highscores                                                                         NOT DONE! priority
#  - clean screen during fight                                                                          NOT DONE! priority    
#  - quiting the game from menu                                                                         NOT DONE! priority
#  - MENU                                                                                               NOT DONE! priority
#  - menu showing                                                                                       NOT DONE! priority
#  - another chest to grab                                                                              NOT DONE
#  - change appearence of inventory to beaty                                                            NOT DONE! priority
#  - timer                                                                                              NOT DONE! priority


PLAYER_START_X = 4
PLAYER_START_Y = 12
PLAYER_INV = {'rope': 0, 'torch': 0, 'gold coin': 0, 'dagger': 0, 'arrow': 0, 'bow': 0}
PLAYER_SCORE = 0
WIZARD_ICON = "\U0001F9D9"
WARRIOR_ICON = "\U0001F482"
ASSASSIN_ICON = "\U0001F9D5"

BOARD_WIDTH = 40
BOARD_HEIGHT = 10

BOARD_WIDTH = 20


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


def action_after_key_pressed(board, player, key, PLAYER_SCORE, HEALTH):
    player_x = player["x"]
    player_y = player["y"]
    player_inv = player["inventory"]
    player_icon = "\U0001F9D9"
    BLAST_ICON = "\U0001F4A5"

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
            new_player_position_on_board = board[player_new_x_or_y_position][player_x]
            old_player_position_on_board = board[player_old_x_or_y_position][player_x]
        elif key == "a" or key == "d":
            new_player_position_on_board = board[player_y][player_new_x_or_y_position]
            old_player_position_on_board = board[player_y][player_old_x_or_y_position]

        if key == "w" or key == "s":
            board_y = player_old_x_or_y_position
            board_x = player_x
        elif key == "a" or key == "d":
            board_y = player_y
            board_x = player_old_x_or_y_position

        if new_player_position_on_board == "X":
            return player, board, PLAYER_SCORE, HEALTH
        elif new_player_position_on_board == "o":
            return player, board, PLAYER_SCORE, HEALTH
        elif new_player_position_on_board == "O":
            return player, board, PLAYER_SCORE, HEALTH
        elif new_player_position_on_board == "'":
            return player, board, PLAYER_SCORE, HEALTH
        elif new_player_position_on_board == "=":
            return player, board, PLAYER_SCORE, HEALTH
        elif new_player_position_on_board == "$":
            player[x_or_y_coord] = player[x_or_y_coord] + adjustment
            inventory_controller.add_to_inventory(player_inv, chest.chest_inventory)
            PLAYER_SCORE += 1
            if old_player_position_on_board == player_icon:
                board[board_y][board_x] = "."
            return player, board, PLAYER_SCORE, HEALTH
        elif new_player_position_on_board == "^":
            player[x_or_y_coord] = player[x_or_y_coord] + adjustment
            PLAYER_SCORE += 10
            if old_player_position_on_board == "@":
                board[board_y][board_x] = "."
            return player, board, PLAYER_SCORE, HEALTH
        elif new_player_position_on_board == ".":
            player[x_or_y_coord] = player[x_or_y_coord] + adjustment
            if old_player_position_on_board == "$":
                board[board_y][board_x] = "."
            elif old_player_position_on_board == player_icon:
                board[board_y][board_x] = "."
            elif old_player_position_on_board == "^":
                PLAYER_SCORE += 10
            return player, board, PLAYER_SCORE, HEALTH
        elif new_player_position_on_board == "|":
            player[x_or_y_coord] = player[x_or_y_coord] + adjustment
            if old_player_position_on_board == "$":
                board[board_y][board_x] = "."
            elif old_player_position_on_board == "^":
                PLAYER_SCORE += 10
            return player, board, PLAYER_SCORE, HEALTH
        elif new_player_position_on_board == BLAST_ICON:
            player[x_or_y_coord] = player[x_or_y_coord] + adjustment
            HEALTH -= 1
            if old_player_position_on_board == player_icon:
                board[board_y][board_x] = "."
            return player, board, PLAYER_SCORE, HEALTH
        return player, board, PLAYER_SCORE, HEALTH
    
    elif key == "i":
        is_running_inventory = True
        while is_running_inventory:
            key = helpers.key_pressed()
            
            helpers.clear_screen()
            ui.print_table(player_inv, 'count,desc')
            ui.print_text('Press e for exit')
            if key == "e":
                is_running_inventory = False    

    return player, board, PLAYER_SCORE, HEALTH


def const_position(player, player_x_position, player_y_position):

    player["x"] = player_x_position
    player["y"] = player_y_position

    return player


def main():

    # ui.print_introduction_screen(graphics.introduction_screen(), speed=0.05)
    # ui.print_introduction_screen(graphics.logo_of_game(), speed=0.005)

    # choosen_character_number = graphics.choosing_character()
    
    choosen_character_number = ui.class_selection_screen()

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

    board_from_file = engine.create_board_out_of_file(FILE_PATH)              # ACTUAL VERSION ---> WORKS, BUT IT IS FROM FILE, AND DONT HIDE DOLLAR SIGN
    board = copy.deepcopy(board_from_file) 

    ui.put_emoji_on_board(board)

    is_running = True
    while is_running:
        # input_ask = input('Do you want to START a game? (y/n): ')
        HEALTH = 1
        PLAYER_SCORE = 0

        ui.print_text("Press any key to START! Press * to exit")
        key = helpers.key_pressed()
        if key == '*':
            is_running = False
        else:
            is_running_first_lvl = True
            while is_running_first_lvl:
                key = helpers.key_pressed()
                if key == 'q':
                    is_running = False
                else:
                    if PLAYER_SCORE < 2 and HEALTH > 0:
                        # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)        # OLD VERSION ---> simple rectangle board out of algorithm
                        # board = engine.create_board_out_of_file(FILE_PATH)              # ACTUAL VERSION ---> WORKS, BUT IT IS FROM FILE, AND DONT HIDE DOLLAR SIGN
                        player, board, PLAYER_SCORE, HEALTH  = action_after_key_pressed(board, player, key, PLAYER_SCORE, HEALTH)
                        board = engine.put_player_on_board(board, player)
                        ui.display_board(board)
                        ui.print_table(player_inv, 'count,desc')
                        ui.print_score_of_player(PLAYER_SCORE)       
                        ui.display_heath(HEALTH)
                    else:
                        is_running_first_lvl = False
            if PLAYER_SCORE >= 2 and HEALTH > 0:
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
                            player, board, PLAYER_SCORE, HEALTH = action_after_key_pressed(board, player, key, PLAYER_SCORE, HEALTH)
                            board = engine.put_player_on_board(board, player)
                            ui.display_board(board)
                            ui.print_score_of_player(PLAYER_SCORE)       # should show????
                            # ui.print_table(player_inv, 'count,desc')          # dont know if in this lvl should show inventory!!!
                        else:
                            is_running_second_lvl = False
                if PLAYER_SCORE >= 2 and HEALTH > 0:
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
                        ui.print_text('Do you want to FIGHT the boss (y/n)')
                        key = helpers.key_pressed()
                        if key == "y":
                            helpers.clear_screen()
                            # HOW TO PLAY                        
                            turn_game.how_to_play()
                            is_running_fight = True
                            while is_running_fight:
                                turn_game.fighting_boss(character, HEALTH)
                                is_running_fight = False
                            is_running_third_lvl
                        elif key == 'n':
                            is_running_third_lvl = False
                        is_running_third_lvl = False
            if HEALTH > 1:
                ui.print_text('You win!!!!!!!!!!!!!!!!!!!!!!! Congrats')
                # CREDITS
                ui.print_text("Produced by .....")
                break
                is_running_third_lvl = False
                is_running_second_lvl = False
            else:       # HEALTH < 1
                ui.print_text("You lost")
                input_ask = input('Do you want to START AGAIN a game? (y/n): ')
                if input_ask == "y":
                    is_running_third_lvl = False
                elif input_ask == "n":
                    ui.print_text("Good bye")
                    sys.exit(0)                    


if __name__ == '__main__':
    main()