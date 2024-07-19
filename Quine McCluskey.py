import threading
import random

# Crear un lock para sincronización
lock = threading.Lock()

# Variable para controlar si se ha encontrado al ganador
ganador_encontrado = False

def corredor(nombre):
    global ganador_encontrado
    
    distancia_recorrida = 0
    
    while distancia_recorrida < 100 and not ganador_encontrado:
        distancia_avance = random.randint(1, 5)
        distancia_recorrida += distancia_avance

    # Adquirir el lock antes de imprimir el mensaje de llegada
    with lock:
        if not ganador_encontrado:
            ganador_encontrado = True
            print(f"¡{nombre} ha llegado a la meta y es el ganador!")

# Crear dos threads para los corredores
corredor1_thread = threading.Thread(target=corredor, args=("Corredor 1",))
corredor2_thread = threading.Thread(target=corredor, args=("Corredor 2",))

# Iniciar la carrera
corredor1_thread.start()
corredor2_thread.start()

# Esperar a que al menos un corredor llegue a la meta
corredor1_thread.join()
corredor2_thread.join()

print("Carrera finalizada")