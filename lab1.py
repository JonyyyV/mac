# Laboratorio 1 de MAC


import math
import numpy


# Ejercicio 1

v = 0

while int(v) >= 0:
    print("Introduce un valor negativo")
    v = input()
print(abs(int(v)))

# Ejercicio 2

print("\nIntroduce primer sumando")
s1 = int(input())
print("Introduce segundo sumando")
s2 = int(input())
print(s1 + s2)


# Ejercicio 3

print("\nIntroduce el valor que deseas convertir de Cº a Farenheit")
tCelsius = float(input())
print((9/5) * tCelsius + 32)

# Ejercicio 4

print("\nIntroduce el radio de la esfera")
print(4 * math.pi * math.pow(float(input()),2))

# Ejercicio 5

print("\nIntroduce a")
a = float(input())

print("\nIntroduce b")
b = float(input())

print("\nIntroduce c")
c = float(input())

assert a == b
assert b < c
assert c > a

# Ejercicio 6

print("\nIntroduce el x del primer punto")
x1 = float(input())
print("\nIntroduce el y del primer punto")
y1 = float(input())
print("\nIntroduce el x del segundo punto")
x2 = float(input())
print("\nIntroduce el y del segundo punto")
y2 = float(input())

print(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))

# Ejercicio 7
print("\nIntroduce primer valor")
x = int(input())
print("Introduce segundo valor")
y = int(input())
print(5 * math.pow(x,3) + math.sqrt(math.pow(x,2) + math.pow(y,2)) + math.pow(math.e,math.log(x)))

# Ejercicio 8

lista = [ 1, 2, 3, 4, 5]

# Es un vector de int. Si se puede considerar

# Ejercicio 9

lista4 = [ 1, 2, 3, 4, 5, 4, 4, 56, 6]
print(lista4)
for index, value in enumerate(lista4):
    if value == 4:
      lista4[index] = 10

print(lista4)

#Ejercicio 10

lista =  [6, 11, 27, 32, 33]
contador = 0

for index, value in enumerate(lista):
    while(lista[index] != 1):
        if(lista[index] % 2 == 0):
            contador = contador + 1
            lista[index] = lista[index] / 2
        else:
            contador = contador + 1
            lista[index] = ( lista[index] * 3 ) + 1
    lista[index] = contador
    contador = 0
    print(lista[index])

# Ejercicio 11


