from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.gameobject import *

from utils.variables import window, keyboard, mouse, menu
from utils.variables import start, options, leave, start1, options1, leave1

window = window

while True:
    if keyboard.key_pressed("ESC"):
        window.close()
    
    menu.draw()
    start.draw()
    options.draw()
    leave.draw()

    if mouse.is_over_object(start):
        start1.draw()
    if mouse.is_over_object(options):
        options1.draw()
    if mouse.is_over_object(leave):
        leave1.draw()     
    
    window.update()