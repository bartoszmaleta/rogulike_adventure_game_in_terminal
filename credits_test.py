import engine as engine
import ui as ui


FILE_PATH_CREDITS = "credits.txt"
credits_board = engine.create_board_out_of_file(FILE_PATH_CREDITS)
ui.display_credits(credits_board)
