#Ejercicio Python - POO2 M4S2

class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso

    # Métodos GET
    def get_nombre(self):
        return self.__nombre

    def get_raza(self):
        return self.__raza

    def get_edad(self):
        return self.__edad

    def get_peso(self):
        return self.__peso

    # Métodos SET
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_raza(self, raza):
        self.__raza = raza

    def set_edad(self, edad):
        self.__edad = edad

    def set_peso(self, peso):
        self.__peso = peso

# Crear instancias de la clase Animal
caballo = Animal("Zeus", "Pura sangre", 5, 450)
leon = Animal("Boulder", "Atlas", 10, 130)

# Mostrar información
print(f"Caballo: {caballo.get_nombre()}, Raza: {caballo.get_raza()}, Edad: {caballo.get_edad()} años, Peso: {caballo.get_peso()} kg.")
print(f"León: {leon.get_nombre()}, Raza: {leon.get_raza()}, Edad: {leon.get_edad()} años, Peso: {leon.get_peso()} kg.")
