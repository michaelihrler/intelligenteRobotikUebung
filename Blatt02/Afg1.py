
from math import sqrt,arcos

import numpy as np

class Vector2D:
    def __init___(self,x:float ,y:float):
        self.x=x
        self.y=y

    def null_vektor(self):
        self.x *=0
        self.y *=0

    def skalar_multiplikation(self, skalar):
        self.x *= skalar
        self.y *= skalar
    
    def vektor_negation(self):
        self.x *= -1
        self.y *= -1

    def Laenge(self):
        return sqrt(self.x^2 + self.y^2)
        
def vektor_addition(a: Vector2D, z: Vector2D):
    new_x = a.x + z.x
    new_y = a.y + a.x
    return Vector2D(new_x,new_y)

def vektor_substraktion(a: Vector2D, z: Vector2D):
    new_x = a.x - z.x
    new_y = a.y - a.x
    return Vector2D(new_x,new_y)

def skalar_produkt(a: Vector2D, z: Vector2D):
    return (a.x * z.x) + (a.y * z.y)

def isvectorequal(a: Vector2D, z: Vector2D):
    return bool(a==z)

def kreuz_produkt(a: Vector2D, z: Vector2D):
    return (a.x * z.y - a.y * z.x)

def winkel_berechnung(a: Vector2D, z: Vector2D):
    return (arcos(skalar_produkt(a,z))/(a.Laenge()*z.Laenge()))


class Matrix33d():
    def __init__(self, a: np.array):
        self.a = a

    def null_vektor(self):
        self.a *= 0

    def einheits_matrix(self):
        self.null_vektor(self.a)
        self.a[0[0]]=1
        self.a








