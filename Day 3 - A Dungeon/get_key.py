import sys
import os

if os.name == 'nt':
    import msvcrt

    def get_key():
        return msvcrt.getch().decode().lower()
else:
    import tty
    import termios

    def get_key():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1).lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)