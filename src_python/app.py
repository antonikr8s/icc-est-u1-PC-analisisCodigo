#Ejecutar benchMarking
#from benchmarking import Benchmarking
import matplotlib.pyplot as plt
from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento

if __name__ == "__main__":
    print("Funciona")
    #instancias
    metodos=MetodosOrdenamiento()
    benchmark = Benchmarking()
    
    tam=10000
    arreglo_base=benchmark.build_arreglo(tam)
    
    #diccionario llamado metodos
    #tenga 2 elementos
    #1 - clave = burbuja valor la funcion sin()
    #2 - clave seleccion valor la funcion sin ()
    
    metodos={#hacemios un diccionario
        "burbuja": metodos.sortByBubble,#no le pongo un parentesis para no ejecutar la funcion
        "seleccion":metodos.sortBySeleccion,
    }
    resultados=[]
    for nombre, metodo in metodos.items():#items me da una tupla donde nombre=burbuja y metodo = sortBubble
        tiempo=benchmark.medir_tiempo(metodo, arreglo_base)
        tupResultado=(tam,nombre,tiempo)#tamano:10000 nombre=burbuja tiempo=tiempo
        resultados.append(tupResultado)
        
    #for resultado in resultados:
    #    tam,nombre,tiempo=resultado
    #    print(f"Tamano: {tam}, Metodo: {nombre}, Tiempo: {tiempo:.6f} segundos")
    
    
    # Imprimir resultados
    print("\n===== RESULTADOS =====")
    for tam, nombre, tiempo in resultados:
        print(f"Tamaño: {tam}, Metodo: {nombre}, Tiempo: {tiempo:.6f} segundos")

    # Preparar datos para graficar
    nombres = [nombre for _, nombre, _ in resultados]
    tiempos = [tiempo for _, _, tiempo in resultados]

    # Graficar
    plt.figure(figsize=(8, 5))
    plt.bar(nombres, tiempos, color=['skyblue', 'lightgreen'])
    plt.title("Comparacion de algoritmos de ordenamiento")
    plt.xlabel("Metodo")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.tight_layout()
    plt.grid(axis='y')
    plt.show()


#-> benchmarking es un archivo
# Diccionario guarda valores
# Tuplas() no se pueden modificar

