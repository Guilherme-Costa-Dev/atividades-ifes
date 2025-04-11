import java.util.Scanner;
public class Ativ5TriangRet {
    public static void main(String[] args) {
        //le os valores
        Scanner scanner = new Scanner(System.in);

        System.out.println("Primeiro lado: ");
        float lado1 = scanner.nextFloat();
        System.out.println("Segundo lado: ");
        float lado2 = scanner.nextFloat();
        System.out.println("Terceiro lado: ");
        float lado3 = scanner.nextFloat();

        scanner.close();

        String triang = checkTriang(lado1, lado2, lado3);
        System.out.println(triang);
    }

    public static String checkTriang(float lado1, float lado2, float lado3) {
        //checa se o triangulo é valido e retorna "O triangulo é válido" caso nao entre no proximo if
        if (lado1+lado2 > lado3 && lado2+lado3 > lado1 && lado3+lado1>lado2) {
            //checa se o triangulo é retangulo e retorna "O triangulo é retangulo"
            if (lado1 == lado2 || lado2 == lado3 || lado3 == lado1) {
                return "O triangulo é retangulo";
            }
            return "O triangulo é válido";
        }
        //retorna "O triangulo não é válido" caso nao tenha atendido as condiçoes
        return "O triangulo não é válido";
    }
}
