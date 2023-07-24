class Node:
    def __init__(self, data = None):

        self.__data__ = data
        self.next = None
    
    def setProx(self, prox):
        self.next = prox
    
    def getData(self):
        return self.__data__
    
    def getProx(self):
        return self.next