# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gi7F0YpZBU0hKrg0XPYrbBbkr2uuhJFI
"""

'''
Clase:        Clase 1
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    Identificador de la clase
Descripción:  Definición del ejercicio

Autor:        Rodrigo Lazo
Fecha:        2025-05-14
Estado:       [ Terminado ]
'''
total_de_cuenta = int(input("Ingrese su cuenta total: "))
porcentaje_de_propina = int(input("Ingresa el porcentaje de propina: "))
total_cuenta_con_propina = total_de_cuenta + total_de_cuenta*(porcentaje_de_propina/100)
print(total_cuenta_con_propina)

'''
Clase:        Clase 1
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    Identificador de la clase
Descripción:  Definición del ejercicio

Autor:        Rodrigo Lazo
Fecha:        2025-05-14
Estado:       [ Terminado ]
'''
nombre = input("Ingresa tus nombres: ")
nombres = nombre.split()
primer_nombre = nombres[0]
apellido = input("ingrese su apellido: ")
apellidos = apellido.split()
primer_apellido = apellidos[0]

correo = (f"{primer_nombre}.{primer_apellido}@keyinstitute.edu.sv")
print(correo.lower())

'''
Clase:        Clase 2
Tema:         Bloque condicional
Ejercicio:    Identificador de la clase
Descripción:  Definición del ejercicio

Autor:        Rodrigo Lazo
Fecha:        2025-05-16
Estado:       [ Terminado ]
'''
contrasena = input("Ingrese su clave: ")

if len(contrasena) >= 8:
    for i in contrasena:
        if i.isupper():
            si_hay_mayuscula = True
            if si_hay_mayuscula:
                for c in contrasena:
                    if c.isdigit():
                        print("Contraseña segura")
                        break
                else:
                    print("Contraseña no segura")
            break
    else:
        print("Contraseña no segura")
else:
    print("Contraseña no segura")

'''
Clase:        Clase 2
Tema:         Bloque condicional
Ejercicio:    Identificador de la clase
Descripción:  Definición del ejercicio

Autor:        Rodrigo Lazo
Fecha:        2025-05-16
Estado:       [ Terminado ]
'''
consumo = int(input("Agrege su consumo: "))
if consumo <= 100:
  print("Sin impusto")
elif consumo in range(101, 200):
  rango1 = consumo * 0.5
  print(rango1)
elif consumo >= 201:
  rango2 = consumo * 0.7
  print(rango2)

'''
Clase:        Clase 2
Tema:         Bloque condicional
Ejercicio:    Identificador de la clase
Descripción:  Definición del ejercicio

Autor:        Rodrigo Lazo
Fecha:        2025-05-16
Estado:       [ Terminado ]
'''
numero = int(input("Ingresa un numero: "))
if numero % 7 == 0 and numero % 5 != 0:
  print("Magico")
else:
  print("No magico")