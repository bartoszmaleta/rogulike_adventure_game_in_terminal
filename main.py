import helpers as helpers
import engine as engine
import ui as ui
# import operator
import inventory_controller as inventory_controller
import chest as chest
# import map_manager as map_manager


PLAYER_ICON = '@'
PLAYER_START_X = 4
PLAYER_START_Y = 13
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
    player["score"] = PLAYER_SCORE       # NEW, NOT USED
    return player


def change_player_position(board, player, key):
    player_x = player["x"]
    player_y = player["y"]
    player_inv = player["inventory"]
    player_score = player["score"]       # NEW, NOT USED

    if key in "wasd":
        if key == "w":
            player_new_y_position = player["y"] - 1
            player_old_y_position = player["y"]

            if board[player_new_y_position][player_x] == "X":
                return player, board
            elif board[player_new_y_position][player_x] == "o":
                return player, board
            elif board[player_new_y_position][player_x] == "O":
                return player, board
            elif board[player_new_y_position][player_x] == "'":
                return player, board
            elif board[player_new_y_position][player_x] == "$":
                player["y"] = player["y"] - 1
                inventory_controller.add_to_inventory(player_inv, chest.chest_inventory)
                # engine.adding_score(player_score, 2)       # NEW, NOT USED
                player_score += 1       # NEW, NOT USED
                player["score"] = player["score"] + 1       # NEW, NOT USED
                return player, board
            elif board[player_new_y_position][player_x] == "." or "|" or "=":
                player["y"] = player["y"] - 1
                if board[player_old_y_position][player_x] == "$":
                    board[player_old_y_position][player_x] = "."
                return player, board
            return player, board

        elif key == "s":
            player_new_y_position = player["y"] + 1
            player_old_y_position = player["y"]

            if board[player_new_y_position][player_x] == "X":
                return player, board
            elif board[player_new_y_position][player_x] == "o":
                return player, board
            elif board[player_new_y_position][player_x] == "O":
                return player, board
            elif board[player_new_y_position][player_x] == "'":
                return player, board
            elif board[player_new_y_position][player_x] == "$":
                player["y"] = player["y"] + 1
                inventory_controller.add_to_inventory(player_inv, chest.chest_inventory)
                return player, board
            elif board[player_new_y_position][player_x] == "." or "|" or "=":
                player["y"] = player["y"] + 1
                if board[player_old_y_position][player_x] == "$":
                    board[player_old_y_position][player_x] = "."
                return player, board
            return player, board

        elif key == "a":
            player_new_x_position = player["x"] - 1
            player_old_x_position = player["x"]

            if board[player_y][player_new_x_position] == "X":
                return player, board
            elif board[player_y][player_new_x_position] == "o":
                return player, board
            elif board[player_y][player_new_x_position] == "O":
                return player, board
            elif board[player_y][player_new_x_position] == "'":
                return player, board
            elif board[player_y][player_new_x_position] == "$":
                player["x"] = player["x"] - 1
                inventory_controller.add_to_inventory(player_inv, chest.chest_inventory)
                return player, board
            elif board[player_y][player_new_x_position] == "." or "|" or "=":
                player["x"] = player["x"] - 1
                if board[player_y][player_old_x_position] == '$':
                    board[player_y][player_old_x_position] = '.'
                return player, board
            return player, board

        elif key == "d":
            player_new_x_position = player["x"] + 1
            player_old_x_position = player["x"]

            if board[player_y][player_new_x_position] == "X":
            # if board[player_y][player_new_x_position] == "X" or "o" or "O" or "-" or "/" or "\\" or "#" or "*":
                return player, board
            elif board[player_y][player_new_x_position] == "o":
                return player, board
            elif board[player_y][player_new_x_position] == "O":
                return player, board
            elif board[player_y][player_new_x_position] == "'":
                return player, board
            elif board[player_y][player_new_x_position] == "$":
                player["x"] = player["x"] + 1
                inventory_controller.add_to_inventory(player_inv, chest.chest_inventory)
                return player, board
            elif board[player_y][player_new_x_position] == "." or "|" or "=":
                player["x"] = player["x"] + 1
                if board[player_y][player_old_x_position] == '$':
                    board[player_y][player_old_x_position] = '.'
                return player, board
            return player, board

    return player, board


def copy_board(board):      # NEW, NOT USED
    board = board.copy()
    return board


def main():
    FILE_PATH = "map_visual.txt"
    FILE_PATH_OF_LABIRYNTH = "labirynth.txt"
    player = create_player()
    player_inv = player["inventory"]
    player_score = player["score"]       # NEW, NOT USED
    print(player_score)       # NEW, NOT USED
    print(type(player_score))       # NEW, NOT USED
    # board_out_of_file = engine.create_board_out_of_file(FILE_PATH)        # NEW, NOT USED
    is_running = True
    # board = copy_board(board_out_of_file)       # NEW, NOT USED

    while is_running:
        key = helpers.key_pressed()
        if key == 'q':
            is_running = False

        else:
            # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)        # OLD VERSION ---> simple rectangle board out of algorithm
            board = engine.create_board_out_of_file(FILE_PATH)              # ACTUAL VERSION ---> WORKS, BUT IT IS FROM FILE, AND DONT HIDE DOLLAR SIGN
            # board = engine.create_board_out_of_file(FILE_PATH_OF_LABIRYNTH)           # TO GET LABIRYNTH VERSION, JUST UNCOMMENT THIS LINE, AND COMMENT LINE 169
            # COPY BOARD AND USE IT FURTHER                                 NEW, NOT USED
            # board = board
            # board = board_out_of_file.copy()                              NEW, NOT USED
            # player = change_player_position(board, player, key)           # without second return!!!
            player, board = change_player_position(board, player, key)
            board = engine.put_player_on_board(board, player)
            ui.display_board(board)
            ui.print_table(player_inv, 'count,desc')
            # print('score : ', player_score)       # NEW, NOT USED
            # ui.print_score_of_player(player_score)       # NEW, NOT USED


if __name__ == '__main__':
    main()