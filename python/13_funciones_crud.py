flota = [
    {
        "N1-001": {
            "nombre": "Caza N-1",
            "combustible": 80
        }
    },
    {
        "N2-002": {
            "nombre": "Nave Real",
            "combustible": 35
        }
    }
]

def create_nave(nave):
    flota.append(nave)


def update_nave(nave_updated, index):
    flota[index].update(nave_updated)


def read_nave(index):
    return flota[index]

def delete_nave(index):
    return flota.pop(index)

print(flota)

new_nave = {
        "N2-003": {
            "nombre": "Nave Real 2",
            "combustible": 85
        }
    }

create_nave(new_nave)
print(flota)
new_updated = {
        "N2-006": {
            "nombre": "Nave Real NR6",
            "combustible": 50
        }
    }
update_nave(new_updated, 2)
print(flota)
print(read_nave(2))
print(delete_nave(2))
print(flota)

