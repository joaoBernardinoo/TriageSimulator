import pyglet
from pyglet import shapes
from pyglet import font
import os
path = os.path.dirname(os.path.abspath(__file__))

class labels:

    def __init__(self):

        self.hospital = None

        self.deaths = 0       # Obitos
        self.attended = '0'     # Pacientes atendidos
        self.red_line = '0'     # redline.size()
        self.orange_line = '0'  # orangeline.size()
        self.yellow_line = '0'  # yellowline.size()

        self.avaliable_label = None
        self.queue_labels = None # informações sobre as filas
        
        #Tamanho das filas
        self.red_line1     = 0
        self.orange_line1  = 0
        self.yellow_line1  = 0
        self.red_line2     = 0
        self.orange_line2  = 0
        self.yellow_line2  = 0
        self.red_line3     = 0
        self.orange_line3  = 0
        self.yellow_line3  = 0
        
        self.neonatal_total  = 0
        self.pediatric_total = 0
        self.adult_total     = 0

        # Subtítulos
        self.subtitle = None 

        #Quantidade de leitos na pilha
        self.neonatal_beds  = 0
        self.pediatric_beds = 0
        self.adult_beds     = 0

        #Diálogo com a ambulância
        self.ambulance_display = ''
        self.ambulance_label = None 

        # Setas para indicar a entrada e saída de pacientes
        self.greenArrowN = pyglet.shapes.Triangle(
            720,400,745,450,770,400, color = (32,142,70),
        )
        self.redArrowN = pyglet.shapes.Triangle(
            840,450,865,400,890,450, color = (178,48,40),
        )
        self.greenArrowP = pyglet.shapes.Triangle(
            720,315,745,365,770,315, color = (32,142,70),
        )
        self.redArrowP = pyglet.shapes.Triangle(
            840,365,865,315,890,365, color = (178,48,40),
        )
        self.greenArrowA = pyglet.shapes.Triangle(
            720,230,745,280,770,230, color = (32,142,70),
        )
        self.redArrowA = pyglet.shapes.Triangle(
            840,280,865,230,890,280, color = (178,48,40),
        )
        # Carrega a prancheta e a barra de progressão
        self.pacientInfo = pyglet.graphics.Batch()
        self.boardVisible = False

        self.clipboard = pyglet.sprite.Sprite(
            pyglet.image.load(f"{path}/resources/clipboard.png"), x = 225, y = -50, batch= self.pacientInfo,
        )
        self.progression_bar = pyglet.sprite.Sprite(
            pyglet.image.load_animation(f"{path}/resources/progression_bar.gif"), x = 270, y = -60,
        )
        self.progression_bar.scale = 1.5
        
        #Variáveis que guardam as informações da prancheta
        self.pacient = 'Nome: Ana Araujo\nIdade: 38 anos\nSexo: Feminino\nId: A3F2A42'
        self.bed = 'Atribuindo paciente\nao leito A09487 do\nHospital Albert Einstein'
        
        #Atualiza as informações
        self.update_labels()

    

    # Atualiza as informações das fila
    def update_hospital(self,ambulance_passengers= ''):
        self.red_line1 = self.hospital.neonatal.redLine.size()
        self.red_line2 = self.hospital.pediatric.redLine.size()
        self.red_line3 = self.hospital.adult.redLine.size()

        self.orange_line1 = self.hospital.neonatal.orangeLine.size()
        self.orange_line2 = self.hospital.pediatric.orangeLine.size()
        self.orange_line3 = self.hospital.adult.orangeLine.size()

        self.yellow_line1 = self.hospital.neonatal.yellowLine.size()
        self.yellow_line2 = self.hospital.pediatric.yellowLine.size()
        self.yellow_line3 = self.hospital.adult.yellowLine.size()

        self.red_line    = self.red_line1 + self.red_line2 + self.red_line3
        self.orange_line = self.orange_line1 + self.orange_line2 + self.orange_line3
        self.yellow_line = self.yellow_line1 + self.yellow_line2 + self.yellow_line3

        self.neonatal_total   = self.red_line1 + self.orange_line1 + self.yellow_line1
        self.pediatric_total  = self.red_line2 + self.orange_line2 + self.yellow_line2
        self.adult_total      = self.red_line3 + self.orange_line3 + self.yellow_line3

        self.neonatal_beds    = self.hospital.neonatal.free
        self.pediatric_beds    = self.hospital.pediatric.free
        self.adult_beds    = self.hospital.adult.free

        self.ambulance_display = str(ambulance_passengers)
        self.update_labels()

    # Labels para todas as iformações na tela
    def update_labels(self):  
        self.batch = pyglet.graphics.Batch()
#**************** Informações no canto inferior direito ************
        self.deaths_label = pyglet.text.Label(
            " ".join(str(self.deaths)),
            font_name="Arial",
            font_size=56,
            color= (0,0,30,255),
            x = 1190, 
            y = 50,
            anchor_x="right",
            anchor_y="center",
            batch=self.batch,
        )
        self.attends_label = pyglet.text.Label(
            "Encaminhados:  ",
            font_name="Arial",
            font_size=26,
            color= (0,0,30,255),
            x = 1160, 
            y = 160,
            anchor_x="right",
            anchor_y="top",
            batch=self.batch,
        )
        self.attends_label = pyglet.text.Label(
            " ".join(str(self.attended)),
            font_name="Arial",
            font_size=48,
            color= (0,0,30,255),
            x = 1190, 
            y = 140,
            anchor_x="right",
            anchor_y="center",
            batch=self.batch,
        )
#**************** Numero de Pacientes em cada fila no total************
        self.red_label = pyglet.text.Label(
            " ".join(str(self.red_line)),
            font_name="Arial",
            font_size=46//len(str(self.red_line)),
            color= (0,0,30,255),
            x = 160, 
            y = 525,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )
        self.orange_label = pyglet.text.Label(
            " ".join(str(self.orange_line)),
            font_name="Arial",
            font_size=46//len(str(self.orange_line)),
            color= (0,0,30,255),
            x = 640-265, 
            y = 525,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )
        self.yellow_label = pyglet.text.Label(
            " ".join(str(self.yellow_line)),
            font_name="Arial",
            font_size=46//len(str(self.yellow_line)),
            color= (0,0,30,255),
            x = 588, 
            y = 525,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )
#**************** Numero de Pacientes em cada fila por categoria************

        #********** Categoria Neonatal **********
        self.queue_labelsN1 = pyglet.text.Label(
            " ".join(str(self.red_line1)),
            font_name="Arial",
            font_size=46 if len(str(self.red_line1)) < 3 else 30,
            color= (0,0,30,255),
            x = 960, 
            y = 425,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )
        self.queue_labelsN2 = pyglet.text.Label(
            " ".join(str(self.orange_line1)),
            font_name="Arial",
            font_size=46 if len(str(self.orange_line1)) < 3 else 30,
            color= (0,0,30,255),
            x = 1050, 
            y = 425,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )
        self.queue_labelsN3 = pyglet.text.Label(
            " ".join(str(self.yellow_line1)),
            font_name="Arial",
            font_size=46 if len(str(self.yellow_line1)) < 3 else 30,
            color= (0,0,30,255),
            x = 1145, 
            y = 425,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )
        # ********** Categoria Pediátrica ********
        self.queue_labelsP1 = pyglet.text.Label(
            " ".join(str(self.red_line2)),
            font_name="Arial",
            font_size=46 if len(str(self.red_line2)) < 3 else 30,
            color= (0,0,30,255),
            x = 960, 
            y = 340,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )
        self.queue_labelsP2 = pyglet.text.Label(
            " ".join(str(self.orange_line2)),
            font_name="Arial",
            font_size=46 if len(str(self.orange_line2)) < 3 else 30,
            color= (0,0,30,255),
            x = 1050, 
            y = 340,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )
        self.queue_labelsP3 = pyglet.text.Label(
            " ".join(str(self.yellow_line2)),
            font_name="Arial",
            font_size=46 if len(str(self.yellow_line2)) < 3 else 30,
            color= (0,0,30,255),
            x = 1145, 
            y = 340,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )
        # ********** Categoria Adulta ************
        self.queue_labelsA1 = pyglet.text.Label(
            " ".join(str(self.red_line3)),
            font_name="Arial",
            font_size=46 if len(str(self.red_line3)) < 3 else 30,
            color= (0,0,30,255),
            x = 960, 
            y = 255,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )
        self.queue_labelsA2 = pyglet.text.Label(
            " ".join(str(self.orange_line3)),
            font_name="Arial",
            font_size=46 if len(str(self.orange_line3)) < 3 else 30,
            color= (0,0,30,255),
            x = 1050, 
            y = 255,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )
        self.queue_labelsA3 = pyglet.text.Label(
            str(self.yellow_line3),
            font_name="Arial",
            font_size=46 if len(str(self.yellow_line3)) < 3 else 30,
            color= (0,0,30,255),
            x = 1145, 
            y = 255,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )
        
#**************** Titulos dos bonecos ************
        self.header1 = pyglet.text.Label(
            "Emergência",
            font_name="Arial",
            font_size=19,
            color= (255,0,30,255),
            x = 640-484, 
            y = 360+305,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )
        self.header2 = pyglet.text.Label(
            "Muito Urgente",
            font_name="Arial",
            font_size=17,
            color= (255,120,0,255),
            x = 640-265, 
            y = 360+305,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )
        self.header3 = pyglet.text.Label(
            "Urgente",
            font_name="Arial",
            font_size=20,
            color= (255,204,0,255),
            x = 640-56, 
            y = 360+305,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch,
        )
#*************** Indicadores da disponibilidade de leitos *********
        # Indicadores em vermelho para a quantidade de pacientes que esperam na fila
        self.neonatal_total_label = pyglet.text.Label(
            str(self.neonatal_total),
            font_name="Arial",
            font_size=30 if len(str(self.neonatal_total)) <3 else 20,
            color= (178,48,40,255),
            x = 830, y = 420,
            anchor_x="right",
            anchor_y="center",
        )
        self.pediatric_total_label = pyglet.text.Label(
            str(self.pediatric_total),
            font_name="Arial",
            font_size=30 if len(str(self.neonatal_total)) <3 else 20,
            color= (178,48,40,255),
            x = 830, y = 335,
            anchor_x="right",
            anchor_y="center",
        )
        self.adult_total_label = pyglet.text.Label(
            str(self.adult_total),
            font_name="Arial",
            font_size=30 if len(str(self.neonatal_total)) <3 else 20,
            color= (178,48,40,255),
            x = 830, y = 250,
            anchor_x="right",
            anchor_y="center",
        )
        # Indicadores em verde para a quantidade de leitos disponível
        self.neonatal_beds_label = pyglet.text.Label(
            str(self.neonatal_beds),
            font_name="Arial",
            font_size=30,
            color= (32,142,70,255),
            x = 710, y = 420,
            anchor_x="right",
            anchor_y="center",
        )
        self.pediatric_beds_label = pyglet.text.Label(
            str(self.pediatric_beds),
            font_name="Arial",
            font_size=30,
            color= (32,142,70,255),
            x = 710, y = 335,
            anchor_x="right",
            anchor_y="center",
        )
        self.adult_beds_label = pyglet.text.Label(
            str(self.adult_beds),
            font_name="Arial",
            font_size=30,
            color= (32,142,70,255),
            x = 710, y = 250,
            anchor_x="right",
            anchor_y="center",
        )
        # Tutoriais
        self.tutorial0 = pyglet.text.Label(
            "Leitos disponíveis",
            font_name="Arial",
            font_size=15,
            color= (32,142,70,255),
            x = 785, y = 530,
            anchor_x="center",
            anchor_y="center",
        )
        self.tutorial1 = pyglet.text.Label(
            "Pacientes em espera",
            font_name="Arial",
            font_size=15,
            color= (178,48,40,255),
            x = 785, y = 500,
            anchor_x="center",
            anchor_y="center",
        )
        self.tutorial2 = pyglet.text.Label(
            "Pressione 'Espaço' para buscar os pacientes",
            font_name="Arial",
            font_size=20,
            color= (0,20,40,255),
            x = 700, y = 30,
            anchor_x="center",
            anchor_y="center",
        )
        self.tutorial3 = pyglet.text.Label(
            "Pressione 'Espaço' para alocar os leitos",
            font_name="Arial",
            font_size=20,
            color= (0,20,40,255),
            x = 700, y = 30,
            anchor_x="center",
            anchor_y="center",
            bold = True
        )
    # ********** Ficha do Paciente ***********
        self.pacient_label = pyglet.text.Label(
            str(self.pacient),
            font_name="Times New Roman",
            font_size=18,
            color= (0,20,40,255),
            x = 475, y = 205,
            anchor_x="center",
            anchor_y="center",
            width = 260,
            multiline = True,
            bold = True,
        )
        self.bed_label = pyglet.text.Label(
            str(self.bed),
            font_name="Times New Roman",
            font_size=17,
            color= (0,20,40,255),
            x = 500, y = 95,
            anchor_x="center",
            anchor_y="center",
            width = 300,
            multiline = True,
        )   

# ********** Display dos pacientes entregues pela ambulância **************
        self.ambulance_label = pyglet.text.Label(
            self.ambulance_display,
            font_name="Arial",
            font_size=15,
            color= (0,20,40,255),
            x = 160, y = 180,
            anchor_x="center",
            anchor_y="center",
            width = 200,
            multiline = True,
        )

    #Desenha os indicadores na tela (setas e tutoriais)
    def draw_indicators(self):
        self.greenArrowN.draw()
        self.neonatal_beds_label.draw()

        self.redArrowN.draw()
        self.neonatal_total_label.draw()
    
        self.greenArrowP.draw()
        self.pediatric_beds_label.draw()

        self.redArrowP.draw()
        self.pediatric_total_label.draw()

        self.greenArrowA.draw()
        self.adult_beds_label.draw()

        self.redArrowA.draw()
        self.adult_total_label.draw()

        self.tutorial1.draw()
        self.tutorial0.draw()
        if self.hospital.step:
            self.tutorial2.draw()
        


# *************** Animação das pranchetas com o relatório médico *************
    def draw_clipboard(self):
        if self.boardVisible:
            self.pacientInfo.draw()
            self.progression_bar.draw()
            self.pacient_label.draw()
            self.bed_label.draw()

    #Desenha as informações na tela     
    def draw_labels(self):
        self.batch.draw()

