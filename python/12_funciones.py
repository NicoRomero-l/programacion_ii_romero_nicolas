def activar_sistema(): #funciones sin parametros / simples
    print("== sistema de naboo ==")
    print ("sistema de control activado")

activar_sistema()

def saludar_jedi(nombre): #funciones con parametros
    print(f"Que la fuerza te acompañe : {nombre}")

saludar_jedi("Qui-Gon Jim")
saludar_jedi("Obi-Wan Kenobi") 

def mostrar_nave(nombre, combustible):
    print(f"nave: {nombre}")
    print(f"combustible: {combustible}")

mostrar_nave("Caza n-1", 80)


#funciones que devuelven un dato o informacion "RETURN"

def calcular_combustible(inicial, consumo):
    restante = inicial - consumo
    return restante

resultado = calcular_combustible(100, 30)
print(f"combustible: {resultado}")


def calcular_combustible(inicial, consumo):
    return inicial - consumo

resultado = calcular_combustible(100, 30)
print(f"combustible: {resultado}")


def nave_preparada(combustible):
    return combustible>=50


if nave_preparada(80):
    print("nave autorizada para despegar")
else:
    print("nave necesita recarga")
