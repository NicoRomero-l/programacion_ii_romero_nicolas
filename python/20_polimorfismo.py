class Guerrero:
    nombre:str
    poder_inicial:int
    horas:int

    def __init__(self, nombre: str, poder_inicial: int, horas:int):
        self.nombre = nombre
        self.poder_inicial = poder_inicial
        self.horas = horas

    def atacar(self):
        print(f"{self.nombre} realiza un ataque")

    def calcular_poder(self):
        return self.poder_inicial + self.horas*150



class Goku(Guerrero):
    def __init__(self, nombre: str, poder_inicial:int, horas: int):
        super().__init__(nombre, poder_inicial, horas)

    def atacar(self):
        print(self.nombre, "Usa Kamehameha")
    
    def calcular_poder(self):
        return self.poder_inicial + self.horas*100

class Vegueta(Guerrero):
    def __init__(self, nombre: str, poder_inicial:int, horas: int):
        super().__init__(nombre, poder_inicial, horas)

    def atacar(self):
        print(self.nombre, "Usa final flash")

    def calcular_poder(self):
        return self.poder_inicial + self.horas*150

goku=Goku("Gran Goku", 150, 60)
vegueta=Vegueta("Gran Vegeta", 100, 100)
goku.atacar()
vegueta.atacar()
print(goku.calcular_poder())
print(vegueta.calcular_poder())
