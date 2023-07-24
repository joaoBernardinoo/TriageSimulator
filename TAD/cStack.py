
class Stack:
    #Inicializa a pilha com um tamanho máximo de elementos
    def __init__(self,n):

        self.numElem = 0
        self.tam = n
        self.pilha = [0]*n
        self.top = None

    #Checa se a pilha está vazia
    def empty(self):
        if self.top != None:
            return False

        return True

    # Adiciona um elemento ao topo da pilha
    def push(self,n): 
        if self.tam == self.numElem:
            return False

        self.pilha[self.numElem] = n
        self.numElem += 1
        self.top = n
        return True

    # Remove o elemento do topo da pilha
    def pop(self):
        if self.empty():
            return False
        topo = self.top
        
        if self.numElem == 1:
            self.top = None

        self.top = self.pilha[self.numElem-2]
        self.pilha[self.numElem -1] = 0
        self.numElem -= 1
        return topo