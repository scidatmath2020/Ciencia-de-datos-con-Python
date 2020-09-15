# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 12:36:52 2020

@author: hp
"""

"""Python es un lenguaje orientado a objetos. Una de las grandes ventajas de 
esto radica en el uso de clases.

Las clases en Python 3 tienen la sintaxis

class NombreDeLaClase:
    def metodo1(self):  -->todos los métodos de la clase toman "self" como su primer argumento
        #definición  del método
    
    def metodo2(self):
        #definición del método
        
"""

#%%

class CarroBásico:
    def girar_izquierda(self):
        print("Girando a la izquierda")
    
    def girar_derecha(self):
        print("Girando a la derecha")
        
    def acelerar(self):
        #podemos usar pass cuando definimos una función que no hace nada
        pass
    
    def frenar(self):
        pass
        
print(CarroBásico)
#%%
"""Las clases se pueden considerar como plantillas que se pueden usar para 
generar objetos. Los objetos generados por una clase se conocen como instancias.

Por ejemplo, CarroBásico nos da las instrucciones para fabricar un coche."""

monchito = CarroBásico()
print(monchito)

type(monchito)

#%%
""" Como monchito es una instancia de CarroBásico, tiene sus métodos"""

monchito.girar_izquierda()
monchito.girar_derecha()
monchito.acelerar()
monchito.frenar()

#%%

""" 
Al igual que con las funciones, generalmente vamos a querer que nuestros objetos
tengan características variables. Con la clase CarroBásico todos nuestros carros
serán 100% iguales. Pero qué pasa si queremos que nuestros carros tengan un color.

Para ello usamos el método especial __init__ que se ejecuta cuando se instancia una clase
"""

class CarroConColor:
    def __init__(self,color):
        self.color = color # Esto es un atributo
        
    def describir(self):
        print(f"Carro de color {self.color}")
    
    def girar_izquierda(self):
        print("Girando a la izquierda")
    
    def girar_derecha(self):
        print("Girando a la derecha")
        
    def acelerar(self):
        #podemos usar pass cuando definimos una función que no hace nada
        pass
    
    def frenar(self):
        pass    
    
#%%
        
monchito_rojo = CarroConColor(color = "rojo") 

monchito_rojo.describir()   

#%%

"""
También podemos añadir atributos a las instancias
"""

monchito_rojo.matricula = "ABC123"

monchito_rojo.matricula

#%%
"""Al crear un CarroConColor sí o sí debemos especificar el color"""

monchito_sin_color = CarroConColor()

#%%

"""
Podemos evitar esto simplemente usando valores por defecto en el método __init__"""

class CarroConColor:
    def __init__(self,color = "negro"):
        self.color = color # Esto es un atributo
        
    def describir(self):
        print(f"Carro de color {self.color}")
    
    def girar_izquierda(self):
        print("Girando a la izquierda")
    
    def girar_derecha(self):
        print("Girando a la derecha")
        
    def acelerar(self):
        #podemos usar pass cuando definimos una función que no hace nada
        pass
    
    def frenar(self):
        pass    


monchito_sin_color = CarroConColor()

monchito_sin_color.color
monchito_sin_color.describir()

#%%

"""
También podemos definir todas las variables que necesitamos para definir un objeto
"""

class CarroVariable:
    def __init__(self,modelo, velocidad_maxima, color = "negro"):
        self.color = color # Esto es un atributo
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0 #el carro está detenido
        
    def describir(self):
        descripcion = f"Carro modelo {self.modelo} de color {self.color} con velocidad máxima de {self.velocidad_maxima} km/h"
        return descripcion
    
    def estado(self):
        if self.velocidad == 0:
            print("El carro está detenido")
        else:
            print(f"El carro va a {self.velocidad} km/h")
    
    def girar_izquierda(self):
        print("Girando a la izquierda")
    
    def girar_derecha(self):
        print("Girando a la derecha")
        
    def acelerar(self):
        #podemos usar pass cuando definimos una función que no hace nada
        pass
    
    def frenar(self):
        pass    
    
#%%    
monchito = CarroVariable(modelo = "Bora", velocidad_maxima = 250, color = "plateado")

monchito.describir()

monchito.estado()

monchito.velocidad = 120

monchito.estado()



#%%
"""
Uno de los principales usos de las clases es conservar el "estado actual" de un objeto. 
"""

class Carro:
    def __init__(self,modelo, velocidad_maxima, color = "negro"):
        self.color = color # Esto es un atributo
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0 #el carro está detenido
        
    def describir(self):
        descripcion = f"Carro modelo {self.modelo} de color {self.color} con velocidad máxima de {self.velocidad_maxima} km/h"
        return descripcion
    
#    def __repr__(self):
#        return self.describir()
    
    def estado(self):
        if self.velocidad == 0:
            print("El carro está detenido")
        elif self.velocidad > 0:
            print(f"El carro va a {self.velocidad} km/h")
        else:
            print(f"El vehículo va marcha atrás a {-self.velocidad} km/h")
            
    def girar_izquierda(self):
        print("Girando a la izquierda")
    
    def girar_derecha(self):
        print("Girando a la derecha")
        
    def acelerar(self,diferencia_velocidad):
        if diferencia_velocidad >= 0:
            print(f"Subiendo la velocidad en {diferencia_velocidad} km/h")
            self.velocidad = self.velocidad + diferencia_velocidad
            self.velocidad = min(self.velocidad,self.velocidad_maxima)
        else:
            print("No se puede acelerar negativamente")
            
    def frenar(self,diferencia_velocidad):
        if diferencia_velocidad >= 0:
            print(f"Frenando en {diferencia_velocidad} km/h")
            self.velocidad = self.velocidad - diferencia_velocidad
            self.velocidad = max(self.velocidad,-5)    
    
#%%
        
monchito = Carro(modelo = "Bora", velocidad_maxima = 250, color = "plateado")

print(abc)

monchito.velocidad = -5

monchito.estado()

monchito.acelerar(-300) 

monchito.estado()

monchito.acelerar(50)

monchito.estado()

monchito.frenar(-10)

monchito.frenar(10)

monchito.estado()

monchito.frenar(100)

monchito.estado()

#%%

"""
Herencia de clases

Una de las principales ventajas de usar clases es que se pueden crear otras clases utilizando las ya creadas. Se dice que
una clase hereda a la otra.

Esto nos permite crear una clase genérica después crear clases mas avanzadas con funcionalidades específicas
"""

class Autobús(Carro):
    def acelerar(self,diferencia_velocidad):
        if diferencia_velocidad >= 0:
            print(f"Subiendo la velocidad en {diferencia_velocidad} km/h")
            self.velocidad = self.velocidad + diferencia_velocidad
            self.velocidad = min(self.velocidad,100)
        else:
            print("No se puede acelerar negativamente")
            
    def frenar(self,diferencia_velocidad):
        if diferencia_velocidad >= 0:
            print(f"Frenando en {diferencia_velocidad} km/h")
            self.velocidad = self.velocidad - diferencia_velocidad
            self.velocidad = max(self.velocidad,0)