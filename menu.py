import pyglet
from pyglet import shapes

import os
path = os.path.dirname(os.path.abspath(__file__))

class Menu:

    def __init__(self,x = 1280, y = 720):

        self.win_width = x
        self.win_height = y
        self.visible = True
        self.welcome_label = None

        self.menu = pyglet.graphics.Batch()

        self.hospital = pyglet.sprite.Sprite(
            pyglet.image.load_animation(f"{path}/resources/hospital.gif"), x = 40, y = 80, batch = self.menu,
        )
        self.border1 = pyglet.shapes.Rectangle(
            x = 0, y = 0, width = 40, height = 720, color= (0,0,30), batch = self.menu
        )
        self.border2 = pyglet.shapes.Rectangle(
            x = 0, y = 0, width = 1280, height = 80, color= (0,0,30), batch = self.menu
        )
        self.border3 = pyglet.shapes.Rectangle(
            x = 1240, y = 0, width = 40, height = 720, color= (0,0,30), batch = self.menu
        )

        self.welcome_label = pyglet.text.Label(
            "Pressione qualquer tecla para começar a simulação",
            font_name="Arial",
            font_size=30,
            color= (255,255,255,255),
            x = self.win_width  // 2, y = 20,
            anchor_x="center",
            anchor_y="bottom",
        )

    def draw_menu(self):
        
        self.menu.draw()
        self.welcome_label.draw()
