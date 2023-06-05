from variables import window, key, mouse, state
from variables import menuFundo, start, options, leave, start1, options1, leave1
from variables import gameFundo, personagem, bowl_1, bowl_2, bowl_3, life_puzzle, life_player, thorns, fire

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
    while state == True:
        if key.key_pressed("ESC"):
            return 

        gameFundo.draw()
        personagem.draw()
        bowl_1.draw()
        bowl_2.draw()
        bowl_3.draw()
        life_puzzle.draw()
        life_player.draw()
        thorns.draw()
        fire.draw()
        
        window.update()

while state == True:
    escapeQuestMenu()