from variables import window, key, mouse, state, som
from variables import menuFundo, start, options, leave, start1, options1, leave1, strLevel, strSound
from variables import soundOn, soundOff, soundOn1, soundOff1, easy, medium, hard, easy1, medium1, hard1, optionsFundo
from variables import personagem, velPersonagem, telas, numCenas, potes, iCena, pp1, pp2, pp3, pi1, pi2, pi3
from variables import questions, answers, triesImg, timer, optionLetters, usedQuestions, qTimeAux
from random import randint

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

def escapeQuestUtil(pp, pi, iCena, potes, personagem):
    if iCena == pi:
        potes[pp].draw()
        if personagem.collided(potes[pp]):
            escapeQuestQuestion()

def escapeQuestGame():
    global state, iCena, potes, pi1, pi2, pi3, pp1, pp2, pp3
    pIndex = randint(0, 2)

    while state == True:
        if key.key_pressed("ESC"):
            return

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
            window.draw_text("Yay, you won!!!", x=window.width/2, y=window.height/2, size=150, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
            personagem.hide()  

        if iCena < numCenas:
            telas[iCena].draw() 
        
        escapeQuestUtil(pp1, pi1, iCena, potes, personagem)
        escapeQuestUtil(pp2, pi2, iCena, potes, personagem)
        escapeQuestUtil(pp3, pi3, iCena, potes, personagem)

        personagem.draw()
        window.update()

def escapeQuestQuestion():
    global state, questions, answers, usedQuestions, optionLetters, qTimeAux
    
    qIndex = randint(0, len(questions) - 1)
    qSplit = questions[qIndex].split("? ")
    qPhrase = qSplit[0] + "?"
    qOptions = qSplit[1].split(",")
    tries = []

    if qIndex in usedQuestions:
        qIndex = randint(0, len(questions) - 1)
    else:
        usedQuestions.append(qIndex)
        qSplit = questions[qIndex].split("? ")
        qPhrase = qSplit[0] + "?"
        qOptions = qSplit[1].split(",")

    while state == True:
        if qTimeAux <= 0:
            return
        if key.key_pressed("ESC"):
            return
        qTimeAux -= 0.75 * window.delta_time()

        if key.key_pressed("A"):
            if qOptions[0] == answers[qIndex]:
                return
        if key.key_pressed("B"):
            if qOptions[1] == answers[qIndex]:
                return
        if key.key_pressed("C"):
            if qOptions[2] == answers[qIndex]:
                return

        window.set_background_color((0, 0, 0))
        window.draw_text(qPhrase, x=window.width / 2 - 290, y=180, size=26, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
        A = window.draw_text(optionLetters[0] + qOptions[0], x=window.width / 2 - 75, y=30*0+240, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
        B = window.draw_text(optionLetters[1] + qOptions[1], x=window.width / 2 - 75, y=30*1+240, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
        C = window.draw_text(optionLetters[2] + qOptions[2], x=window.width / 2 - 75, y=30*2+240, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
        window.draw_text(str(int(qTimeAux)), x=window.width - 60, y=window.height - 40, size=20, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
        
        for i in triesImg:
            i.draw()
        timer.draw()
        window.update()

def escapeQuestOptions():
    global state, som, velPersonagem
    global strSound, strLevel

    while state == True:
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