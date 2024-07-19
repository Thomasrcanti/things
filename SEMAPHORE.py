from threading import Semaphore, Thread
import time
from random import randint

class SalaEspera:
    def __init__(self, cp=5):
        self.capacidad_maxima = cp
        self.sem = Semaphore(cp)
        self.cant = 0

    def entrar(self):
        self.sem.acquire()
        self.cant += 1
        print(f"+1. {self.cant}/{self.capacidad_maxima}")

    def salir(self):
        if self.cant > 0:
            self.sem.release()
            self.cant -= 1
            print(f"-1. {self.cant}/{self.capacidad_maxima}")
        else:
            print("Sala vacia.")

    def obtener_cantidad_actual(self):
        print(f"Cantidad actual de personas: {self.cant}")

def simular():
    sala_espera = SalaEspera()

    def generar():
        decision = randint(0, 1)
        if decision == 0:
            sala_espera.salir()
        else:
            sala_espera.entrar()
        time.sleep(tiempo)

    for i in range(6):
        Thread(target=generar).start()
        time.sleep(tiempo)

    time.sleep(7)
    sala_espera.obtener_cantidad_actual()

tiempo = randint(1, 4)
simular()