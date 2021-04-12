#!/usr/bin/python3

"""
Crearemos una clase Hotel() que tendrá 3 métodos :
    1) añadir-huesped
    2) eliminar-huesped
    3) contar-huesped

y claro nuestro constructor que tomará 2 argumentos principales:
    1) numero_maximo_de_huespedes
    2) lugares_de_estacionamiento

a adicional en nuestro constructor tendremos un objeto huesped
que sera bien sea una lista que me vaya agregando el numero de huespeds
o solo sea un int
"""


class Hotel():
    # definimos nuestro constructor de la clase Hotel
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.huespeds = []

    def añadir_huesped(self, *args):
        self.huespeds.append(args)

    def listar_huespeds(self):
        if len(self.huespeds) > 0:
            for i in self.huespeds:
                return 'En total hay: {} huespeds!'.format(len(i))
        else:
            return 'Aun no se han añadido huespeds a este hotel!'


hotel = Hotel(50, 30)
hotel.añadir_huesped('1193128170', '1193128173', '1194128170', '1193528170')
print(hotel.listar_huespeds())
