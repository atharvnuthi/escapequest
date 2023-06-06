from variables import window, key, mouse, state, dificuldade, som
from variables import menuFundo, start, options, leave, start1, options1, leave1
from variables import soundOn, soundOff, easy, medium, hard, easy1, medium1, hard1, optionsFundo
from variables import personagem, velPersonagem, telas, numCenas

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

    while state == True:
        if key.key_pressed("ESC"):
            return

        if key.key_pressed("RIGHT"):
            personagem.set_sequence(0, 2, True)
            personagem.update()
            personagem.x += velPersonagem * window.delta_time()

        if key.key_pressed("LEFT"):
            personagem.set_sequence(2, 4, True)
            personagem.update()
            personagem.x -= velPersonagem * window.delta_time()

        if personagem.x > window.width:
            personagem.x = 0
            i += 1

        if personagem.x < 0:
            if i !=0:
                personagem.x = window.width
                i -= 1
            elif i == 0:
                personagem.x = 0   

        if i == numCenas:
            return
        
        telas[i].draw()
        personagem.draw()
        window.update()

def escapeQuestOptions():
    global dificuldade, som, state

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
        
        if mouse.is_over_object(medium):
            medium1.draw()
            if mouse.is_button_pressed(1):
                dificuldade = 2
            
        if mouse.is_over_object(hard):
            hard1.draw()
            if mouse.is_button_pressed(1):
                dificuldade = 3
        
        if mouse.is_over_object(soundOn):
            if mouse.is_button_pressed(1):
                som = True
        
        if mouse.is_over_object(soundOff):
            if mouse.is_button_pressed(1):
                som = False

        window.update()


while state == True:
    escapeQuestMenu()