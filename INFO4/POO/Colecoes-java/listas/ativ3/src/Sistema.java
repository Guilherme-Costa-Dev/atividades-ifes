import java.util.ArrayList;
import java.util.Scanner;
public class Sistema {
    public static void main(String[] args) {

        ArrayList<Pessoa> lista = ColetarDados();
        Menu(lista);

    }

    public static ArrayList<Pessoa> ColetarDados() {
        ArrayList<Pessoa> lista = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o Nome (deixe vazio para buscar): ");
        System.out.print("-> ");
        String nome = scanner.nextLine();
        while (!nome.equals("")) {
            System.out.println("Digite a Idade: ");
            System.out.print("-> ");
            int idade = scanner.nextInt();
            scanner.nextLine();

            System.out.println("Digite o Celular");
            System.out.print("-> ");
            String celular = scanner.nextLine();

            System.out.println("Digite o Email");
            String email = scanner.nextLine();

            Pessoa pessoa = new Pessoa(nome, idade, celular, email);
            lista.add(pessoa);

            System.out.println("Digite o Nome (deixe vazio para buscar): ");
            System.out.print("-> ");
            nome = scanner.nextLine();
        }
        
        return lista;
    }

    public static void BuscaNome(ArrayList<Pessoa> lista, String nome){
        for (Pessoa pessoa : lista) {
            if (pessoa.nome.equals(nome)){
                System.out.println(pessoa);
            }
        }
    }

    public static void BuscaCelular(ArrayList<Pessoa> lista, String celular) {
        for (Pessoa pessoa : lista) {
            if (pessoa.celular.equals(celular)) {
                System.out.println(pessoa);
            }
        }
    }

    public static void BuscaEmail(ArrayList<Pessoa> lista, String email) {
        for (Pessoa pessoa : lista) {
            if (pessoa.email.equals(email)) {
                System.out.println(pessoa);
            }
        }
    }

    public static void BuscaIdade(ArrayList<Pessoa> lista, int idade) {
        for (Pessoa pessoa : lista) {
            if (pessoa.idade == idade) {
                System.out.println(pessoa);
            }
        }
    }

    public static void Menu(ArrayList<Pessoa> lista) {
        Scanner scanner = new Scanner(System.in);

        int sair;
        do {
            System.out.println("======================================");
            System.out.println("Escolha um dos metodos para buscar:");
            System.out.println("(1) para buscar por Nome");
            System.out.println("(2) para buscar por Idade");
            System.out.println("(3) para buscar por Email");
            System.out.println("(4) para buscar por Telefone");
            System.out.println("======================================");
            System.out.print("-> ");
            int num = scanner.nextInt();

            if (num == 1) {
                System.out.println("Digite o Nome: ");
                System.out.print("-> ");
                String nome = scanner.next();
                System.out.println("");

                BuscaNome(lista, nome);
            } else {
                if (num == 2) {
                    System.out.println("Digite a idade: ");
                    System.out.print("-> ");
                    int idade = scanner.nextInt();
                    System.out.println("");
                    BuscaIdade(lista, idade);
                } else {
                    if (num == 3) {
                        System.out.println("Digite o Email: ");
                        System.out.print("-> ");
                        String email = scanner.next();
                        System.out.println("");
                        BuscaEmail(lista, email);
                    } else {
                        if (num == 4) {
                            System.out.println("Digite o Telefone: ");
                            System.out.print("-> ");
                            String telefone = scanner.next();
                            System.out.println("");
                            BuscaCelular(lista, telefone);
                        }
                    }
                }
            }
            
            System.out.println("====================================");
            System.out.println("Digite (1) para coninuar buscando");
            System.out.println("Digite (0) para sair");
            System.out.println("====================================");
            System.out.print("->");
            sair = scanner.nextInt();

        } while (sair != 0);
        scanner.close();
    }
}
