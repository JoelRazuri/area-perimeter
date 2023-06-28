""" Implementar algoritmos que permitan:

    a) Calcular el perímetro de un rectángulo dada su base y su altura.
    b) Calcular el área de un rectángulo dada su base y su altura.
    c) Calcular el área de un rectángulo (alineado con los ejes 𝑥 e 𝑦) dadas sus coordenadas
    𝑥1, 𝑥2, 𝑦1, 𝑦2.
    d) Calcular el perímetro de un círculo dado su radio.
    e) Calcular el área de un círculo dado su radio.
    f) Calcular el volumen de una esfera dado su radio.
    g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa."""

import math

print("--------------------------")
print("RECTANGULO")

base = int(input("Ingrese la base del rectangulo:"))
altura = int(input("Ingrese la altura del rectangulo:"))

perimetro = (2*base) + (2*altura)
area = base * altura

print("")
print(f"El rectangulo de base {base} y altura {altura} tiene como perimetro: {perimetro} y área:{area}")
print("--------------------------")
x1 = 0
y1 = 0
x2 = int(input("Ingrese coordenada x2:"))
y2 = int(input("Ingrese coordenada y2:"))

area_2 = x2 * y2

print("")
print(f"El rectangulo con coordenadas x1=0,x2={x2},y1=0 e y2={y2}, tiene area:{area_2}")
print("")
print("--------------------------")
print("CIRCULO")

radio = int(input("Ingrese el radio del circulo:"))

perimetro_cir = 2 * 3.14 * radio
area_cir = 3.14 * radio**2

print("")
print(f"El circulo con radio {radio} tiene perimetro:{perimetro_cir} y area: {area_cir}")
print("")
print("--------------------------")
print("ESFERA")

radio_esfera = int(input("Ingrese el radio de la esfera:"))

volumen = (4/3) * 3.14 * (radio*radio*radio)

print("")
print(f"La esfera con radio {radio_esfera} tiene volumen:{volumen}")
print("")
print("--------------------------")
print("TRIANGULO RECTANGULO")

cateto_1 = int(input("Ingrese un cateto:"))
cateto_2 = int(input("Ingrese el otro cateto:"))

hipotenusa = math.sqrt(cateto_1**2 + cateto_2**2)  # "math.sqrt" funcion para calcular la raiz cuadrada (de la libreria math)

print("")
print(f"El triangulo rectangulo de cateto1 {cateto_1} y cateto2 {cateto_2} tiene hipotenusa: {hipotenusa} ")

