catalogo_maquillaje = {
    "Rare Beauty": {
        "fundadora": "Selena Gomez",
        "pais": "Estados Unidos",
        "cruelty_free": True
    },
    "Fenty Beauty": {
        "fundadora": "Rihanna",
        "pais": "Estados Unidos",
        "cruelty_free": True
    }
}


def agregar_marca():
    nombre = input("Nombre de la marca: ")
    fundadora = input("Fundadora o fundador: ")
    pais = input("Pais de origen: ")
    respuesta = input("Es cruelty free? Escribe si o no: ")

    if respuesta == "si":
        cruelty_free = True
    else:
        cruelty_free = False

    catalogo_maquillaje[nombre] = {
        "fundadora": fundadora,
        "pais": pais,
        "cruelty_free": cruelty_free
    }

    print("Marca agregada correctamente")


agregar_marca()

print("Catalogo actualizado:")
print(catalogo_maquillaje)
