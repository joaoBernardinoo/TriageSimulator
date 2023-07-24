import os
path = os.path.dirname(os.path.abspath(__file__))
import pyglet
import sys
import menu
import cLabels
import hospital

# ********** Inicializa a janela da simulação ***********
window = pyglet.window.Window(width= 1280, height =720, caption="Central de Regulação de Leitos")
window.set_location(220,40)
class Game():

    def __init__(self,maxBedsPerDay = 5, maxBedsTotal= 6):
        ############## Carrega os recursos #########################

        self.background = pyglet.resource.image("resources/background.png") # Plano de fundo
        # x = 640 y = 360

        icon = pyglet.resource.image("resources/icon.png") # Icone
        window.set_icon(icon)

        self.doctor = pyglet.sprite.Sprite(
            pyglet.image.load_animation(f"{path}/resources/medico.gif"), x = 962, y = 480,
        )
        self.ambulance = pyglet.sprite.Sprite(
            pyglet.image.load(f"{path}/resources/ambulancia22.png"), x = 15, y = -40,
        )

        self.ambulance.parked = True
        self.ambulance.inMovement = False

        #### Musiquinha ####
        music = pyglet.media.load(f"{path}/resources/sound2.mp3")
        music.play()

        ############## Atualiza as informações a serem desenhadas ###########
        #     
        self.mainMenu = menu.Menu(window.width,window.height)

        self.gui = cLabels.labels()
        
        ############## Realiza o processo de triagem de pacientes ###########

        self.hp = hospital.waitRoom(maxBedsPerDay,maxBedsTotal,self.gui)

        self.gui.hospital = self.hp

    ## Renderiza as informações na tela
    def run(self):

        self.background.blit(0, 0)
        self.doctor.draw()
        self.gui.draw_labels()
        self.gui.draw_clipboard()
        self.gui.draw_indicators()
        
        self.ambulance.draw()
        
        if not self.ambulance.inMovement:
            self.gui.ambulance_label.draw()

            if not self.gui.boardVisible and not self.hp.step:
                self.gui.tutorial3.draw()

        if self.mainMenu.visible:
            self.mainMenu.draw_menu()

# Capacidade máxima leitos que o centro pode armazenar
n = 6
if (len(sys.argv) > 1):
    n = int(sys.argv[1])
    if n < 0:
        n = 6

# Capacidade máxima de pacientes que podem ser transportados pela ambulância
m = 50
if (len(sys.argv) > 2):
    m = int(sys.argv[2])

game = Game(maxBedsPerDay= n, maxBedsTotal= m)

# Detecta o evento para desenhar na tela
@window.event 
def on_draw():
    window.clear()
    game.run()

# Detecta se alguma tecla foi pressionada
@window.event 
def on_key_press(symbol,modifiers):
    if symbol == pyglet.window.key.SPACE and not game.mainMenu.visible:
        game.hp.run(game.ambulance)

    elif symbol == pyglet.window.key.P:
        game.hp.printQueues()
    
    game.mainMenu.visible = False

if __name__ == '__main__':
    pyglet.app.run()


