from pyco import *
from pyco.color import Fore
from pyco import cursor
from time import sleep
import this

print(Fore.BRIGHT_GREEN, end='', flush=True)
sleep(2)
cursor.line_up(5)
sleep(0.5)
print("Up 5 lines", end='', flush=True)
sleep(0.5)
cursor.right(5)
sleep(0.5)
print("Right 5 characters", end='', flush=True)
sleep(0.5)
cursor.up(1)
sleep(0.5)
print("Up 1 character", end='', flush=True)
sleep(0.5)
cursor.down(2)
sleep(0.5)
print("Down 2 characters", end='', flush=True)
sleep(0.5)
cursor.left(50)
sleep(0.5)
print("Left 50 characters", end='', flush=True)
sleep(0.5)
cursor.line_up(9)
sleep(0.5)
print("Up 9 lines ", end='', flush=True)
sleep(0.5)
cursor.save_position()
sleep(0.5)
print("Saved position", end='', flush=True)
sleep(0.5)
cursor.line_down(2)
sleep(0.5)
print("Down 2 lines", end='', flush=True)
sleep(0.5)
cursor.horizontal(28)
sleep(0.5)
print("X position 28", end='', flush=True)
sleep(0.5)
cursor.vertical(8)
sleep(0.5)
print("Y position 8", end='', flush=True)
sleep(0.5)
cursor.set_position(11, 2)
sleep(0.5)
print("X position 11, Y position 2", flush=True)
sleep(0.5)
cursor.hide()
sleep(0.5)
print("cursor hidden", flush=True)
sleep(2)
cursor.show()
sleep(0.5)
print("cursor visible", flush=True)
sleep(2)
cursor.disable_blink()
sleep(0.5)
print("cursor blink disabled", flush=True)
sleep(2)
cursor.enable_blink()
sleep(0.5)
print("cursor blink enabled", flush=True)
sleep(2)
print("cursor position is: " + str(cursor.get_position()), flush=True)
sleep(0.5)
cursor.restore_position()
sleep(0.5)
print("cursor position restored to previous saved position", flush=True)
