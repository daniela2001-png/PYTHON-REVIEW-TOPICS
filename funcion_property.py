#!/usr/bin/python3

"""
Qué es la función property?

Función property():
Esta función está incluida en Python, en particular crea y retorna
la propiedad de un objeto.
La propiedad de un objeto posee los métodos getter(), setter() y del().

En tanto la función tiene cuatro atributos: property(fget, fset, fdel, fdoc) :

fget : trae el valor de un atributo.
fset : define el valor de un atributo.
fdel : elimina el valor de un atributo.
fdoc : crea un docstring por atributo.
Veamos un ejemplo del mismo caso implementando la función property() :
"""


class Millas:
    # def __init__(self):
    #     self._distancia = 0

    # # Función para obtener el valor de _distancia
    # def obtener_distancia(self):
    #     print("Llamada al método getter")
    #     return self._distancia

    # # Función para definir el valor de _distancia
    # def definir_distancia(self, recorrido):
    #     print("Llamada al método setter")
    #     self._distancia = recorrido

    # # Función para eliminar el atributo _distancia
    # def eliminar_distancia(self):
    #     del self._distancia

    # distancia = property(
    #     obtener_distancia, definir_distancia, eliminar_distancia)
    def __init__(self):
        self._distancia = 0

    # Función para obtener el valor de _distancia
    # Usando el decorador property
    @property
    def obtener_distancia(self):
        print("Llamada al método getter")
        return self._distancia

    # Función para definir el valor de _distancia
    @obtener_distancia.setter
    def definir_distancia(self, valor):
        if valor < 0:
            raise ValueError(
                "No es posible convertir distancias menores a 0.")
        print("Llamada al método setter")
        self._distancia = valor


# Creamos un nuevo objeto
avion = Millas()
print(avion.obtener_distancia) # 0
print(avion.definir_distancia)
avion._distancia = 200
print(avion.obtener_distancia) # 200