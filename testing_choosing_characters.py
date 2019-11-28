import engine as engine 
import ui as ui
FILE_PATH_OF_CHOOSING_CHARACTERS = "choosing_character.txt"
characters_board = engine.create_board_out_of_file(FILE_PATH_OF_CHOOSING_CHARACTERS)
#print(characters_board)
ui.display_choosing_characters(characters_board)
