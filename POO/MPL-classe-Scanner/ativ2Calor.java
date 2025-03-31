import java.util.Scanner;
public class ativ2Calor {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite a massa do corpo: ");
        double massa = scanner.nextDouble();
        System.out.print("Digite o calor específico da substância: ");
        double calorEspecifico = scanner.nextDouble();
        System.out.print("Digite a variação de temperatura: ");
        double deltaT = scanner.nextDouble();
        
        double quantidadeDeCalor = calcCalor(deltaT, massa, calorEspecifico, deltaT);
        
        System.out.println("A quantidade de calor e: "+quantidadeDeCalor);
        
        scanner.close();
    }

    public static double calcCalor(double quantidadeDeCalor, double massa, double calorEspecifico, double deltaT) {
        return quantidadeDeCalor = massa * calorEspecifico * deltaT;
    }
}
