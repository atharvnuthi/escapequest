from PPlay.window import Window
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite
from PPlay.animation import *

WIDTH, HEIGHT = 1300, 650
window = Window(WIDTH, HEIGHT)
window.set_title("Escape Quest")

key = Keyboard()
mouse = Mouse()
state = True
telas = []

for i in range(20):
    fundo = GameImage("assets/images/backgrounds/" + str(i+2) + ".png")
    telas.append(fundo)

#Menu
menuFundo = GameImage("assets/images/backgrounds/menu.png")

start = Sprite("assets/images/buttons/start.png")
options = Sprite("assets/images/buttons/options.png")
leave = Sprite("assets/images/buttons/leave.png")
start.set_position((window.width-start.width)/2, 180)
options.set_position((window.width-options.width)/2, 260)
leave.set_position((window.width-leave.width)/2, 340)

start1 = Sprite("assets/images/buttons/start_pink.png")
options1 = Sprite("assets/images/buttons/options_pink.png")
leave1 = Sprite("assets/images/buttons/leave_pink.png")
start1.set_position((window.width-start1.width)/2, 180)
options1.set_position((window.width-options1.width)/2, 260)
leave1.set_position((window.width-leave1.width)/2, 340)

#Objects
personagem = Sprite("assets/images/objects/cientista_jogo.png", 4)
personagem.set_position((window.width - personagem.width) / 2, window.height - personagem.height)
personagem.set_total_duration(800)