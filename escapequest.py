from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.gameobject import *
from game import tela_jogo

from utils.variables import window, keyboard, mouse, menu
from utils.variables import start, options, leave, start1, options1, leave1

window = window

while True:
    
    menu.draw()
    start.draw()
    options.draw()
    leave.draw()

    if mouse.is_over_object(start):
        start1.draw()
        if mouse.is_button_pressed(1):
            tela_jogo()

    if mouse.is_over_object(options):
        options1.draw()
    if mouse.is_over_object(leave):
        leave1.draw()     
    
    window.update()