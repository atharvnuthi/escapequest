from variables import window, key, mouse, state
from variables import menuFundo, telas, start, options, leave, start1, options1, leave1
from variables import personagem

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

        if mouse.is_over_object(leave):
            leave1.draw()
            if mouse.is_button_pressed(1):
                state = False    
        
        window.update()

def escapeQuestGame():
    global state
    vel_personagem = 400
    i = 0

    while state == True:
        if key.key_pressed("ESC"):
            return

        if key.key_pressed("RIGHT"):
            personagem.set_sequence(0, 2, True)
            personagem.update()
            personagem.x += vel_personagem * window.delta_time()

        if key.key_pressed("LEFT"):
            personagem.set_sequence(2, 4, True)
            personagem.update()
            personagem.x -= vel_personagem * window.delta_time()

        if personagem.x > window.width and i != 21:
            personagem.x = 0
            i += 1

        if personagem.x < 0 and i != 0:
            personagem.x = window.width
            i -= 1

        telas[i].draw()
        personagem.draw()
        window.update()

while state == True:
    escapeQuestMenu()