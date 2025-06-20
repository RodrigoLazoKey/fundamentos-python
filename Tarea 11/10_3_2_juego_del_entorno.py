# -*- coding: utf-8 -*-
"""10.3.2. Juego del entorno.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Za8GPkve6Bdu1d43uOXNDa8ghvYCDeUO
"""

'''
Clase:        Clase 10
Tema:         Matrices
Ejercicio:    10.3.2. Juego del entorno
Descripción:  Dada una matriz binaria ingresada por el
              usuario, verifica para cada celda de una
              matriz binaria cuántos elementos con valor
              de 1 hay en las celdas vecinas (arriba, abajo,
              izquierda, derecha, diagonales).

Autor:        Rodrigo Lazo
Fecha:        2025-06-11
Estado:       [ Terminado ]
'''
n = int(input("Ingrese el número de filas: "))
m = int(input("Ingrese el número de columnas: "))
def contar_unos_vecinos(matriz, n, m):
    direcciones = [(-1,-1), (-1,0), (-1,1),
                   (0,-1),         (0,1),
                   (1,-1),  (1,0),  (1,1)]

    resultado = []

    for i in range(n):
        fila_resultado = []
        for j in range(m):
            conteo = 0
            for xd, dx in direcciones:
                no, si = i + xd, j + dx
                if 0 <= no < n and 0 <= si < m:
                    if matriz[no][si] == 1:
                        conteo += 1
            fila_resultado.append(conteo)
        resultado.append(fila_resultado)

    return resultado

matriz = []
for u in range(n):
    fila = list(map(int, input().split(',')))
    matriz.append(fila)

resultado = contar_unos_vecinos(matriz, n, m)

for fila in resultado:
    print(fila)