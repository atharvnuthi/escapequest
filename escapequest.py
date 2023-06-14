from variables import window, key, mouse, state, dificuldade, som
from variables import menuFundo, start, options, leave, start1, options1, leave1, strLevel, strSound
from variables import soundOn, soundOff, soundOn1, soundOff1, easy, medium, hard, easy1, medium1, hard1, optionsFundo
from variables import personagem, velPersonagem, telas, numCenas, potes
from variables import questions, answers, answerTries, timer
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

def escapeQuestGame():
    global state
    i = 0
    index = randint(0, 2)

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
            i += 1
        if personagem.x < 0:
            if i != 0:
                personagem.x = window.width
                i -= 1
            elif i == 0:
                personagem.x = 0   
        if i == numCenas:
            return

        if potes[index].collided(personagem):
            escapeQuestQuestion()

        telas[i].draw()
        potes[index].draw()
        personagem.draw()
        window.update()


def escapeQuestQuestion():
    global state

    op_letter = ["A - ", "B - ", "C - "] # Letras das opções das perguntas (A, B, C)
    already_used = [] # Guarda os indices das perguntas que já foram usadas
    index = randint(0, len(questions) - 1)
    aux = 11

    if index in already_used:
        index = randint(0, len(questions) - 1)
    else:
        already_used.append(index)
        split_q = questions[index].split("? ")
        phrase = split_q[0] + "?"
        opcoes = split_q[1].split(",")

    while state == True:
        window.set_background_color((0, 0, 0))

        window.draw_text(phrase, x=window.width / 2 - 290, y=180, size=26, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
        A = window.draw_text(op_letter[0] + opcoes[0], x=window.width / 2 - 75, y=30*0+240, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
        B = window.draw_text(op_letter[1] + opcoes[1], x=window.width / 2 - 75, y=30*1+240, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)
        C = window.draw_text(op_letter[2] + opcoes[2], x=window.width / 2 - 75, y=30*2+240, size=20, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)

        for i in answerTries:
            i.draw()

        aux -= 0.75 * window.delta_time()
        timer.draw()
        window.draw_text(str(int(aux)), x=window.width - 60, y=window.height - 40, size=20, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)

        # Condição para quando o tempo acabar, (está incompleta)
        # if aux < 0:
        #     break

        window.update()

def escapeQuestWin():
    global state

    while state == True:
        if key.key_pressed("ESC"):
            escapeQuestMenu()
        

        

def escapeQuestOptions():
    global state, dificuldade, som
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
                dificuldade = 1
                strLevel = "Easy"
        
        if mouse.is_over_object(medium):
            medium1.draw()
            if mouse.is_button_pressed(1):
                dificuldade = 2
                strLevel = "Medium"
            
        if mouse.is_over_object(hard):
            hard1.draw()
            if mouse.is_button_pressed(1):
                dificuldade = 3
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