import helpers as helpers
import engine as engine
import ui as ui
import graphics as graphics
# import operator
# import inventory_controller as inventory_controller
# import chest as chest
import time
import copy
import turn_game as turn_game
import sys
import player_controller as player_controller
# import map_manager as map_manager

#  TODO:
#  Right now:
#  - timer                                                                                              DONE, partially! ONE LOOP
#  - Icons of attacks in turn game                                                                      NOT DONE! priority
#  - ui.display_goodbye_logo_and_credits() ---> change credits                                          NOT DONE! priority
#  - writing to file highscores                                                                         DONE, partially! ONE LOOP
#  - ascii art colour                                                                                   NOT DONE! priority
#  - start point in beauty position                                                                     NOT DONE! priority
#  - case sensitive                                                                                     NOT DONE


#  TODO:
#  Further:
#  - clean screen during fight                                                                          NOT DONE! priority    
#  - ifinite game                                                                                       DONE, ALMOST! EXCEPT FIGHTING! When lose program breaks!
#  - HEALTH                                                                                             DONE, ALMOST!! NOT FOR BATTLE
#  - another chest to grab                                                                              NOT DONE


PLAYER_INV = {'healing potions': 0, 'magic mushrooms': 0, 'anti-alien cream': 0, 'shield': 0, 'weapon': 0, 'old map': 0}
PLAYER_SCORE = 0
WIZARD_ICON = "\U0001F9D9"
WARRIOR_ICON = "\U0001F482"
ASSASSIN_ICON = "\U0001F9D5"
PLAYER_START_X = 4
PLAYER_START_Y = 12


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


def handle_menu():
    options = ["Back to the game"]
    menu_title = ''
    
    ui.print_menu(menu_title, options, "Exit program")


def const_position(player, player_x_position, player_y_position):
    player["x"] = player_x_position
    player["y"] = player_y_position

    return player


def creating_highscore_file_after_wining(name, PLAYER_SCORE, time_of_the_game_afer_winning):
    with open('highscores2.txt', 'a') as hs:
        line_hs_one_str = (
            str(name) +
            ' : ' +
            str(PLAYER_SCORE) +
            ' : ')

        line_with_time = (time_of_the_game_afer_winning)
        line_with_time_str = str(line_with_time)
        hs.write(line_hs_one_str + line_with_time_str + '\n')
        hs.close()


# NOT USED, BECAUSE IT WANTS TABLE AND WE HAVE PURE DATA
def write_table_to_file(file_name, table):
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")


def main():
    # NAME!!!! to make highscore
    input_name = ui.get_inputs(["name"], "Please provide your ")
    input_name = input_name[0]
    # ui.welcoming_text()
    # ui.print_introduction_screen(graphics.introduction_screen(), speed=0.05)
    # ui.print_introduction_screen(graphics.logo_of_game(), speed=0.005)

    # choosen_character_number = graphics.choosing_character()
    
    choosen_character_number = ui.class_selection_screen()

    FILE_PATH_OF_GOODBYE_LOGO = "goodbye_logo.txt"
    goodbye_logo_list_of_list = engine.create_board_out_of_file(FILE_PATH_OF_GOODBYE_LOGO)

    FILE_PATH_CREDITS = "credits.txt"
    credits_board_list_of_list = engine.create_board_out_of_file(FILE_PATH_CREDITS)

    FILE_PATH_OF_YOU_WON = "you_won.txt"
    you_won_logo_list_of_list = engine.create_board_out_of_file(FILE_PATH_OF_YOU_WON)

    player = create_player()
    player_inv = player["inventory"]
    
    if choosen_character_number == "1":
        character = 'wizard'
        player["icon"] = WIZARD_ICON
    elif choosen_character_number == "3":
        character = 'warrior'
        player["icon"] = WARRIOR_ICON
    elif choosen_character_number == "5":
        character = 'assasssin'
        player["icon"] = ASSASSIN_ICON

    FILE_PATH = "map_visual.txt"
    FILE_PATH_OF_LABIRYNTH = "labirynth2.txt"       
    # FILE_PATH_OF_LABIRYNTH = "labirynth.txt"       # "labirynth2.txt" to shortcut to exit
    board_from_file = engine.create_board_out_of_file(FILE_PATH)              # ACTUAL VERSION ---> WORKS, BUT IT IS FROM FILE, AND DONT HIDE DOLLAR SIGN
    board = copy.deepcopy(board_from_file) 

    ui.put_emoji_on_board(board)

    is_running = True
    while is_running:
        # input_ask = input('Do you want to START a game? (y/n): ')
        HEALTH = 5
        PLAYER_SCORE = 0

        ui.print_text("Press any key to START! Press * to exit")

        key = helpers.key_pressed()
        if key == '*':
            # GOODBYE SCREEN
            sys.exit(0)
            is_running = False
        else:
            PLAYER_SCORE = 0
            is_running_first_lvl = True
            PLAYER_START_X = 4
            PLAYER_START_Y = 12
            player = const_position(player, PLAYER_START_X, PLAYER_START_Y)  
            
            while is_running_first_lvl:
                starttime = time.time()
                key = helpers.key_pressed()
                if key == 'q':
                    is_running = False
                elif key == 'i':
                    ui.print_inventory_and_wait(player_inv)
                else:
                    if PLAYER_SCORE < 2 and HEALTH > 0:

                        # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)        # OLD VERSION ---> simple rectangle board out of algorithm
                        # board = engine.create_board_out_of_file(FILE_PATH)              # ACTUAL VERSION ---> WORKS, BUT IT IS FROM FILE, AND DONT HIDE DOLLAR SIGN
                        player, board, PLAYER_SCORE, HEALTH  = player_controller.action_after_key_pressed(board, player, key, PLAYER_SCORE, HEALTH)
                        board = engine.put_player_on_board(board, player)
                        ui.display_board(board)
                        ui.print_how_to_show_inventory()
                        ui.print_score_of_player(PLAYER_SCORE)       
                        ui.display_heath(HEALTH)
                        ui.display_press_m_to_menu()
                    else:
                        is_running_first_lvl = False

            if PLAYER_SCORE >= 2 and HEALTH > 0 and PLAYER_SCORE < 10:
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
                            player, board, PLAYER_SCORE, HEALTH = player_controller.action_after_key_pressed(board, player, key, PLAYER_SCORE, HEALTH)
                            board = engine.put_player_on_board(board, player)
                            
                            ui.display_board(board)
                            ui.print_score_of_player(PLAYER_SCORE)       # should show????
                            ui.display_press_m_to_menu()
                            # ui.print_table(player_inv, 'count,desc')          # dont know if in this lvl should show inventory!!!
                        elif PLAYER_SCORE > 10:
                            is_running_second_lvl = False
                    
                        elif HEALTH < 1:       # HEALTH < 1
                            ui.print_text("You lost")
                            input_ask = input('Do you want to START AGAIN a game? (y/n): ')
                            if input_ask == "y":
                                is_running_third_lvl = False
                            elif input_ask == "n":
                                helpers.clear_screen()

                                ui.display_goodbye_logo(goodbye_logo_list_of_list)
                                ui.display_credits(credits_board_list_of_list)  
                                sys.exit(0)                      

                if PLAYER_SCORE >= 4 and HEALTH > 0:
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
                        key = input()
                        if key == "y":
                            helpers.clear_screen()
                            # HOW TO PLAY                        
                            turn_game.how_to_play()
                            is_running_fight = True
                            while is_running_fight:
                                turn_game.fighting_boss(character, HEALTH)
                                is_running_fight = False
                        
                                # creates time after game, and highscores2.txt
                                time_after_the_game = helpers.time_after_the_game(starttime)
                                creating_highscore_file_after_wining(input_name, PLAYER_SCORE, time_after_the_game)
                            is_running_third_lvl = False
                        elif key == 'n':
                            # save to file
                            is_running_third_lvl = False
                            
                    if HEALTH > 1:      # This HEALTH should be vaildated after turn_game, but turn_game nothing returns so it cant know who won!
                        helpers.clear_screen()
                        # save to file
                        ui.display_you_won_logo(you_won_logo_list_of_list)
                        time.sleep(4)
                        helpers.clear_screen()
                        ui.display_goodbye_logo(goodbye_logo_list_of_list)
                        ui.display_credits(credits_board_list_of_list)

                        board_from_file = engine.create_board_out_of_file(FILE_PATH)              # ACTUAL VERSION ---> WORKS, BUT IT IS FROM FILE, AND DONT HIDE DOLLAR SIGN
                        board = copy.deepcopy(board_from_file)
                        continue

                # if HEALTH < 1:       # HEALTH < 1
                #     ui.print_text("You lost")
                #     input_ask = input('Do you want to START AGAIN a game? (y/n): ')
                #     if input_ask == "y":
                #         is_running_third_lvl = False
                #     elif input_ask == "n":
                #         ui.print_text("Good bye")
                #         sys.exit(0)                    
            elif HEALTH < 1:      # HEALTH < 1
                ui.blank_line()
                helpers.clear_screen()
                ui.print_text("You lost")
                input_ask = input('Do you want to START AGAIN a game? (y/n): ')
                if input_ask == "y":
                    board_from_file = engine.create_board_out_of_file(FILE_PATH)              # ACTUAL VERSION ---> WORKS, BUT IT IS FROM FILE, AND DONT HIDE DOLLAR SIGN
                    board = copy.deepcopy(board_from_file)
                    is_running_third_lvl = False
                    continue
                elif input_ask == "n":
                    helpers.clear_screen()
                    ui.display_goodbye_logo(goodbye_logo_list_of_list)
                    ui.display_credits(credits_board_list_of_list)             
                    sys.exit(0)    
    

if __name__ == '__main__':
    main()