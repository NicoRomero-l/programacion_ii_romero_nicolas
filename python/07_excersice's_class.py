costo = float(input("Ingrese el peso de paquete en Kg (Puede añadir decimales): "))
zona = int(input("Ingrese la zona de destino ingresando un numero del America (1), Europa (2) o Resto del mundo (3): "))

America = 5.0
Europa = 7.5
Resto_del_mundo = 10.0

if zona == 1:
    costo_total = costo * America
    print("El costo total del envio es: ", costo_total)
elif zona == 2:
    costo_total = costo * Europa
    print("El costo total del envio es: ", costo_total)
elif zona == 3: 
    costo_total = costo * Resto_del_mundo
    print("El costo total del envio es: ", costo_total)
else:
    print("Los digitos que a ingresado no son validos, por favor verifique.")


if zona == 1:
    costo_total = costo * America
    print("El costo total del envio es: ", costo_total)
    if zona == 2:
        costo_total = costo * Europa
        print("El costo total del envio es: ", costo_total)
        if zona == 3: 
            costo_total = costo * Resto_del_mundo
            print("El costo total del envio es: ", costo_total)
else:
    print("los datos ingresados son invalidos, por favor verificar")
