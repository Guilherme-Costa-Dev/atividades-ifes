import java.util.Scanner;

public class megasena {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

            for (int i = 0 ; i<2709 ; i++) {
                String linha = scanner.nextLine();
                String[] lista = linha.split("\t");

                System.out.println(lista[0] + " " + lista[1] + " " +
                                    lista[2] + " " + lista[3] + " " +
                                    lista[4] + " " + lista[5]
                );
            }

        scanner.close();
    }
}
