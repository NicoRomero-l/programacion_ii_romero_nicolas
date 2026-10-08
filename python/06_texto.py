#String cadeda de caracteres

jedi= "Qui-Gon Jinn"
aprendiz= "Obi-Wan Kenobi"
droide= "R2-D2"
planeta= "Naboo"
codigo="327"


print ("El Jedi es: ", jedi)
print("El jedy", type(jedi))
print("El aprendiz es: ", aprendiz)
print("El aprendiz", type(aprendiz))
print("El droide es: ", droide)
print("El droide", type(droide))
print("El planeta es: ", planeta)
print("El planeta", type(planeta))
print("El codigo es: ", codigo)
print("El codigo", type(codigo))



longitud_jedi= len(jedi)
print("La longitud del nombre del Jedi es: ", longitud_jedi)
longitud_aprendiz= len(aprendiz)
print("La longitud del nombre del aprendiz es: ", longitud_aprendiz)


mensaje= "La federacion de comercio ha bloqueado los planetas de Naboo"
print("El mensaje es: ", mensaje)
mensaje_mayusculas= mensaje.upper()
print("El mensaje en mayusculas es: ", mensaje_mayusculas)
mensaje_minusculas= mensaje.lower()
print("El mensaje en minusculas es: ", mensaje_minusculas)

comunicado= "Los Jedi vana a negociar..."
print("El comunicado es: ", comunicado)
nuevo_comunicado= comunicado.replace("vana", "van a")
print("El nuevo comunicado es: ", nuevo_comunicado) 

planetas= "Naboo", "Tatooine", "Coruscant", "Alderaan"
planetas_lista = planetas.split(", ")
print(planetas_lista)
print("La lista de planetas es: ", str(planetas_lista))
print("El primer planeta es: ", planetas_lista[0])

droide = "R2-D2"
print("El droide es: ", droide)
print("El primer caracter del droide es: ", droide[0])
print("El segundo caracter del droide es: ", droide[1])
print("El tercer caracter del droide es: ", droide[2])
print("El cuarto caracter del droide es: ", droide[3])
print("El quinto caracter del droide es: ", droide[4])
print("El sexto caracter del droide es: ", droide[-1])


planeta = "            Naboo         "
print("El planeta es: ", planeta)
planeta_sin_espacios = planeta.strip()
print("El planeta sin espacios es: ", planeta_sin_espacios)

