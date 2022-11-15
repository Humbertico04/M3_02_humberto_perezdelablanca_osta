def error_elemento_fuera_lista(lista, elemento_lista):
    try:
        elemento = lista[elemento_lista]
        return elemento
    except IndexError:
        print("No se puede acceder al elemento {} de lista porque solo tiene {} elementos".format(elemento_lista, len(lista)))

error_elemento_fuera_lista([4, 7, 30, 23, 5], 10)