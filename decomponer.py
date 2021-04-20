#!/usr/bin/python3

class Auto:
    def __init__(self, modelo: str, marca: str, placa: str):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.motor = Motor(4).info_motor()

    def encender(self, bool: bool) -> str:  # esta funcion retornara un 'str'
        result = "El auto esta encendido" if bool else "El auto esta apagado"
        return result


class Motor:
    def __init__(self, num_cilindros: int, tipo="gasolina"):
        self.num_cilindros = num_cilindros
        self.tipo = tipo
        self.__temperatura = 20

    def info_motor(self) -> str:  # esta funcion retornara un 'str'
        return f"Su motor es tipo {self.tipo} y tiene {self.num_cilindros} cilindros"


if __name__ == "__main__":
    auto = Auto(modelo="hi", marca="bmw", placa="BTL357")
    print(auto.motor)
    motor = Motor(4)
    print(motor.info_motor())
    # si queremos acceder al valor que tiene la varibale privada "temperatura"
    # solo miramos con el metodo dir(objeto) de como esta reescrita esa
    #  instacia
    # print(dir(motor))  # _Motor__temperatura
    # aqui hemos accedido al valor de la variable privada :3
    print(motor._Motor__temperatura)
    print(auto.encender(True))  # El auto esta encendidoç
