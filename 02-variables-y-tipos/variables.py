"""
    Una variable es un contenedor de información
    que dentro guarda un dato, se pueden crear 
    muchas variables y que cada una tenga unos datos distintos
"""

# Crear variables y asignar un valor
# Mostrar variables en pantalla
texto = "Master en Python"
print(texto)

numero = 45
print(numero)

decimal = 13.3
print(decimal)


# Concatenacion
nombre = "Juan Francisco"
apellidos = "Hernandez Sebastian"
print(nombre + " " + apellidos)

# Interpolacion de strings o string template
print(f"{nombre} {apellidos}")

print("Hola me llamo {} {}".format(nombre, apellidos))