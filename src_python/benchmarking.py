

# benchmarking.py
import random
import time
from metodos_ordenamiento import MetodosOrdenamiento


class Benchmarking:
    def __init__(self):
        print("Benchmarking inicializado...")
        self.mOrdenamiento = MetodosOrdenamiento()
        
        arreglo=self.build_arreglo(1000)
        
        tarea=lambda: self.mOrdenamiento.sortByBubble(arreglo)
        
        tiempoMillis=self.contar_con_current_time_milles(tarea)
        tiempoNano=self.contar_con_nano_time(tarea)
        
        print(f'Tiempo en milisegundos: {tiempoMillis:.3f} ms')
        print(f'Tiempo en nanosegundos: {tiempoNano} ns')
            #tarea=()->

    def build_arreglo(self, tamanio):
        array = []
        for i in range(tamanio):
            numero = random.randint(0, 99999)
            array.append(numero)
        return array
    
    
    #x = time.time()
    def contar_con_current_time_milles(self, tarea):
        inicio = time.time()  # segundos con decimales
        tarea()               # ejecuta la función
        fin = time.time()
        
        return (fin - inicio) * 1000
        
    
    
    #x=tome.time_ns()
    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
         # ya está en nanosegundos
        return fin-inicio
