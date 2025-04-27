import java.util.Scanner;
public class Sistema {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Qual o valor de x: ");
        double x = scanner.nextDouble();
        System.out.println("Qual o valor de y: ");
        double y = scanner.nextDouble();

        while (x != 9999){

            Ponto ponto = new Ponto(x,y);
            System.out.println("Qual o valor de x: ");
            x = scanner.nextFloat();
            System.out.println("Qual o valor de y: ");
            y = scanner.nextFloat();
        }

        scanner.close();
    }
}
