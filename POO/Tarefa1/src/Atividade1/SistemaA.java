package src.Atividade1;
import java.util.Scanner;

public class SistemaA {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        for (int i = 1 ; i<=10 ; i++) {
            System.out.print("Digite o valor do tempo "+i+": ");
            Double tempo = scanner.nextDouble();
            Eq2g funcao = new Eq2g(-5, 20, 1);
            double altura = funcao.a * Math.pow(tempo, 2) + funcao.b * tempo + funcao.c;
            System.out.println(tempo+"s, " + altura + "m");
        }
        scanner.close();
    }
}
