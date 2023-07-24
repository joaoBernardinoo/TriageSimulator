import random
import os
path = os.path.dirname(os.path.abspath(__file__))
with open(f'{path}\\name_list.txt','r',encoding="utf-8") as file:
    content = file.readlines()

content = [x.rstrip('\n').split('|') for x in content]

class pacient:

    def __init__(self,category):
        
        info = random.sample(content,1)[0]
        self.name = info[0] # Nome do Paciente
        self.gender = info[1] # Sexo Biológico
        self.category = category

        if self.category == 0:
            self.age = random.randint(1,11) # Idade em mêses
            self.category_name = "Neonatal"
        elif self.category == 1:
            self.age = random.randint(1,13) # Idade em anos
            self.category_name = "Pediatrica"
        else:
            self.age = random.randint(18,65)
            self.category_name = "Adulta"
            
        self.id = self.name[0] + str(self.age)[0] + self.gender[0] + str(self.category) + self.category_name[0] +str(random.randint(10,99)) 

    #Ficha do Paciente
    def __str__(self):
        token = f"Nome: {self.name}\n"
        if self.category == 0:
            token += f"Idade: {self.age} meses\n"
        else:
            token += f"Idade: {self.age} anos\n"

        token += f"Sexo: {self.gender}\nId: {self.id}"
        return token

if __name__ == '__main__':
    paciente = pacient(random.randint(0,2))
    a = paciente
    print(str(paciente))
