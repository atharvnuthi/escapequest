from PPlay.window import Window
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite
from random import randint, sample

WIDTH, HEIGHT = 1300, 650
window = Window(WIDTH, HEIGHT)
window.set_title("Escape Quest")
key = Keyboard()
mouse = Mouse()

#main state
state = True
iCena = 0
som = True
strLevel = "Medium" #Easy/Medium/Hard
strSound = "On" #On/Off
gameRun = True
numCenas = 6

#Personagem Principal
personagem = Sprite("assets/images/objects/cientista_jogo.png", 4)
personagem.set_position((window.width - personagem.width) / 2, window.height - personagem.height - 150)
personagem.set_total_duration(800)
velPersonagem = 500

#Recipientes
potes = [] #Lista com os recipientes
numPotes = 3
for i in range(numPotes):
    pote = Sprite("assets/images/objects/pt" + str(i+1) + ".png")
    potes.append(pote)
    potes[i].set_position(randint(100, 1100), randint(350, 450))

#Obstacles
demon = Sprite("assets/images/objects/demon.png")
demon.set_position(randint(demon.width, window.width - demon.width), window.height - personagem.height - 150)

obs_1 = Sprite("assets/images/objects/obs_1.png")
obs_1.set_position(randint(obs_1.width, window.width - obs_1.width), window.height / 2 + 150)

obs_2 = Sprite("assets/images/objects/obs_2.png")
obs_2.set_position(randint(obs_2.width, window.width - obs_2.width), obs_2.height)

iObs_2, iObs_1, iDemon = 1, 3, 5

#Arquivo com as Perguntas e Respostas
qFile = open("assets/texts/questions.txt", "r", encoding="utf-8")
allQuestions = qFile.readlines()
aFile = open("assets/texts/answers.txt", "r", encoding="utf-8")
allAnswers = aFile.readlines()
for i in range(len(allAnswers)):
    allAnswers[i] = allAnswers[i].split("\n")[0] #Remove o \n do final da linha

textQuestions = [] #Lista com as perguntas
textOptions = [] #Lista com as opções
for i in range(len(allQuestions)): #Separa as perguntas das opções de resposta e guarda em listas diferentes (textQuestions e textOptions)
    qSplit = allQuestions[i].split("? ")
    textQuestions.append(qSplit[0]+"?")
    textOptions.append(qSplit[1].split(","))

optionLetters = ["A - ", "B - ", "C - "] # Letras das opções das perguntas (A, B, C)
phrasesW = ["Ops, sua resposta está incorreta!", "O tempo esgotou!", "Muito bem!", "Ganhou 10 pontos!", "Ajude o cientista a retornar para casa", "respondendo as perguntas e evitando os monstros!", "É necessário alcançar a pontução 60!"]

timer = Sprite("assets/images/objects/timer.png")
timer.set_position(window.width - 100, window.height - 50)
qTime = 11 
# qRedirect = 3

#Game Backgrounds
telas = [] #Lista com as imagens de fundo das cenas
for i in range(numCenas):
    fundo = GameImage("assets/images/backgrounds/" + str(i+1) + ".png")
    telas.append(fundo)
menuFundo = GameImage("assets/images/backgrounds/menu.png")
optionsFundo = Sprite("assets/images/backgrounds/options.png")
finalFundo = Sprite("assets/images/backgrounds/finalizar.png")

#Menu Buttons
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

#Options Buttons
soundOn = Sprite("assets/images/buttons/soundOn.png")
soundOn.set_position(window.width/2 - soundOn.width/2 + 150, window.height/2 - soundOn.height/2 - 80)
soundOff = Sprite("assets/images/buttons/soundOff.png")
soundOff.set_position(window.width/2 - soundOff.width/2 + 150, window.height/2 - soundOff.height/2 + 20)
soundOn1 = Sprite("assets/images/buttons/bSoundOn.png")
soundOn1.set_position(window.width/2 - soundOn1.width/2 + 150, window.height/2 - soundOn1.height/2 - 80)
soundOff1 = Sprite("assets/images/buttons/bSoundOff.png")
soundOff1.set_position(window.width/2 - soundOff1.width/2 + 150, window.height/2 - soundOff1.height/2 + 20)
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

life = []
for i in range(3):
    vida = Sprite("assets/images/objects/life_puzzle.png")
    vida.set_position(i * 10 + (i + 39) * vida.width, 30)
    life.append(vida)

tiro = Sprite("assets/images/objects/tiro_demon.png")
tiro_nave = Sprite("assets/images/objects/tiro_nave.png")
tiros_demon = []
tiros_nave = []

def t():
    pCena = randint(0, numCenas - 1)
    pIndex = randint(0, numPotes - 1)

    return pCena, pIndex