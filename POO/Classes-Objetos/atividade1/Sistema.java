import java.util.Scanner;

public class Sistema {
    public static void main(String[] args) {
        Pessoa pearson = new Pessoa();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Nome: ");
        pearson.nome = scanner.nextLine();

        while (pearson.name != "") {
            System.out.println("Peso: ");
            pearson.peso = scanner.nextDouble();

            System.out.println("altura: ");
            pearson.altura = scanner.nextDouble();

            System.out.println("Nome: " + pearson.nome);
            System.out.println("Peso: " + pearson.peso);
            System.out.println("altura: " + pearson.altura);
            System.out.println("IMC: " + pearson.imc);

            System.out.println("Nome: ");
            pearson.nome = scanner.nextLine();
        }
    }
}
