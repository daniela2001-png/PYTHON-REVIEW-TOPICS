#!/usr/bin/python3

class Coordenada:
    """
    clase que calcula la ditancia entre 2 puntos
    usando la formula:
    distancia = √ ( (x_2-x_1) ² + (y_2-y_1) ² )
    para calcular la distancia entre cualesquiera dos puntos
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_cordenada):
        x_diff = (self.x - otra_cordenada.x) ** 2
        y_diff = (self.y - otra_cordenada.y) ** 2
        # retornamos el resultado final que es el calculo
        # de la distancia entre dos puntos (x) y (y)
        return ((x_diff + y_diff) ** (1/2))


if __name__ == "__main__":
    cordenada_1 = Coordenada(4, 8)
    cordenada_2 = Coordenada(20, 10)
    # imprimimos la distancia entre el punto 1 y 2
    # 16 aproximado será la distancia entre estas coordenadas
    print(cordenada_1.distancia(cordenada_2))
    # isinstacne para saber si un objeto creado es instancia o no de un clase
    print(isinstance(cordenada_2, Coordenada))  # deberia retornar True!
