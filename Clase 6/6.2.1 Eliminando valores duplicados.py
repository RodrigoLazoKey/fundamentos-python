# -*- coding: utf-8 -*-
"""Clase 6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mgugd8u0L05BYHtw0RTdJEj2Zp9H9Tek
"""

'''
Clase:        Clase 6
Tema:         Manejo de listas
Ejercicio:    Eliminando valores duplicados
Descripción:  Dada una lista ingresada por el usuario, elimina los elementos duplicados manteniendo la primera aparición de cada número.

Autor:        Rodrigo Lazo
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''
lista_ingresada = list(map(int, input("Ingrese los datos").split()))
lista_sin_repetir = []

for i in lista_ingresada:
  if i not in lista_sin_repetir:
        lista_sin_repetir.append(i)

print(lista_sin_repetir)