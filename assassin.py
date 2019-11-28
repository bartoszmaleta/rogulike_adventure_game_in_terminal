import engine as engine
import ui as ui


FILE_PATH_OF_ASSASIN = "assassin.txt"
assasin_board = engine.create_board_out_of_file(FILE_PATH_OF_ASSASIN)
ui.display_warrior(assasin_board)