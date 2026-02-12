import java.util.ArrayList;
import java.util.Scanner;

public class Sistema {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        ArrayList<Automovel> lista = new ArrayList<>();

        System.out.println("Digite a placa do carro: ");
        System.out.print("->");
        String placa = scanner.nextLine();

        while (!placa.equals("ZZZZZZZZ")) {
            
            System.out.println("Digite a quantidade de passageiros: ");
            System.out.print("->");
            int passageiros = scanner.nextInt();
            scanner.nextLine();
           
            System.out.println("Digite o modelo do carro: ");
            System.out.print("->");
            String modelo = scanner.nextLine();

            System.out.println("Digite o peso do carro: ");
            System.out.print("->");
            Double peso = scanner.nextDouble();

            System.out.println("Digite a quantidade de gasolina (L): ");
            System.out.print("->");
            int gasolina = scanner.nextInt();
            scanner.nextLine();

            Automovel carro = new Automovel(placa, modelo, passageiros, peso, gasolina);
            lista.add(carro);

            System.out.println("");
            System.out.println("Digite a placa do carro: ");
            System.out.print("->");
            placa = scanner.nextLine();
        }

        scanner.close();

        int carro_com_maior_peso = 0;
        double maior_peso = 0;
        int tam = lista.size()-1;
        for (int i = 0 ; i<=tam ; i++) {
            System.out.println("===================");
            System.out.println("CARRO "+(i+1)+":");
            System.out.println(lista.get(0));

            double peso_total = lista.get(i).pesoTotal(lista.get(i).peso_fabrica, lista.get(i).quantidade_de_passageiros, lista.get(i).quantidade_litros_gasolina);

            if (peso_total > maior_peso) {
                maior_peso = peso_total;
                carro_com_maior_peso = i;
            }
        }

        System.out.println("===================");
        System.out.println((carro_com_maior_peso+1)+" E O CARRO COM MAIOR PESO TOTAL");
        System.out.println(lista.get(carro_com_maior_peso));
    }
}
