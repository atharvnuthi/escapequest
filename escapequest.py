from random import *
from variables import window, key, mouse, state, som, gameRun, telas, numCenas, iCena #main
from variables import menuFundo, start, options, leave, start1, options1, leave1 #menu
from variables import soundOn, soundOff, soundOn1, soundOff1, easy, medium, hard, easy1, medium1, hard1, optionsFundo, strLevel, strSound #options
from time import sleep #options
from variables import personagem, velPersonagem #personagem
from variables import potes, pCenas, pIndexes, allQuestions, allAnswers, optionLetters, qTime, textOptions, textQuestions, phrasesW, timer, qAnswered, qChoices #Q&A

def escapeUtilResetGame(gR, iC):
    global gameRun, iCena, personagem
    iCena = iC
    gameRun = gR
    personagem.set_position((window.width - personagem.width) / 2, window.height - personagem.height - 150)

def escapeQuestMenu():
    global state
    while state == True:
        menuFundo.draw()
        start.draw()
        options.draw()
        leave.draw()

        if mouse.is_over_object(start):
            start1.draw()
            if mouse.is_button_pressed(1):
                escapeUtilResetGame(True, 0)
                escapeQuestGame()

        if mouse.is_over_object(options):
            options1.draw()
            if mouse.is_button_pressed(1):
                escapeQuestOptions()

        if mouse.is_over_object(leave):
            leave1.draw()
            if mouse.is_button_pressed(1):
                state = False    
        
        window.update()

def escapeQuestQuestion():
    global qAnswered, qChoices, qTime, phrasesW
    
    #get random question which hasn't been answered yet
    qIndex = randint(0, len(allQuestions) - 1)
    while(qIndex not in qChoices):
        qIndex = randint(0, len(allQuestions) - 1)
    qChoices.remove(qIndex)
    tTime = qTime

    while True:
        tTime -= 1 * window.delta_time()

        window.set_background_color((0, 0, 0))
        window.draw_text(textQuestions[qIndex], x=(window.width - (len(textQuestions[qIndex]) * 15.6)) / 2, y=200, size=26, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
        window.draw_text(optionLetters[0] + textOptions[qIndex][0], x=(window.width - (len(textOptions[qIndex][0]) * 15)) / 2, y=260, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
        window.draw_text(optionLetters[1] + textOptions[qIndex][1], x=(window.width - (len(textOptions[qIndex][0]) * 15)) / 2, y=290, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
        window.draw_text(optionLetters[2] + textOptions[qIndex][2], x=(window.width - (len(textOptions[qIndex][0]) * 15)) / 2, y=320, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
        window.draw_text(str(int(tTime)), x=window.width - 60, y=window.height - 40, size=25, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
        timer.draw()

        if tTime < 0:
            window.draw_text(phrasesW[1], x=20, y=window.height-40, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
            window.update()
            sleep(2)
            break

        if key.key_pressed("A"):
            if allAnswers[qIndex] == textOptions[qIndex][0]:
                window.draw_text(phrasesW[2], x=20, y=window.height-40, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
                window.update()
                qAnswered += 1
            elif allAnswers[qIndex] != textOptions[qIndex][0]:
                window.draw_text(phrasesW[0], x=20, y=window.height-40, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
                window.update()
            sleep(2)
            break
        
        if key.key_pressed("B"):
            if allAnswers[qIndex] == textOptions[qIndex][1]:
                window.draw_text(phrasesW[3], x=20, y=window.height-40, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
                window.update()
                qAnswered += 1
            elif allAnswers[qIndex] != textOptions[qIndex][1]:
                window.draw_text(phrasesW[0], x=20, y=window.height-40, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
                window.update()
            sleep(2)
            break
                    
        if key.key_pressed("C"):
            if allAnswers[qIndex] == textOptions[qIndex][2]:
                window.draw_text(phrasesW[2], x=20, y=window.height-40, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
                window.update()
                qAnswered += 1
            elif allAnswers[qIndex] != textOptions[qIndex][2]:
                window.draw_text(phrasesW[0], x=20, y=window.height-40, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
                window.update()
            sleep(2)
            break

        window.update()
    return

def escapeQuestGame():
    global gameRun, iCena, potes, pCenas, pIndexes, qChoices

    while gameRun == True:
        if key.key_pressed("ESC"):
            escapeUtilResetGame(False, 0)

        # Movimentação do personagem
        if key.key_pressed("RIGHT"):
            personagem.set_sequence(0, 2, True)
            personagem.update()
            personagem.x += velPersonagem * window.delta_time()
        if key.key_pressed("LEFT"):
            personagem.set_sequence(2, 4, True)
            personagem.update()
            personagem.x -= velPersonagem * window.delta_time()

        # Condições para o personagem não sair da tela e para mudar de cena quando chegar no final da tela
        if personagem.x > window.width:
            personagem.x = 0
            iCena += 1
        if personagem.x < 0:
            if iCena != 0:
                personagem.x = window.width
                iCena -= 1
            elif iCena == 0:
                personagem.x = 0 

        if iCena == numCenas: #& qAnswered == numPotes
            escapeQuestWinner()
            escapeUtilResetGame(False, 0)
            return

        if iCena < numCenas:
            telas[iCena].draw()
        
        if iCena in pCenas:
            if(len(potes) > 0):
                potes[0].draw()
                if personagem.collided(potes[0]):
                    escapeQuestQuestion()
                    potes[0].hide()
                    pCenas.remove(iCena)
                    potes.pop(0)

        personagem.draw()
        window.update()

def escapeQuestWinner():
    while True:
        if key.key_pressed("ESC") or key.key_pressed("ENTER"):
            return
        
        window.set_background_color((0, 0, 0))
        window.draw_text("Yay, you won!!!", x=window.width/2, y=window.height/2, size=50, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
        window.update()

def escapeQuestOptions():
    global som, velPersonagem
    global strSound, strLevel

    while True:
        if key.key_pressed("ESC") or key.key_pressed("ENTER"):
            return
        
        optionsFundo.draw()
        easy.draw()
        medium.draw()
        hard.draw()
        soundOn.draw()
        soundOff.draw()
        
        if mouse.is_over_object(easy):
            easy1.draw()
            if mouse.is_button_pressed(1):
                velPersonagem = 550
                strLevel = "Easy"
        
        if mouse.is_over_object(medium):
            medium1.draw()
            if mouse.is_button_pressed(1):
                velPersonagem = 500
                strLevel = "Medium"
            
        if mouse.is_over_object(hard):
            hard1.draw()
            if mouse.is_button_pressed(1):
                velPersonagem = 450
                strLevel = "Hard"
        
        if mouse.is_over_object(soundOn):
            soundOn1.draw()
            if mouse.is_button_pressed(1):
                som = True
                strSound = "On"
        
        if mouse.is_over_object(soundOff):
            soundOff1.draw()
            if mouse.is_button_pressed(1):
                som = False
                strSound = "Off"
        
        window.draw_text("Level: {}".format(strLevel), x=window.width - 200, y=window.height - 75, size=20, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
        window.draw_text("Sound: {}".format(strSound), x=window.width - 200, y=window.height - 50, size=20, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
        window.update()

while state == True:
    escapeQuestMenu()