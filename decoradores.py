#!/usr/bin/python3

"""
Creando mi propio decorador
y entendiendolos

¿ Qué es un decorador ?
    - Un decorador básicamente toma una función,
        le añade alguna funcionalidad y la retorna.
"""


# Ejemplo:
def funcion_decorador(funcion):
    def wrapper():
        print("llamando a mi funcion")
        funcion()
        print("finalizo llamado")
    return wrapper


"""
(@funcion_decorador) es lo mismo que =>
ejemplo = funcion_decoradora(ejemplo) => print(ejemplo())
solo que usando la sintaxis que nos permite usar python con el "@"
"""


@funcion_decorador
def ejemplo():
    print("soy una funcion ejemplo que tendra una nueva funcionalidad cuando sea llmada!")


print(ejemplo())
"""
SALIDA DEL PROGRAMA:

llamando a mi funcion
soy una funcion ejemplo que tendra una nueva funcionalidad cuando sea llmada!
finalizo llamado

"""
