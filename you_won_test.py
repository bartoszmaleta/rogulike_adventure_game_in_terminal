import engine as engine
import ui as ui


FILE_PATH_OF_YOU_WON = "you_won.txt"
you_won_logo_list_of_list = engine.create_board_out_of_file(FILE_PATH_OF_YOU_WON)
ui.display_you_won_logo(you_won_logo_list_of_list)