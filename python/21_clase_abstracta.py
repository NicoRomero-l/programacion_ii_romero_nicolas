from abc import ABC, abstractmethod

class NaveEspacial(ABC):
    modelo:str
    
    def __init__(self, modelo:str):
        self.modelo = modelo

    @abstractmethod
    def despegar():
        pass

class NaveCapsula(NaveEspacial):
    def __init__(self, modelo:str):
        super().__init__(modelo)

    def despegar(self):
        print(self.modelo, "despega con motores de capsule corp")

class NaveSayajin(NaveEspacial):
    def __init__(self, modelo:str):
        super().__init__(modelo)

    def despegar(self):
        print(self.modelo, "Despega inmediatamente")

nave_bulma=NaveCapsula("Nave de Bulma")
nave_vegeta=NaveSayajin("Capsula de Saiyajin")
nave_bulma.despegar()
nave_vegeta.despegar()