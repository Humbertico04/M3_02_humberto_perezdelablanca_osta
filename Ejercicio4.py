from ast import main

print("Ejercicio 4:\n")

def error_suma_tipos(*args):
    suma = 0
    for arg in args:
        try:
            suma += arg
        except TypeError:
            print('No se puede sumar un string a un int/float, pruebe a quitar las "" del numero {} y pruebe de nuevo'.format(arg))
    return suma

error_suma_tipos("2", 10)

if __name__ == "__main__":
    main()