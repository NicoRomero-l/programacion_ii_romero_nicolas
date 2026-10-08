#condicional if simple 

combustible = 10
if combustible >= 10:
    print("Puedes despegar")

#condicional if else

creditos= int(input("Ingrese la cantidad de creditos: "))
precio_repuesto = int(input("Ingrese el precio del repuesto: ")) 

if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
else:
    print("No tienes suficientes creditos para comprar el repuesto")


#condicional anidado if

if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
    if creditos > precio_repuesto:
        print("Te sobraran creditos")
    else:
        print("No te sobraran creditos")
else:
    print("No tienes suficientes creditos para comprar el repuesto")

#condicional if elif else

if creditos > precio_repuesto:
    print("Puedes comprar el repuesto y te sobran creditos")
elif creditos == precio_repuesto:
    print("Puedes comprar el repuesto pero no te sobraran creditos")
else:
    print("No tienes suficientes creditos para comprar el repuesto")


tipo_repuesto = input("Ingrese el tipo de repuesto (motor, ala o escudo): ")
if tipo_repuesto == "motor" and creditos >= precio_repuesto and tipo_repuesto == "ala":
    print("Puedes comprar el repuesto")
elif tipo_repuesto == "escudo" and creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
elif tipo_repuesto == "ala" and creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
else:
    print("No tienes suficientes creditos para comprar el repuesto o el tipo de repuesto no es valido")




