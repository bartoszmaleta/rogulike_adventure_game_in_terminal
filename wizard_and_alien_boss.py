import engine as engine
import ui as ui


FILE_PATH_OF_WIZARD_AND_ALIEN_BOSS = "wizard_and_alien_boss.txt"
wizard_and_alien_boss_board = engine.create_board_out_of_file(FILE_PATH_OF_WIZARD_AND_ALIEN_BOSS)
ui.display_wizard_and_alien_boss(wizard_and_alien_boss_board)