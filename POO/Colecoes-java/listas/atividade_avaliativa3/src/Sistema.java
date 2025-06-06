import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Scanner;

public class Sistema{
    public static void main(String[] args) {

        ArrayList<CartaoCredito> listaCartao = new ArrayList<>();

        Scanner scanner = new Scanner(System.in);

        while (true) {

            System.out.println("Digite o numero do cartao: ");
            System.out.print("-> ");
            String numero = scanner.nextLine();

            if (numero.equals("XXX")) {
                break;
            }

            System.out.println("Digite o titular do cartao: ");
            System.out.print("-> ");
            String titular = scanner.nextLine();

            System.out.println("Digite o banco do cartao: ");
            System.out.print("-> ");
            String banco = scanner.nextLine();

            int cod_seg;
            while (true) {
                System.out.println("Digite o cod_seg do cartao: ");
                System.out.print("-> ");
                cod_seg = scanner.nextInt();
                scanner.nextLine();

                if (cod_seg < 100 || cod_seg > 999) {
                    System.out.println("--O codigo de seguranca deve ser um numero entre 100 e 999, digite outro valor--");
                } else {
                    break;
                }
            }

            System.out.print("Digite a data de emissao (formato yyyy-MM-dd): ");
            System.out.print("-> ");
            String strEmissao = scanner.nextLine();
            LocalDate emissao = LocalDate.parse(strEmissao);

            System.out.print("Digite a data de validade (formato yyyy-MM-dd): ");
            System.out.print("-> ");
            String strValidade = scanner.nextLine();
            LocalDate validade = LocalDate.parse(strValidade);

            CartaoCredito cartao = new CartaoCredito(numero, titular, banco, cod_seg, emissao, validade);
            listaCartao.add(cartao);
        }

        System.out.println("");
        System.out.println("==============================");

        System.out.println("Digite o valor da data que deseja conferir (formato yyyy-MM-dd):");
        System.out.print("-> ");
        String strData = scanner.nextLine();
        LocalDate data = LocalDate.parse(strData);

        scanner.close();

        System.out.println("==============================");

        System.out.println("");

        for (CartaoCredito cartao : listaCartao) {
            System.out.println("==============================");
            System.out.println(cartao);
            if (cartao.isValid(cartao.emissao, cartao.validade, data)) {
                System.out.println("O CARTAO E VALIDO");
            } else {
                System.out.println("O CARTAO E INVALIDO");
            }
            System.out.println("==============================");
            System.out.println("");
        }
    }
}