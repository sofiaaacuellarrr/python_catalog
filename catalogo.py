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


def ver_marcas():
    print("\nCatalogo de maquillaje:")

    for nombre, informacion in catalogo_maquillaje.items():
        print("\nMarca:", nombre)
        print("Fundadora:", informacion["fundadora"])
        print("Pais:", informacion["pais"])
        print("Cruelty free:", informacion["cruelty_free"])


def modificar_marca():
    nombre = input("Nombre de la marca que desea modificar: ")

    if nombre in catalogo_maquillaje:
        print("1. Modificar fundadora")
        print("2. Modificar pais")
        print("3. Modificar cruelty free")

        opcion = input("Seleccione un atributo: ")

        if opcion == "1":
            nueva_fundadora = input("Nueva fundadora o fundador: ")
            catalogo_maquillaje[nombre]["fundadora"] = nueva_fundadora
            print("Fundadora modificada correctamente")

        elif opcion == "2":
            nuevo_pais = input("Nuevo pais: ")
            catalogo_maquillaje[nombre]["pais"] = nuevo_pais
            print("Pais modificado correctamente")

        elif opcion == "3":
            respuesta = input("Es cruelty free? Escriba si o no: ")

            if respuesta == "si":
                catalogo_maquillaje[nombre]["cruelty_free"] = True
            else:
                catalogo_maquillaje[nombre]["cruelty_free"] = False

            print("Cruelty free modificado correctamente")

        else:
            print("Opcion incorrecta")

    else:
        print("La marca no existe")


opcion = ""

while opcion != "4":
    print("\nMENU")
    print("1. Ver todas las marcas")
    print("2. Agregar una marca")
    print("3. Modificar una marca")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        ver_marcas()

    elif opcion == "2":
        agregar_marca()

    elif opcion == "3":
        modificar_marca()

    elif opcion == "4":
        print("Programa finalizado")

    else:
        print("Opcion incorrecta")
        