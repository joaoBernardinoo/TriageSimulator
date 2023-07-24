import random
hospitals = ["Albert Einstein","Sirio Libanes","Santa Catarina","Aliança","Santa Isabel","Português"]
class Bed:
    # Cria um leito de acordo com sua categoria e gera um id aleatório
    def __init__(self,category):
        self.category = category
        self.hospital = random.sample(hospitals,1)[0]
        # Gera um id aleatório baseado em sua categoria, hospital e números
        self.id = self.hospital[0] + str(self.category) + str(random.randint(1000,9999))

    def __str__(self):
        return f"Atribuindo paciente \nao leito {self.id} do \nHospital {self.hospital}"

if __name__ == '__main__':
    b = Bed(0)
    print(b)