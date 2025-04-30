
    #self es la instancia de la clase
    #obligatorio en cada metodo
    # metodos_ordenamiento.py

class MetodosOrdenamiento:
    def sortByBubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)

        for i in range(n):
            for j in range(i + 1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
                    #solo funciona en python
        return arreglo

                    
                    