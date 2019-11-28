import engine as engine
import ui as ui

character = '''
    " "                                     
     "       A                          |
     |      /_\                         |       
     |     | ..|                        |
     |   __\ ^^/_                       |
     @====#######\                      |
          |# * #|\\                      |      
          /# * #\ \\                     |
         |#  *  #|                      |
         /#  *  #\                      |      
        /#   *   #\                     |
'''



print(character)
FILE_PATH_OF_WIZARD = "wizard.txt"
wizard_board = engine.create_board_out_of_file(FILE_PATH_OF_WIZARD)
ui.display_wizard(wizard_board)