from PIL import Image, ImageGrab
from pynput.mouse import Button, Controller
from pynput import keyboard

done = False
active = False

def on_press(key):
    print(key)
    if key.char == 's':
        print('Script is started')
        active = True
    if key.char == 'p':
        print('Script is paused')
        active = False
    # if key.char == 's':
    #     print('Exiting')
    #     done = True
def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
while not done:
    if active:
        pass
