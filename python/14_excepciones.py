print("==== CONTROL DE ENERGIA ====")
energia_texto= "ochenta"

try:
    energia = int("mucho")
    print(energia)
except ValueError: #si no se especifica, tomara cualquier valor
    print("ERROR: debe ser numerico")


print("fin del sistema")

"""
TIPOS DE EXCEPCION:

ValudeError
TypeError
KeyError
IndexError
ZeroDivisionError
"""


def calcular_energia(total, cantidad):
    try:
        resultado=total/cantidad
        return resultado
    except ZeroDivisionError:
        print("Error: division entre cero")
        return None

    except TypeError:
        print("Error: deben ser valores numero")
        return None

print("Caso 1:", calcular_energia(100,4))
print("Caso 1:", calcular_energia(100,0))
print("Caso 1:", calcular_energia(100,"cuatro"))


print("========= DIAGNOSTICO R2-D2 =========")
try:
    energia = int("cautro")
    print("energia", energia)
except ValueError:
    print("Error de lectura")
else:
    print("Diagnostico completado")
finally:
    print("cerrando diagnostico")



def validar_energia(energia):
    if type(energia) is not int:
        raise TypeError("La energia debe ser numerica")
    if energia < 0 or energia > 100:
        raise TypeError("La energia debe ser entre 0 y 100")
    return energia


try:
    resultado=validar_energia(60)
    print("Energia: ", resultado)
except (TypeError, ValueError) as error:
    print("Error: ", error)

