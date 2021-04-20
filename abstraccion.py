#!/usr/bin/python3
import uuid


class Computador:
    def __init__(self, SO: str):
        self.SO = SO
        self._compus = []

    def __crearCompu(self, **kwargs):
        my_dic = {}
        for key, value in kwargs.items():
            my_dic["id"] = str(uuid.uuid4())
            my_dic[key] = value
        if key in ["distribucion", "version"]:
            self._compus.append(my_dic)
        else:
            print(f"los campos permitidos son: \n \t id, distribucion, version")

    def crear_computador(self, **kwargs):
        self.__crearCompu(**kwargs)

    def listarCompus(self):
        for index in range(0, len(self._compus)):
            print("*" * 30)
            print(f"{index}) ---> {self._compus[index]}\n")
        print(f"El total de computadores que hay es: {len(self._compus)}")


linux = Computador("Linux")
linux.crear_computador(distribucion="ubuntu", version="20.04")
linux.crear_computador(distribucion="debian", version="16.04")
linux.listarCompus()
"""
salida ===>

******************************
0) ---> {'id': 'ead163d2-1041-442c-ab85-16cdca7d9302', 'distribucion': 'ubuntu', 'version': '20.04'}

******************************
1) ---> {'id': '6ec46614-031b-4b66-8817-a1a9f5497dd3', 'distribucion': 'debian', 'version': '16.04'}

El total de computadores que hay es: 2
"""
