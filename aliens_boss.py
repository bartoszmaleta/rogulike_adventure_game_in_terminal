import engine as engine
import ui as ui


FILE_PATH_OF_BOSS_ALIEN = "alien_boss.txt"
alien_board = engine.create_board_out_of_file(FILE_PATH_OF_BOSS_ALIEN)
ui.display_alien_boss(alien_board)