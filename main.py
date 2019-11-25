import helpers as helpers
import engine as engine
import ui as ui

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


def change_player_position(player, key):
    if key in "wasd":
        if key == "w":
            player["y"] = player["y"] - 1
        elif key == "s":
            player["y"] = player["y"] + 1
        elif key == "a":
            player["x"] = player["x"] - 1
        elif key == "d":
            player["x"] = player["x"] + 1
    return player


def main():

    player = create_player()

    # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    # board = engine.put_player_on_board(board, player)
    # ui.display_board(board)

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
            player = change_player_position(player, key)
            board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
            board = engine.put_player_on_board(board, player)
            ui.display_board(board)


if __name__ == '__main__':
    main()