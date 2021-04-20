#!/usr/bin/python3


class Persona():
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"hola {self.nombre}"


daniela = Persona("daniela")
print(daniela.saludar())
