nada = None
cadena = "Hola soy Juan"
cadena = "Desarrollador web"
entero = 99
flotante = 3.14
booleano = True
lista = [1, 2, 3, 4, 5]
listaStrings = ["Hola", "Mundo", "desde", "Python", 20]
tuplaNoCambia = ("Master", "en", "Python")
diccionario = {
    "nombre"   : "Juan",
    "apellido" : "Hernandez",
    "curso"    : "Master en Python",
    "edad"     : 22
}
rango = range(9)
dato_byte = b"Probando el byte"

# Iprimir variables
print(nada)
print(cadena)
print(entero)
print(flotante)
print(booleano)
print(lista)
print(listaStrings)
print(tuplaNoCambia)
print(diccionario)
print(rango)
print(dato_byte)

# Mostrar tipo de dato
print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(lista))
print(type(listaStrings))
print(type(tuplaNoCambia))
print(type(diccionario))
print(type(rango))
print(type(dato_byte))


# Convertir tipo de datos
texto = "Soy un texto"
numerito = 775

print(texto + " " + str(numerito))
# print(f"{texto} {numerito}")