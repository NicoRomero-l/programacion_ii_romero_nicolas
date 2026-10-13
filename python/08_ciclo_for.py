# ciclo for 

naves=[
    "caza N-1",
    "Nave real de Naboo",
    "Tranporte"
]

for nave in naves:
    print("Inspeccionado ", nave)

print("Inspeccion realizada.")

rondas=range(1, 6)
print("Tipo de rondas: ", type(rondas))
for ronda in rondas:
    print("Ronda de vigilancia: ", {ronda})
    print("Tipo de dato: ", type(ronda))

droides=range(1,17,2)
print("Tipo de Droides: ", type(droides))
for droide in droides:
    print(f"Reparar : Droide B1-{droide}")
    print("Tipo de dato droide: ", {type(droide)})

planetas=[
    "Naboo",
    "Tatooine",
    "Coruscant",
]

recorrido=enumerate(planetas, start=1)

for posicion, planeta in recorrido:
    print(f"Destino {posicion}: {planeta}")
    print(f"Tipos de dato {type(planeta)}: {type(planeta)}")

paises=[
    "Ecuador",
    "Venezuela",
    "Chile",
    "Colombia",
    "Brasil",
    "Estados Unidos"
]

for pais in paises:
    if pais == "Chile":
        continue
    if pais == "Brasil":
        break
    print(f"Pais visitado: {pais}")

jedi = {}
jedi_activo={
    "nombre": "obiwan",
    "Fuerza": 120,
    "estilo_pelea": "samurai",
    "misiones": ["Guerra alderan", "secuestro palpatine", "escolta de leia"],
    "descripcion": {
        "estatura": 1.80,
        "especie": "humano",
    }
}
print(jedi_activo)
nave=dict(nombre="AZ-1", capacidad=8, turbolaser=2)
print(nave)

jedi["nombre"]="Luck"
jedi["Fuerza"]=150
print(jedi)

for clave,valor in jedi_activo.items():
    print(f"{clave}: {valor}")