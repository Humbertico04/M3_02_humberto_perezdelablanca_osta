from ast import main

print("Ejercicio 1:\n")

def error_division_0(divisor, dividendo):
    try:
        numero = divisor / dividendo
        return numero
    except ZeroDivisionError:
        print("No se puede evaluar la división de un número entre 0") 

error_division_0(7, 0)

if __name__ == "__main__":
    main()