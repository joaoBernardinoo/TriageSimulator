import TAD.cStack as cStack
import TAD.cBed as cBed
import TAD.cNode as cNode
import TAD.cQueue as cQueue
import pyglet

# Classe implementada para armazenar as filas e pilhas e realizar as atribuições
class WaitLine: # Fila para o leito
    def __init__(self,maxBeds,label):

        self.redLine = cQueue.queue()   # Fila Vermelha

        self.orangeLine = cQueue.queue()   # Fila Laranja

        self.yellowLine = cQueue.queue()   # Fila Amarela
    
        self.bedStack = cStack.Stack(maxBeds) # Pilhas dos leitos

        self.label = label

        self.free  = 0

    # Atribui os pacientes à fila respectiva a sua prioridade
    def assignPacient(self,pacient):
        waiting = cNode.Node(pacient)

        if pacient.category == 0:
            self.redLine.queue(waiting)

        elif pacient.category == 1:
            self.orangeLine.queue(waiting)
        
        else:
            self.yellowLine.queue(waiting)

    def assignBed(self):
        pacient = None
        bed = None

        if self.bedStack.numElem == 0:
            self.label.hospital.nextStep()
            return

        #Atribui os leitos à fila vermelha
        if not self.redLine.isEmpty():

            pacient = self.redLine.deQueue()
            bed     = self.bedStack.pop()
            self.toggleClipboard(0,bed,pacient) # * <- Passa o leito e o paciente para a prancheta
            self.free -= 1

        #Atribui os leitos à fila laranja
        elif not self.orangeLine.isEmpty():

            pacient = self.orangeLine.deQueue()
            bed     = self.bedStack.pop()
            self.toggleClipboard(0,bed,pacient)# *
            self.free -= 1

        #Atribui os leitos à fila amarela
        elif not self.yellowLine.isEmpty():

            pacient = self.yellowLine.deQueue()
            bed     = self.bedStack.pop()
            self.toggleClipboard(0,bed,pacient) # *
            self.free -= 1
        else:
            self.label.hospital.nextStep()
            return
            
        print(pacient.getData().id,'-',pacient.getData().name)
        print(str(bed))
        # Deleta ambos
        del bed
        del pacient   

    # Desenha a prancheta com o relatório médico na tela
    def toggleClipboard(self,dt=0,bed= '', pacient= ''):
        if self.label.boardVisible:
            self.label.boardVisible = False
            print()
            #Chama a função de atribuir o paciente
            self.assignBed()

        else:
            # Atualiza as informações da prancheta e esconde-a após 2 segundos
            self.label.pacient = str(pacient.getData())
            self.label.bed = str(bed)
            self.label.update_hospital()
            self.label.boardVisible = True

            # Tempo que a prancheta fica vísivel na tela
            n = 5
            pyglet.clock.schedule_once(self.toggleClipboard,n)

    #Adiciona os leitos à pilha para serem removidos aqueles mais recentemente liberados
    def pushBed(self, category, quantity):
        for i in range(quantity):
            #Retorna caso a quantidade de leitos exceda a pilha
            if self.bedStack.tam <= self.bedStack.numElem:
                return
            self.bedStack.push(cBed.Bed(category))
            self.free += 1
