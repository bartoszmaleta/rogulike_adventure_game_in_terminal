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
import main as main


def action_after_key_pressed(board, player, key, PLAYER_SCORE, HEALTH):
    FILE_PATH_OF_GOODBYE_LOGO = "goodbye_logo.txt"
    goodbye_logo_list_of_list = engine.create_board_out_of_file(FILE_PATH_OF_GOODBYE_LOGO)

    FILE_PATH_CREDITS = "credits.txt"
    credits_board_list_of_list = engine.create_board_out_of_file(FILE_PATH_CREDITS)

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

    elif key == "m":
        is_running_menu = True
        while is_running_menu:
            helpers.clear_screen()
            main.handle_menu()
            try:
                # inputs = ui.get_inputs(["Please enter a number: "], "")
                # option = inputs[0]
                key = helpers.key_pressed()
                if key == "1":
                    is_running_menu = False
                elif key == "0":
                    helpers.clear_screen()
                    ui.display_goodbye_logo(goodbye_logo_list_of_list)
                    ui.display_credits(credits_board_list_of_list)  
                    sys.exit(0)
                else:
                    raise KeyError("There is no such option.")                
            except KeyError as err:
                ui.print_error_message(str(err))
                    
    return player, board, PLAYER_SCORE, HEALTH