import helpers as helpers
import engine as engine
import ui as ui
import operator
# import map_manager as map_manager


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


def change_player_position(board, player, key):
    player_x = player["x"]
    player_y = player["y"]
    
    if key in "wasd":
        if key == "w":
            player_new_y_position = player["y"] - 1

            if board[player_new_y_position][player_x] == "X":
                return player
            elif board[player_new_y_position][player_x] == "o":
                return player
            elif board[player_new_y_position][player_x] == "O":
                return player
            elif board[player_new_y_position][player_x] == "'":
                return player
            elif board[player_new_y_position][player_x] == "$":
                player["y"] = player["y"] - 1
                # heeeere!
                return player
            elif board[player_new_y_position][player_x] == "." or "|" or "=":  
                player["y"] = player["y"] - 1

        elif key == "s":
            player_new_y_position = player["y"] + 1

            if board[player_new_y_position][player_x] == "X":
                return player
            elif board[player_new_y_position][player_x] == "o":
                return player
            elif board[player_new_y_position][player_x] == "O":
                return player
            elif board[player_new_y_position][player_x] == "'":
                return player
            elif board[player_new_y_position][player_x] == "." or "|" or "=":
                player["y"] = player["y"] + 1

        elif key == "a":
            player_new_x_position = player["x"] - 1

            if board[player_y][player_new_x_position] == "X":
                return player
            elif board[player_y][player_new_x_position] == "o":
                return player
            elif board[player_y][player_new_x_position] == "O":
                return player
            elif board[player_y][player_new_x_position] == "'":
                return player
            elif board[player_y][player_new_x_position] == "." or "|" or "=":
                player["x"] = player["x"] - 1

        elif key == "d":
            player_new_x_position = player["x"] + 1

            if board[player_y][player_new_x_position] == "X":
            # if board[player_y][player_new_x_position] == "X" or "o" or "O" or "-" or "/" or "\\" or "#" or "*":
                return player
            elif board[player_y][player_new_x_position] == "o":
                return player
            elif board[player_y][player_new_x_position] == "O":
                return player
            elif board[player_y][player_new_x_position] == "'":
                return player
            elif board[player_y][player_new_x_position] == "." or "|" or "=":
                player["x"] = player["x"] + 1
    
    return player


def main():
    FILE_PATH = "map_visual.txt"

    player = create_player()
    player_inv = player["inventory"]

    is_running = True
    
    while is_running:
        key = helpers.key_pressed()
        if key == 'q':
            is_running = False

        else:
            # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)        # OLD VERSION
            board = engine.create_board_out_of_file(FILE_PATH)
            player = change_player_position(board, player, key)
            board = engine.put_player_on_board(board, player)
            ui.display_board(board)
            ui.print_table(player_inv, 'count,desc')


if __name__ == '__main__':
    main()