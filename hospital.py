
import TAD.cPacient as cPacient
import cWaitLine as waitLine
import random, pyglet, math, os


# Sala de espera em que haverá o controle de pacientes (Atribuição à leitos, movimentação e etc.)
class waitRoom:

    def __init__(self,maxBedsPerDay,maxBedsTotal,labels):

        self.label      = labels
        self.neonatal   = waitLine.WaitLine(maxBedsTotal,self.label)
        self.pediatric  = waitLine.WaitLine(maxBedsTotal,self.label)
        self.adult      = waitLine.WaitLine(maxBedsTotal,self.label)

        self.bedCap     = maxBedsPerDay
        self.name_list  = []
        self.step       = True
        self.count      = 0

        self.ambulance_passengers = ''
        self.avaliable = [0,0,0]

    

#*** Gera uma quantidade aleatória de leitos pra cada categoria 
#*** (Neonatal,Pediátrica,Adulta)
    def __genBeds(self):
        #Indice 0 = Neonatal, 1 = Pediátrico, 2 = Adulto
        beds = [
            random.randint(0,self.bedCap-1), # nº Leitos Neonatal 
            random.randint(0,self.bedCap-1), # nº Leitos Pediátricos
            random.randint(0,self.bedCap-1), # nº Leitos Adultos
        ]
        print(f"=-=-=-=-=-=-=-=-=\n-Requisitando os leitos... {beds}")
        return beds

    def __genPacients(self):
        # Gerar um numero aleatório, dentro de um loop, representando o número de pacientes que chegaram
        print("Transportando os pacientes...  ",end='')
        for i in range(3):
            numPacients = random.randint(1,self.bedCap)
            self.ambulance_passengers += numPacients
            print(' ', numPacients, end="")
            
            for j in range(numPacients):
                #Gera um número que representa a categoria ( Neonatal, Pediatric ou Adulta )
                priority = random.randint(0,2)
                person = cPacient.pacient(category= priority)

                #Atribui cada paciente em sua respectiva categoria através dos ifs
                if i == 0:
                    self.neonatal.assignPacient(pacient= person)
                elif i == 1:
                    self.pediatric.assignPacient(pacient= person)
                else:
                    self.adult.assignPacient(pacient= person)

        print('\n=-=-=-=-=-=-=-=-=')
          
    # ************** Verifica se o paciente foi a óbito, piorou a situação ou melhorou *********
    def verifyPacients(self,queue):
        #Verifica os pacientes da fila emergência
        node = queue.redLine.getFront()
        while node != None:
            id = node.getData().id
            possibility = random.randint(0,100)
            if possibility < 20:
                print(f"\n{id} foi a obito")
                #Remove o paciente da fila
                queue.redLine.remove(node)
                self.label.deaths += 1
            node = node.getProx()
            self.label.update_hospital(self.ambulance_passengers)   

        #Verifica os pacientes da fila muito urgente
        node = queue.orangeLine.getFront()
        while node != None:
            id = node.getData().id
            possibility = random.randint(0,100)  
            if possibility < 15:
                print(f"\n{id} foi alocado a fila vermelha")
                queue.orangeLine.remove(node)
                queue.redLine.moveNode(node)

            elif possibility < 17:
                print(f"\n{node.getData().id} melhorou sua condicao")
                #Remove o paciente da fila
                queue.orangeLine.remove(node)

            node = node.getProx()
            self.label.update_hospital(self.ambulance_passengers)   

        #Verifica os pacientes da fila urgente
        node = queue.yellowLine.getFront()
        while node != None:    
            id = node.getData().id
            possibility = random.randint(0,100)
            if possibility < 10:
                print(f"\n{id} foi alocado a fila laranja")
                queue.yellowLine.remove(node)
                queue.orangeLine.moveNode(node)

            elif possibility < 13:
                print(f"\n{node.getData().id} melhorou sua condicao")
                queue.yellowLine.remove(node)

            node = node.getProx()
            self.label.update_hospital(self.ambulance_passengers)   


    # ************** Animação da ambulância indo buscar os pacientes *********
    def drive_ambulance(self,dt,ambulance):
        
        if ambulance.x < 1280 and ambulance.parked:
            ambulance.x += self.velocity
            self.velocity += 0.5

        elif ambulance.x > 1280:
            self.velocity = 20
            ambulance.x = -127
            ambulance.parked = False

        elif ambulance.x < 15:
            ambulance.x += self.velocity
            self.velocity -= 1.5*math.log10(abs(self.velocity))

        else:
            ambulance.parked = True
            ambulance.inMovement = False
            pyglet.clock.unschedule(self.drive_ambulance)
            self.label.update_hospital(self.ambulance_passengers)
            self.label.boardVisible = False

        
    def run(self,ambulance):
        ## Primeiro Passo ( Receptar os leitos e os pacientes )
        ### Atribui os leitos às categorias
        if self.step:
            if os.name == "nt":
                os.system("cls")
            else:   
                s.system("clear")

            # Gera números aleatórios representando a quantidade de leitos novos
            self.avaliable = self.__genBeds()
            self.ambulance_passengers = 0

            # Atribui cada leito às filas
            self.neonatal.pushBed(0,self.avaliable[0])
            self.pediatric.pushBed(1,self.avaliable[1])
            self.adult.pushBed(2,self.avaliable[2])

            # Gera os pacientes
            self.__genPacients()
            
            ## Controle da simulação ##
            self.step = False
            self.velocity = 0
            ambulance.inMovement = True
            pyglet.clock.schedule_interval(self.drive_ambulance,1/60,ambulance)   
            self.ambulance_passengers = f"{self.ambulance_passengers} pacientes transportados"
            print("Digirindo a ambulancia...")

        # Segundo Passo (Receptar os pacientes e encaminha-los para UTI)
        ## Atribui cada leito disponível a um paciente      
        else:
            #Verifica o estado dos pacientes na fila           
            self.verifyPacients(self.neonatal)
            self.verifyPacients(self.pediatric)
            self.verifyPacients(self.adult)
            self.label.update_hospital(self.ambulance_passengers)
            self.nextStep(1)
        

    def nextStep(self,dt=None):
        self.count += 1
        if self.count == 1:
            self.neonatal.assignBed()
            
        elif self.count == 2:
            self.pediatric.assignBed()

        elif self.count == 3:
            self.adult.assignBed()

        elif self.count == 4:    
            print(f"\n=-=-=-=-=-=-=-=-=\nSobraram {self.neonatal.free}, {self.pediatric.free} e {self.adult.free} leitos")
            print(f"Sobraram {self.label.neonatal_total}, {self.label.pediatric_total} e {self.label.adult_total} pacientes")
            print("Neonatal, Pediatrico e Adulto respectivamente")
            print("=-=-=-=-=-=-=-=-=")
            print("Ambulancia esta pronta para buscar novos pacientes!")
            self.count = 0
            self.step = True

            self.label.update_hospital(self.ambulance_passengers)
            return

        
        #Atualiza as informações da tela
        self.label.update_hospital(self.ambulance_passengers)
        
    
    def printQueues(self,):
        print('\n')
        self.neonatal.redLine.printList()
        print(" | ",end='')
        self.neonatal.orangeLine.printList()
        print(" | ",end='')
        self.neonatal.yellowLine.printList()
        print()
        self.pediatric.redLine.printList()
        print(" | ",end='')
        self.pediatric.orangeLine.printList()
        print(" | ",end='')
        self.pediatric.yellowLine.printList()
        print()
        self.adult.redLine.printList()
        print(" | ",end='')
        self.adult.orangeLine.printList()
        print(" | ",end='')
        self.adult.yellowLine.printList()
        print()
    