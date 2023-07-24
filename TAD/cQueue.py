
import TAD.cNode


class queue:
    
    def __init__(self):

        self.front = None # Primeiro da Fila

        self.back = None # Ultimo da Fila
        
        self.mysize = 0

    # Retorna o tamanho da fila
    def size(self):
        return self.mysize

    # Checa se a fila está vazia
    def isEmpty(self): 
        return self.front == None 
           
    # Enfileira o nó
    def queue(self, node):
        self.mysize += 1

        if self.back == None:
            self.front = node
            self.back = node
            return

        self.back.setProx(node)
        self.back = node
    def moveNode(self, node):
        node.setProx(None)
        self.mysize += 1
        id = node.getData().id
        if self.front == None or self.back == None:
            self.front = node
            self.back = node
            return
        self.back.next = node
        self.back = node

    # Retorna o primeiro da fila
    def getFront(self):
        return self.front

    # Remove o primeiro da fila
    def deQueue(self): 
        if self.isEmpty():
            raise Exception("Fila vazia")
        front = self.front
        self.mysize -= 1
        self.front = front.getProx()

        if self.front == None:
            self.back = None
        return front
    
    # Remove o paciente escolhido
    def remove(self,node):
        currentnode = self.front
        # Remove o primeiro paciente caso ele tenha o Id procurado
        if currentnode is not None:
            if currentnode.getData() == node.getData():
                self.front = currentnode.getProx()
                self.mysize -= 1
                currentnode = None
                if self.front == None:
                    self.back = None
                return 
        # Percorre a lista e remove o nó
        while currentnode is not None:
            if node.getData() == currentnode.getData():
                self.mysize -= 1
                if currentnode.getProx() == None:
                    self.back = prev
                break
            prev = currentnode
            currentnode = currentnode.getProx()
        # Retorna caso não consiga remover o nó
        if currentnode == None:
            return

        # Faz o nó anterior apontar para o próximo nó, assim removendo a chave da fila
        prev.setProx(currentnode.getProx())
        return False

    #Imprime a fila no terminal
    def printList(self,id= None):
        temp = self.front
        if temp is None:
            print(" Vazia",end='')
        while temp != None:
            if temp.getData().id == id:
                print(f"{temp.getData().id}",end=','),
            else:
                print(f"{temp.getData().id}",end=','),
            temp = temp.getProx()
    