import java.util.ArrayList;
import java.util.Scanner;
public class Sistema {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Circulo> lista = new ArrayList<>();

        double raio;
        System.out.println("Digite o valor do raio: ");
        raio = scanner.nextDouble();

        while (raio > 0) {
            System.out.println("Digite o valor de x: ");
            Double x = scanner.nextDouble();
            System.out.println("Digite o valor de y: ");
            Double y = scanner.nextDouble();
            Ponto ponto = new Ponto(x, y);
            Circulo circulo = new Circulo(raio);
            lista.add(circulo);

            System.out.println("Digite o valor do raio: ");
            raio = scanner.nextDouble();
        }

        scanner.close();

        int index = 1;
        for (Circulo circulo : lista) {
            System.out.printf("Circulo %d: Area %.2f, Perimetro %.2f\n", index, circulo.area(), circulo.perimetro());
            index++;
        }
    }
}
