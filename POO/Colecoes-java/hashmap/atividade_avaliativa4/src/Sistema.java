import java.util.HashMap;
import java.util.Scanner;

public class Sistema {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HashMap<String, UF> hash = new HashMap<>();

        System.out.println("");
        while (true) {
            System.out.println("Digite a UF");
            System.out.print("->");
            String estado = scanner.nextLine();

            if (estado.equals("sair")) {
                break;
            }

            System.out.println("Digite a sigla da UF");
            System.out.print("->");
            String siglaEstado = scanner.nextLine();

            System.out.println("Digite a sigla da regiao");
            System.out.print("->");
            String regiao = scanner.nextLine();

            UF uf = new UF(estado, siglaEstado, regiao);

            hash.put(siglaEstado, uf);

            System.out.println("");
        }

        while (true) {

            System.out.println("");
            System.out.println("Digite a sigla de uma UF ou de uma Regiao");
            System.out.print("->");
            String sigla = scanner.nextLine();
            System.out.println("");

            if (sigla.equals("sair")) {
                break;
            }

            if (hash.containsKey(sigla)) {
                System.out.println(hash.get(sigla));
                System.out.println("");
            } else{
                for (UF uf : hash.values()){
                    if (uf.regiao.equals(sigla)) {
                        System.out.println(uf);
                        System.out.println("");
                    }
                }
            }
        

        }

        scanner.close();
    }    
}
