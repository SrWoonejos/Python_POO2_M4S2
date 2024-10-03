class Persona:
    def __init__(self, nombre, apellido, sexo, edad, estatura, peso):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sexo = sexo
        self.__edad = edad
        self.__estatura = estatura
        self.__peso = peso

    #getters
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_sexo(self):
        return self.__sexo
    
    def get_edad(self):
        return self.__edad
    
    def get_estatura(self):
        return self.__estatura
    
    def get_peso(self):
        return self.__peso
    
    #setters
    def set__nombre(self, nombre):
        self.__nombre = nombre

    def set__apellido(self, apellido):
        self.__apellido = apellido

    def set__sexo(self, sexo):
        self.__sexo = sexo

    def set__edad(self, edad):
        self.__edad = edad

    def set__estatura(self, estatura):
        self.__estatura = estatura

    def set__peso(self, peso):
        self.__peso = peso

#instancia clase Persona
persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.80, 75)

#sett - modificar atributos
persona_1.set__edad(21)
persona_2.get_apellido("Santiago")

#mostrar actualizaciones sett
print(f"Persona 1: {persona_1.get_nombre()}, {persona_1.get_apellido()}, {persona_1.get_sexo()}, {persona_1.get_edad()} años, {persona_1.get_estatura()} mts, {persona_1.get_peso()} kg.")
print(f"Persona 2: {persona_2.get_nombre()}, {persona_2.get_apellido()}, {persona_2.get_sexo()}, {persona_2.get_edad()} años, {persona_2.get_estatura()} mts, {persona_2.get_peso()} kg.")