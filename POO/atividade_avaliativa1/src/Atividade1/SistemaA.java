import java.util.Scanner;

public class SistemaA {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        for (int i = 1 ; i<=10 ; i++) {
            //ler o tempo
            System.out.println();
            System.out.print("Digite o valor do tempo "+i+": ");
            Double tempo = scanner.nextDouble();
            
            //criar o objeto
            Eq2g funcao = new Eq2g(-5, 20, 1);

            // calcular a altura em funcao do tempo lido
            double altura = funcao.fdex(tempo);

            //exibicao do resultado
            System.out.println(tempo+"s, " + altura + "m");
        }
        scanner.close();
    }
}
