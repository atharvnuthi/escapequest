from random import *
from variables import window, key, mouse, state, som, gameRun, telas, numCenas, iCena #main
from variables import menuFundo, start, options, leave, start1, options1, leave1 #menu
from variables import soundOn, soundOff, soundOn1, soundOff1, easy, medium, hard, easy1, medium1, hard1, optionsFundo, strLevel, strSound #options
from variables import personagem, velPersonagem
from variables import potes, pCenas, pIndexes, numPotes, questions, answers, optionLetters, qTime, qRedirect, qOptions, qQuestions, triesImg, phrasesW, timer, qDone, qAnswered, qTotal #Q&A

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

def escapeQuestGame():
    global gameRun, iCena, potes, pCenas, pIndexes, qDone

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
            escapeUtilResetGame(False, 0)
            escapeQuestWinner()
            return

        if iCena < numCenas:
            telas[iCena].draw()
        
        for i in range(numPotes):
            if iCena == pCenas[i] & i not in qDone:
                potes[pIndexes[i]].draw()
                if personagem.collided(potes[pIndexes[i]]):
                    escapeQuestQuestion()
                    potes[pIndexes[i]].hide()

        personagem.draw()
        window.update()

def escapeQuestWinner():
    while True:
        if key.key_pressed("ESC") or key.key_pressed("ENTER"):
            return
        
        window.set_background_color((0, 0, 0))
        window.draw_text("Yay, you won!!!", x=window.width/2, y=window.height/2, size=50, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
        window.update()

def escapeQuestQuestion():
    global qDone, qTotal, qAnswered

    # Verifica se a pergunta já foi feita
    qIndex = randint(0, len(questions) - 1)
    if qIndex in qDone:
        qIndex = randint(0, len(questions) - 1)
    else:
        qDone.append(qIndex)

    qTotal += 1
    
    tTime = qTime  # Tempo para responder a pergunta
    tRedirect = qRedirect  # Tempo para redirecionar a tela quando acertar ou perder as tentativas
    aux = True # Auxiliar para verificar se a resposta está correta
    aux_2 = True # Auxiliar para verificar se o tempo acabou e redirecionar a tela para o jogo

    while True:
        # Verifica se possui tentativas
        if len(triesImg) > 0 and qTotal <= 2:
            tTime -= 1 * window.delta_time()

            window.set_background_color((0, 0, 0))
            window.draw_text(qQuestions[qIndex], x=(window.width - (len(qQuestions[qIndex]) * 15.6)) / 2, y=200, size=26, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
            window.draw_text(optionLetters[0] + qOptions[qIndex][0], x=(window.width - (len(qOptions[qIndex][0]) * 15)) / 2, y=260, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
            window.draw_text(optionLetters[1] + qOptions[qIndex][1], x=(window.width - (len(qOptions[qIndex][0]) * 15)) / 2, y=290, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
            window.draw_text(optionLetters[2] + qOptions[qIndex][2], x=(window.width - (len(qOptions[qIndex][0]) * 15)) / 2, y=320, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
            window.draw_text(str(int(tTime)), x=window.width - 60, y=window.height - 40, size=25, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)

            # Condição para o tempo de resposta
            if tTime <= 0 and aux == True:
                triesImg.pop(len(triesImg) - 1)
                aux = False

            if key.key_pressed("A") and aux == True and aux_2 == True:
                if answers[qIndex] == qOptions[qIndex][0]:
                    aux_2 = False
                    qAnswered += 1
                else:
                    triesImg.pop(len(triesImg) - 1)
                    aux = False

            if key.key_pressed("B") and aux == True and aux_2 == True:
                if answers[qIndex] == qOptions[qIndex][1]:
                    aux_2 = False
                    qAnswered += 1
                else:
                    triesImg.pop(len(triesImg) - 1)
                    aux = False

            if key.key_pressed("C") and aux == True and aux_2 == True:
                if answers[qIndex] == qOptions[qIndex][2]:
                    aux_2 = False
                    qAnswered += 1
                else:
                    triesImg.pop(len(triesImg) - 1)
                    aux = False

            if key.key_pressed("A") == False and key.key_pressed("B") == False and key.key_pressed("C") == False:
                # Se errar a pergunta, chama a função com uma nova pergunta
                if aux == False:
                    tRedirect -= 1 * window.delta_time()
                    window.set_background_color((0, 0, 0))
                    window.draw_text(phrasesW[2], x=(window.width / 2) - 180, y=window.height / 2, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)

                    if tTime <= 0:
                        window.draw_text(phrasesW[1], x=(window.width / 2) - 130, y=window.height/2-60, size=30, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
                    else:
                        window.draw_text(phrasesW[0], x=(window.width / 2) - 275, y=window.height/2-60, size=30, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)

                    if tRedirect <= 0:
                        aux = True
                        escapeQuestQuestion()

                # Se acertar, chama a função com uma nova pergunta
                if aux_2 == False:
                    aux_2 = True
                    escapeQuestQuestion()

            for i in triesImg:
                i.draw()
            timer.draw()

        else:
            tRedirect -= 1 * window.delta_time()
            window.set_background_color((239, 111, 60))

            if len(triesImg) == 0:
                window.draw_text(phrasesW[3], x=window.width / 2 - 300, y=window.height/2 - 26, size=36, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
            else:
                window.draw_text(phrasesW[4], x=window.width / 2 - 110, y=window.height/2 - 86, size=36, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
                window.draw_text("Acertou " + str(qAnswered) + " repostas", x=window.width / 2 - 155, y=window.height/2 - 26, size=28, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
                if qAnswered == 5:
                    window.draw_text(phrasesW[5], x=window.width / 2 - 135, y=window.height/2 + 16, size=28, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
                else:
                    window.draw_text(phrasesW[6], x=window.width / 2 - 135, y=window.height/2 + 16, size=28, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)

            window.draw_text("Redireciondano em " + str(int(tRedirect) + 1), x=20, y=window.height - 25, size=16, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
            
            if tRedirect < 0:
                escapeQuestGame()

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