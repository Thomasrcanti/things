# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 19:14:32 2024

@author: Administrator
"""
def contador_palabra(archivo, palabras):
    conteo = {palabra: 0 for palabra in palabras}
    try:
        with open(archivo, 'r') as file:
            for linea in file:
                for palabra in palabras:
                    if palabra in linea.lower().split():
                        conteo[palabra] += 1
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None

    return conteo

archivo = 'ds.txt'
lista_de_palabras = ['uruguay', "Lorem", "Ipsum", "texto"]

conteo = contador_palabra(archivo, lista_de_palabras)
print(conteo)