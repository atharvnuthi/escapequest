from PPlay.window import Window
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite

WIDTH, HEIGHT = 1300, 650
window = Window(WIDTH, HEIGHT)
window.set_title("Escape Quest")

keyboard = Keyboard()
mouse = Mouse()

#Menu
menu = GameImage("assets/images/menu.png")

start = Sprite("assets/images/start.png")
options = Sprite("assets/images/options.png")
leave = Sprite("assets/images/leave.png")
start.set_position((window.width-start.width)/2, 180)
options.set_position((window.width-options.width)/2, 260)
leave.set_position((window.width-leave.width)/2, 340)

start1 = Sprite("assets/images/start(1).png")
options1 = Sprite("assets/images/options(1).png")
leave1 = Sprite("assets/images/leave(1).png")
start1.set_position((window.width-start1.width)/2, 180)
options1.set_position((window.width-options1.width)/2, 260)
leave1.set_position((window.width-leave1.width)/2, 340)