import java.util.ArrayList;
import java.util.Scanner;
public class Sistema {
    public static void main(String[] args) {

        ArrayList<Pessoa> lista = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        String nome = scanner.next();
        while (!nome.equals("")) {
            int idade = scanner.nextInt();
            String celular = scanner.next();
            String email = scanner.next();
            Pessoa pessoa = new Pessoa(nome, idade, celular, email);
            lista.add(pessoa);

            nome = scanner.next();
        }
        scanner.close();
    }

    public static void BuscaNome(ArrayList<Pessoa> lista, String nome){
        int tam = lista.size()-1;
        for (int i = 0; i<tam; i++) {
            if (lista.get(i).nome.equals(nome)){
                System.out.println(lista.get(i));
            }
        }
    }
}
