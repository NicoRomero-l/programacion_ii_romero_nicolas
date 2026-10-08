#Operadores Aritmeticos

"""
Operadores Aritmeticos:
+ : Suma
- : Resta
* : Multiplicacion
/ : Division
% : Modulo (resto de la division)
** : Potencia
// : Division entera (parte entera de la division)

"""

valor1= 10
valor2= 3

suma= valor1 + valor2
resta= valor1 - valor2
multiplicacion= valor1 * valor2
division= valor1 / valor2
modulo= valor1 % valor2
potencia= valor1 ** valor2


print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion) 
print("Division:", division)
print("Modulo:", modulo)
print("Potencia:", potencia)



print("tabla de multiplicar del 5")
multiplicador= 5
print(multiplicador, "x 1 =", multiplicador * 1)
print(multiplicador, "x 2 =", multiplicador * 2)
print(multiplicador, "x 3 =", multiplicador * 3)
print(multiplicador, "x 4 =", multiplicador * 4)
print(multiplicador, "x 5 =", multiplicador * 5)
print(multiplicador, "x 6 =", multiplicador * 6)
print(multiplicador, "x 7 =", multiplicador * 7)
print(multiplicador, "x 8 =", multiplicador * 8)
print(multiplicador, "x 9 =", multiplicador * 9)
print(multiplicador, "x 10 =", multiplicador * 10)

print("El area de un triangulo con base 5 y altura 10 es:", (5 * 10) / 2)


# Operadores de Comparacion

"""
Operadores de Comparacion:
== : Igual a
!= : Distinto de
> : Mayor que
< : Menor que
>= : Mayor o igual que
<= : Menor o igual que
"""


velocidad_anakin= 950
velocidad_sebulba= 900

print("¿Anakin es mas rapido que Sebulba?", velocidad_anakin > velocidad_sebulba)
print("¿Anakin es mas lento que Sebulba?", velocidad_anakin < velocidad_sebulba)
print("¿Anakin es igual a Sebulba?", velocidad_anakin == velocidad_sebulba)
print("¿Anakin es distinto a Sebulba?", velocidad_anakin != velocidad_sebulba)
print("¿Anakin es mayor o igual a Sebulba?", velocidad_anakin >= velocidad_sebulba)
print("¿Anakin es menor o igual a Sebulba?", velocidad_anakin <= velocidad_sebulba)


resultado= velocidad_anakin > velocidad_sebulba
print("Resultado de la comparacion:", resultado)
print("Tipo de resultado:", type(resultado))


# Operadores Logicos

"""
Operadores Logicos:
- and (y)
- or (o)
- not (no)
"""

motores_funcionando= True
escudos_funcionando= False
combustible=80

print("¿Todos los sistemas estan funcionando?", motores_funcionando and escudos_funcionando)
print("¿Algunos sistema están funcionando?", motores_funcionando or escudos_funcionando)
print("¿Los motores no están funcionando?", not motores_funcionando)

cantidad_motores= 2
cantidad_alas= 4
combustible=80

print("¿La nave tiene 2 motores y 4 alas?")
print(cantidad_motores >= 2 and cantidad_alas >= 4 and combustible >= 50)
print("¿La nave tiene 2 motores o 4 alas?")
print(cantidad_motores >= 2 or cantidad_alas >= 4 or combustible >= 50)
print("¿La nave no tiene 2 motores?")
print(not cantidad_motores == 2 and combustible >= 50 and cantidad_alas >= 4)


#operadores de Asignacion

"""
Operadores de Asignacion:
= : Asignacion
+= : Suma y asignacion
-= : Resta y asignacion
*= : Multiplicacion y asignacion
/= : Division y asignacion
%= : Modulo y asignacion
**= : Potencia y asignacion
"""

velocidad= 100
print("Velocidad inicial:", velocidad)
velocidad += 50
print("Velocidad despues de acelerar:", velocidad)
velocidad -= 30
print("Velocidad despues de frenar:", velocidad)

multiplicador= 2
velocidad *= multiplicador
print("Velocidad despues de multiplicar:", velocidad)
divisor= 4
velocidad /= divisor
print("Velocidad despues de dividir:", velocidad)
modulo= 3
velocidad %= modulo
print("Velocidad despues de aplicar modulo:", velocidad)
potencia= 2
velocidad **= potencia
print("Velocidad despues de aplicar potencia:", velocidad)


#presedencia de operadores
"""
Presedencia de operadores:
1. ()
2. ** - potencia
3. * / // % - multiplicacion, division, division entera, modulo
4. + -  suma, resta
"""

resultado_1= 10 + 5 * 2
print("Resultado 1:", resultado_1)
resultado_2= (10 + 5) * 2
print("Resultado 2:", resultado_2)
resultado_3= 10 + 5 * 2 ** 2
print("Resultado 3:", resultado_3)
