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
fundo_game = GameImage("assets/images/fundo_jogo.png")

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

personagem_inicio = Sprite("assets/images/objects/cientista_inicio.png")
personagem_inicio.set_position((window.width - personagem_inicio.width) / 2, 430)
personagem = Sprite("assets/images/objects/cientista_jogo.png")
personagem.set_position((window.width - personagem_inicio.width) / 2, 430)

bowl_1 = Sprite("assets/images/objects/pt1.png")
bowl_1.set_position(170, 300)
bowl_2 = Sprite("assets/images/objects/pt2.png")
bowl_2.set_position(642, 200)
bowl_3 = Sprite("assets/images/objects/pt3.png")
bowl_3.set_position(950, 400)

life_puzzle = Sprite("assets/images/objects/vida.png")
life_puzzle.set_position(10, window.height - life_puzzle.height - 10)

life_player = Sprite("assets/images/objects/barra_vida.png")
life_player.set_position(window.width - life_player.width - 30, 10)

thorns = Sprite("assets/images/objects/espinho.png")
thorns.set_position(window.width / 2 + 200, window.height - thorns.height)
fire = Sprite("assets/images/objects/fogo.png")
fire.set_position(300, window.height - fire.height)