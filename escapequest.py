from time import sleep #options
from variables import *

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
    qQuestion = []
    qIndex = randint(0, len(allQuestions) - 1)
    while qIndex not in qQuestion:
        qQuestion.append(qIndex)
    tTime = qTime

    ponto = 0

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
                ponto = 1
            elif allAnswers[qIndex] != textOptions[qIndex][0]:
                window.draw_text(phrasesW[0], x=20, y=window.height-40, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
                ponto = 2
                window.update()
            sleep(2)
            break
        
        if key.key_pressed("B"):
            if allAnswers[qIndex] == textOptions[qIndex][1]:
                window.draw_text(phrasesW[3], x=20, y=window.height-40, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
                window.update()
                ponto = 1
            elif allAnswers[qIndex] != textOptions[qIndex][1]:
                window.draw_text(phrasesW[0], x=20, y=window.height-40, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
                ponto = 2
                window.update()
            sleep(2)
            break
                    
        if key.key_pressed("C"):
            if allAnswers[qIndex] == textOptions[qIndex][2]:
                window.draw_text(phrasesW[2], x=20, y=window.height-40, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
                window.update()
                ponto = 1
            elif allAnswers[qIndex] != textOptions[qIndex][2]:
                window.draw_text(phrasesW[0], x=20, y=window.height-40, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
                ponto = 2
                window.update()
            sleep(2)
            break

        window.update()
    return ponto

def escapeQuestGame():
    global gameRun, iCena, potes, pCenas, pIndexes, qChoices, health, qAnswered, iDemon

    # Define jump-related variables
    pontos = [0]
    p = 0
    isJump = False
    initialJumpVel = -800  # Adjust this value to control the jump height
    jumpVel = 0 
    gravity = 2000
    vertical_velocity = 800  # Adjust this value to control the vertical movement speed
    vel_demon = 75
    vel_nave = 200
    espaco_intervalo = 450
    espaco_intervalo_2 = 800
    rec_tiro_demon = 0
    rec_tiro_nave = 0
    acertou = False
    cont_piscar = 0
    piscar = 0
    f, q = t()
    inicio = True
    tTime = qTime

    while gameRun == True:
        if inicio:
            tTime -= 2.5 * window.delta_time()
            finalFundo.draw()
            window.draw_text(phrasesW[4], x=215, y=window.height/2 - 90, size=40, font_name="monospace", color=(255,145,77), bold=True)
            window.draw_text(phrasesW[5], x=100, y=window.height/2 - 30, size=40, font_name="monospace", color=(255,145,77), bold=True)
            window.draw_text(phrasesW[6], x=window.width/2 - 300, y=window.height-100, size=30, font_name="monospace", color=(255,145,77), bold=True)
            if tTime <= 0:
               inicio = False

        else:

            rec_tiro_demon += window.delta_time() * 0.3
            rec_tiro_nave += window.delta_time() * 0.5
            demon.x += vel_demon * window.delta_time()
            obs_2.x += vel_nave * window.delta_time()

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

            # Gravity logic
            if not isJump:
                personagem.y += gravity * window.delta_time()

                if personagem.y >= window.height - personagem.height - 150:
                    personagem.y = window.height - personagem.height - 150

            # Jumping logic
            if key.key_pressed("UP") and not isJump:
                isJump = True
                jumpVel = initialJumpVel
            if isJump:
                personagem.y += jumpVel * window.delta_time()
                jumpVel += gravity * window.delta_time()
                if personagem.y >= window.height - personagem.height - 150:
                    personagem.y = window.height - personagem.height - 150
                    isJump = False

            # Down logic
            if key.key_pressed("DOWN"):
                personagem.y += vertical_velocity * window.delta_time()

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

            if iCena == numCenas - 1:
                if personagem.x > window.width - personagem.width:
                    personagem.x = window.width - personagem.width

            if iCena < numCenas:
                telas[iCena].draw()

            if iCena == f:
                potes[q].draw()
                if personagem.collided(potes[q]):
                    potes[q].hide()
                    p = escapeQuestQuestion()
                    f, q = t()
                potes[q].unhide()

            if p == 1:
                pontos[0] += 10
                p = 0
            elif p == 2:
                if pontos[0] != 0:
                    pontos[0] -= 5
                    p = 0

            if iCena == iObs_1:
                obs_1.draw()

                if personagem.collided(obs_1):
                    life.pop(len(life) - 1)
                    personagem.set_position(obs_1.x - obs_1.width - 100, window.height - personagem.height - 150)
                    acertou = True

            if iCena == iObs_2:
                obs_2.draw()


                # Verificar se o  ultrapassou o limite esquerdo do intervalo
                if obs_2.x <= 0:
                    vel_nave *= -1

                # Verificar se o  ultrapassou o limite direito do intervalo
                if obs_2.x > window.width - obs_2.width + 10:
                    vel_nave *= -1

                if rec_tiro_nave > 0.9:
                    tiro_nave.set_position(obs_2.x, obs_2.y + 50)
                    tiros_nave.append(tiro_nave)
                    rec_tiro_nave = 0

                for tiro_n in tiros_nave:
                    if tiro_n.collided(personagem):
                        life.pop(len(life) - 1)
                        tiros_nave.remove(tiro_n)
                        acertou = True

                for tiro_n in tiros_nave:
                    if tiro_n.y > window.width:
                        tiros_nave.remove(tiro_n)

                for j in tiros_nave:
                    j.y += 400 * window.delta_time()
                    j.draw()

            if iCena == iDemon:
                demon.draw()
                if personagem.x > demon.x:
                    vel_tiro = 400
                else:
                    vel_tiro = -400

                # Verificar se o demon ultrapassou o limite esquerdo do intervalo
                if demon.x <= demon.width + espaco_intervalo:
                    demon.x = demon.width + espaco_intervalo
                    vel_demon *= -1

                # Verificar se o demon ultrapassou o limite direito do intervalo
                if demon.x >= window.width - demon.width - espaco_intervalo:
                    demon.x = window.width - demon.width - espaco_intervalo
                    vel_demon *= -1

                if rec_tiro_demon > 0.9:
                    tiro.set_position(demon.x, demon.y + 50)
                    tiros_demon.append(tiro)
                    rec_tiro_demon = 0

                for tir in tiros_demon:
                    if tir.collided(personagem):
                        life.pop(len(life) - 1)
                        tiros_demon.remove(tir)
                        acertou = True

                for tir in tiros_demon:
                    if tir.x < 0 or tir.x > window.width:
                        tiros_demon.remove(tir)

                for i in tiros_demon:
                    i.x += vel_tiro * window.delta_time()
                    i.draw()

            if acertou:
                piscar += 2
                if piscar == 100:
                    personagem.hide()
                elif piscar == 150:
                    personagem.unhide()
                    piscar = 0
                    cont_piscar += 1

            if cont_piscar == 5:
                acertou = False
                cont_piscar = 0

            if pontos[0] >= 60 and len(life) > 0:
                escapeQuestWinner()
                escapeUtilResetGame(False, 0)
                return


            window.draw_text("Pontos: " + str(pontos[0]), x=25, y=35, font_name="monospace", size=25, color=(255, 255, 255),bold=True)

            for vida in life:
                vida.draw()

            personagem.draw()

            if len(life) == 0:
                escapeUtilResetGame(False, 0)
                escapeQuestLooser()

        window.update()

def escapeQuestWinner():
    tTime = qTime

    while True:
        if key.key_pressed("ESC") or key.key_pressed("ENTER"):
            return

        tTime -= 2 * window.delta_time()
        
        finalFundo.draw()
        window.draw_text("Yay, you won!!!", x=window.width/2- 200, y=window.height/2, size=50, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)

        if tTime <= 0:
            escapeUtilResetGame(False, 0)
            escapeQuestMenu()

        window.update()


def escapeQuestLooser():
    tTime = qTime

    while True:
        if key.key_pressed("ESC") or key.key_pressed("ENTER"):
            return

        tTime -= 2.5 * window.delta_time()

        finalFundo.draw()
        window.draw_text("Acabaram suas vidas, poxa!", x=300, y=window.height / 2 - 100, size=50,
                         color=(255, 255, 255), font_name="monospace", bold=True, italic=False)

        if tTime <= 0:
            escapeUtilResetGame(False, 0)
            escapeQuestMenu()

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