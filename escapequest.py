from variables import window, key, mouse, state, som, gameRun
from variables import menuFundo, start, options, leave, start1, options1, leave1, strLevel, strSound
from variables import soundOn, soundOff, soundOn1, soundOff1, easy, medium, hard, easy1, medium1, hard1, optionsFundo
from variables import personagem, velPersonagem, telas, numCenas, potes, iCena, pp, pi, numPotes
from variables import questions, answers, optionLetters, qTimeAux, qOptions, qPhrases, qChoices, triesImg, timer

def escapeUtilResetGame(gR, iC):
    global gameRun, iCena, personagem
    iCena = iC
    gameRun = gR
    personagem.set_position((window.width - personagem.width) / 2, window.height - personagem.height - 150)

def escapeUtilPotes(pp, pi, iCena, potes, personagem):
    if iCena == pp:
        potes[pi].draw()
        if personagem.collided(potes[pi]):
            escapeQuestQuestion(pi)

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

def escapeQuestGame():
    global iCena, potes, pp, pi, gameRun

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

        if iCena == numCenas:
            escapeUtilResetGame(False, 0)
            escapeQuestWinner()

        if iCena < numCenas:
            telas[iCena].draw() 
        
        for i in range(numPotes):
            escapeUtilPotes(pp[i], pi[i], iCena, potes, personagem)

        personagem.draw()
        window.update()

def escapeQuestWinner():
    while True:
        if key.key_pressed("ESC"):
            return
        
        window.set_background_color((0, 0, 0))
        window.draw_text("Yay, you won!!!", x=window.width/2, y=window.height/2, size=50, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
        window.update()

def escapeQuestQuestion(pi):
    global qTimeAux
    
    while True:
        if qTimeAux <= 9:
            return
        qTimeAux -= 0.75 * window.delta_time()

        window.set_background_color((0, 0, 0))
        window.draw_text(qPhrases[qChoices[pi]], x=window.width / 2 - 290, y=180, size=26, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
        window.draw_text(optionLetters[0] + qOptions[pi][0], x=window.width / 2 - 75, y=30*0+240, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
        window.draw_text(optionLetters[1] + qOptions[pi][1], x=window.width / 2 - 75, y=30*1+240, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
        window.draw_text(optionLetters[2] + qOptions[pi][2], x=window.width / 2 - 75, y=30*2+240, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
        window.draw_text(str(int(qTimeAux)), x=window.width - 60, y=window.height - 40, size=20, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
        
        for i in triesImg:
            i.draw()
        timer.draw()
        window.update()

def escapeQuestOptions():
    global som, velPersonagem
    global strSound, strLevel

    while True:
        if key.key_pressed("ESC"):
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