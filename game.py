from utils.variables import window, keyboard, fundo_game
from utils.variables import personagem, bowl_1, bowl_2, bowl_3, life_puzzle, life_player, thorns, fire

window = window

def tela_jogo():
    while True:

        if keyboard.key_pressed("ESC"):
            return 

        fundo_game.draw()
        personagem.draw()
        bowl_1.draw()
        bowl_2.draw()
        bowl_3.draw()
        life_puzzle.draw()
        life_player.draw()
        thorns.draw()
        fire.draw()
        window.update()