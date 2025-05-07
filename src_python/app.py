#Ejecutar benchMarking
#from benchmarking import Benchmarking
import matplotlib.pyplot as plt
from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento
from datetime import datetime

if __name__ == "__main__":
    print("Funciona")
    #instancias
    metodos = MetodosOrdenamiento()
    benchmark = Benchmarking()

    tamanios = [500, 1000, 2000]
    resultados = []

    #diccionario llamado metodos
    #tenga 2 elementos
    #1 - clave = burbuja valor la funcion sin()
    #2 - clave seleccion valor la funcion sin ()
    
    for tam in tamanios:
        arreglo_base = benchmark.build_arreglo(tam)
        metodos_dic = {
            "burbuja": metodos.sortByBubble,
            "seleccion": metodos.sortBySeleccion,
        }
        for nombre, fun_metodo in metodos_dic.items(): #items me da una tupla donde nombre=burbuja y metodo = sortBubble
            tiempo_resultado = benchmark.medir_tiempo(fun_metodo, arreglo_base)
            resultados.append((tam, nombre, tiempo_resultado))

    #for resultado in resultados:
    #    tam,nombre,tiempo=resultado
    #    print(f"Tamano: {tam}, Metodo: {nombre}, Tiempo: {tiempo:.6f} segundos")
     

    print("\n===== RESULTADOS =====")
    for tam, nombre, tiempo in resultados:
        print(f"Tamaño: {tam}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos")

    tiempos_by_metodo = { "burbuja": [], "seleccion": [] }
    for nombre in tiempos_by_metodo:
        for tam in tamanios:
            for r_tam, r_nombre, r_tiempo in resultados:
                if r_tam == tam and r_nombre == nombre:
                    tiempos_by_metodo[nombre].append(r_tiempo)

    # Obtener fecha y hora actual
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Crear grafica
    fig = plt.figure(figsize=(10, 6))
    fig.canvas.manager.set_window_title(f"Carlos Antonio Gordillo Tenemaza - {ahora}")  # Esto solo funciona en algunos entornos

    for nombre, lista_tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, lista_tiempos, label=nombre, marker='o')

    plt.title("Comparativa métodos\nCarlos Gordillo - " + ahora)
    plt.xlabel("Tamaños arreglo")
    plt.ylabel("Tiempos obtenidos (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Guardar imagen
    plt.savefig("grafica_comparativa.png")
    plt.show()
    
#-> benchmarking es un archivo
# Diccionario guarda valores
# Tuplas() no se pueden modificar
