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
numCenas = 3

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
    potes[i].set_position(randint(pote.width, window.width - pote.width), randint(350, 450))
pp1, pp2, pp3 = sample(range(0, numCenas), 3) #cenas que terão os recipientes
pCenas = [pp1, pp2, pp3] #Lista com os indices das cenas que terão os recipientes
pi1, pi2, pi3 = sample(range(0, numPotes), 3) #recipientes que estarão nas cenas
pIndexes = [pi1, pi2, pi3] #Lista com os indices dos recipientes que estarão nas cenas

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
phrasesW = ["Ops, sua resposta está incorreta!", "O tempo esgotou!", "Muito bem!", "Ganhou 10 pontos!"]

q1, q2, q3 = sample(range(0, len(allQuestions)), 3)
qChoices = [q1, q2, q3] #Lista com os indices das perguntas que serão feitas

# qLifesImg = [] #Lista com as tentativas para responder
# triesLeft = 2
# for i in range(triesLeft):
#     qLifes = Sprite("assets/images/objects/life_puzzle.png")
#     qLifes.set_position(i*10 + (i+1)*qLifes.width - 15, window.height - qLifes.height - 10)
#     qLifesImg.append(qLifes)

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

#for calculating points, health, etc. - to be implemented later on - after all logic is done
qAnswered = 0 # Respostas corretas