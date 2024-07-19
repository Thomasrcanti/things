# -*- coding: utf-8 -*-
"""
Created on Mon May 27 19:04:13 2024

@author: Administrator
"""

from multiprocessing import Process, Queue
def proceso_productor(cola):
    cola.put("Dato 1")
    cola.put("Dato 2")
def proceso_consumidor(cola):
    dato1 = cola.get()
    dato2 = cola.get()
    print(dato1) # Resultado: Dato 1
    print(dato2) # Resultado: Dato 2
    

# Crear una cola
cola_compartida = Queue()
# Crear procesos
productor = Process(target=proceso_productor, args=(cola_compartida,))
consumidor = Process(target=proceso_consumidor, args=(cola_compartida,))
# Iniciar los procesos
productor.start()
consumidor.start()
# Esperar a que los procesos terminen
productor.join()
consumidor.join()