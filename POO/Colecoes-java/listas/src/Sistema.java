import java.util.ArrayList;
import java.util.Scanner;
public class Sistema {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Circulo> lista = new ArrayList<>();

        double raio = 1;
        while (raio > 0) {
            System.out.println("Digite o valor do raio: ");
            raio = scanner.nextDouble();
            System.out.println("Digite o valor de x: ");
            Double x = scanner.nextDouble();
            System.out.println("Digite o valor de y: ");
            Double y = scanner.nextDouble();
            Ponto ponto = new Ponto(x, y);
            Circulo circulo = new Circulo(ponto, raio);
            lista.add(circulo);
        }
        scanner.close();

        int index = 1;
        for (Circulo circulo : lista) {
            System.out.println("Circulo " + index + ": Area " + circulo.area() + "Perimetro " + circulo.perimetro());
            index++;
        }
    }
}
