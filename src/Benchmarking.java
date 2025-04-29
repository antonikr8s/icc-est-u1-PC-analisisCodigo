import java.util.Random;

public class Benchmarking {
    // Se crea un constructor vacio

    private MetodosOrdenamiento metodosOrdenamiento;

    public Benchmarking() {

        long inicioMillis = System.currentTimeMillis();
        long inicioNano = System.nanoTime();

        // System.out.println(inicioMillis);
        // System.out.println(inicioNano);

        metodosOrdenamiento = new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatorio(1000000);//cambiar el 0 por 100000
        Runnable tarea = () -> metodosOrdenamiento.burbujaTradicional(arreglo);

        double tiempoNano = medirConNanoTime(tarea);
        double tiempoMillis = medirConCurrentTime(tarea);

        System.out.println("\n-> Tiempo con nanoTime: " + tiempoNano + " segundos");
        System.out.println("-> Tiempo con currentTimeMillis: " + tiempoMillis + " segundos");
        System.out.println("");

    }

    private int[] generarArregloAleatorio(int tamano) {
        int[] arreglo = new int[tamano];
        Random random = new Random();
        for (int i = 0; i < arreglo.length; i++) {
            arreglo[i] = random.nextInt(10000);
        }
        return arreglo;
    }

    public double medirConNanoTime(Runnable tarea) {
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0;
    }

    public double medirConCurrentTime(Runnable tarea) {
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        return (fin - inicio) / 1_000.0;
    }
}
