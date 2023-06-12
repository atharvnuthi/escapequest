from PPlay.window import Window
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite
from random import *

WIDTH, HEIGHT = 1300, 650
window = Window(WIDTH, HEIGHT)
window.set_title("Escape Quest")

key = Keyboard()
mouse = Mouse()
state = True
telas = []
potes = []
answer_attempts = []
numCenas = 17
dificuldade = 2 #1 - easy, 2 - medium, 3 - hard
som = True

#Game
for i in range(numCenas):
    fundo = GameImage("assets/images/backgrounds/" + str(i+1) + ".png")
    telas.append(fundo)

#Menu
menuFundo = GameImage("assets/images/backgrounds/menu1.png")

start = Sprite("assets/images/buttons/start.png")
options = Sprite("assets/images/buttons/options.png")
leave = Sprite("assets/images/buttons/leave.png")
start.set_position((window.width-start.width)/2, 180)
options.set_position((window.width-options.width)/2, 260)
leave.set_position((window.width-leave.width)/2, 340)

start1 = Sprite("assets/images/buttons/bStart.png")
options1 = Sprite("assets/images/buttons/bOptions.png")
leave1 = Sprite("assets/images/buttons/bLeave.png")
start1.set_position((window.width-start1.width)/2, 180)
options1.set_position((window.width-options1.width)/2, 260)
leave1.set_position((window.width-leave1.width)/2, 340)

#Options 
optionsFundo = Sprite("assets/images/backgrounds/options.png")

soundOn = Sprite("assets/images/buttons/soundOn.png")
soundOn.set_position(window.width/2 - soundOn.width/2 + 150, window.height/2 - soundOn.height/2 - 80)
soundOff = Sprite("assets/images/buttons/soundOff.png")
soundOff.set_position(window.width/2 - soundOff.width/2 + 150, window.height/2 - soundOff.height/2 + 20)

easy = Sprite('assets/images/buttons/easy.png')
easy1 = Sprite('assets/images/buttons/bEasy.png')
easy.set_position(window.width/2 - easy.width/2 - 150, window.height/2 - easy.height/2 - 105)
easy1.set_position(window.width/2 - easy1.width/2 - 150, window.height/2 - easy1.height/2 - 105)
medium = Sprite('assets/images/buttons/medium.png')
medium1 = Sprite('assets/images/buttons/bMedium.png')
medium.set_position(window.width/2 - medium.width/2 - 150, window.height/2 - medium.height/2 - 30)
medium1.set_position(window.width/2 - medium1.width/2 - 150, window.height/2 - medium1.height/2 - 30)
hard = Sprite('assets/images/buttons/hard.png')
hard1 = Sprite('assets/images/buttons/bHard.png')
hard.set_position(window.width/2 - hard.width/2 - 150, window.height/2 - hard.height/2 + 45)
hard1.set_position(window.width/2 - hard1.width/2 - 150, window.height/2 - hard1.height/2 + 45)

#Objects
personagem = Sprite("assets/images/objects/cientista_jogo_1.png", 4)
personagem.set_position((window.width - personagem.width) / 2, window.height - personagem.height - 150)
personagem.set_total_duration(800)
velPersonagem = 500

# Recipientes
for i in range(3):
    pote = Sprite("assets/images/objects/pt" + str(i+1) + ".png")
    potes.append(pote)
    potes[i].set_position(randint(pote.width, window.width - pote.width), randint(350, 450))

# Arquivo com as perguntas
arq = open("assets/texts/questions.txt", "r", encoding="utf-8")
lines_questions = arq.readlines()

# # Arquivo com as respostas
# arq_a = open("assets/texts/answers.txt")
# lines_answers = arq_a.readlines()

# Tentativas para responder
for i in range(2):
    vida = Sprite("assets/images/objects/life_puzzle.png")
    vida.set_position(i*10 + (i+1)*vida.width - 15, window.height - vida.height - 10)
    answer_attempts.append(vida)

timer = Sprite("assets/images/objects/timer.png")
timer.set_position(window.width - 100, window.height - 50)


