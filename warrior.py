import engine as engine
import ui as ui


FILE_PATH_OF_WIZARD = "warrior.txt"
warrior_board = engine.create_board_out_of_file(FILE_PATH_OF_WIZARD)
ui.display_warrior(warrior_board)

