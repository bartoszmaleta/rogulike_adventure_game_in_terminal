import engine as engine
import ui as ui


FILE_PATH_OF_GOODBYE_LOGO = "goodbye_logo.txt"
menu_title_board = engine.create_board_out_of_file(FILE_PATH_OF_GOODBYE_LOGO)
ui.display_goodbye_logo(menu_title_board)
