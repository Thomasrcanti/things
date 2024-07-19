# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:17:32 2024

@author: Administrator
"""

name = "Thomas Ruiz Canti"
print(name.split(maxsplit=-1))

def nametomays(lista):
    cons = "bcdfghjklmnpqrstvwxyz"
    mod_names = []
    for name in lista:
        new_name = ""
        for char in name:
            if char.lower() in cons:
                new_name += char.upper()
            else:
                new_name += char
        mod_names.append(new_name)
    return mod_names

lista = ["Thomas", "Ruiz", "Canti"]

mod = nametomays(lista)
print(mod)