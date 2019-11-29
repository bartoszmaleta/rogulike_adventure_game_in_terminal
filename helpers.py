import time as time


def key_pressed():
    import sys

    try:
        import tty, termios
    except ImportError:
    # Probably Windows.
        try:
            import msvcrt
        except ImportError:
            # FIXME what to do on other platforms?
            # Just give up here.
            raise ImportError('getch not available')
        else:
            key = msvcrt.getch().decode('utf-8')
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def clear_screen():
    import os

    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def time_after_the_game(starttime):
    time_after_loosing = time.time()
    time_of_the_game_no_round_after_losing = time_after_loosing - starttime
    time_of_the_game_after_losing = round(time_of_the_game_no_round_after_losing, 2)
    # print('Your time in this round: ', time_of_the_game_after_losing)
    # datetime_object_after_losing = time.asctime(time.localtime(time.time()))

    return time_of_the_game_after_losing