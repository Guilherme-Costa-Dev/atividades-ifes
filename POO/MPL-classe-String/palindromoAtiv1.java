import java.util.Scanner;

public class palindromoAtiv1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite uma palavra: ");
        String palavra = scanner.next();
        scanner.close();

        if (checkPalindromo(palavra)){
            System.out.println("É palindromo");
        }
        else{
            System.out.println("Não é palindromo");
        }
    }

    public static boolean checkPalindromo(String palavra) {
        String palavraSemEspaco = palavra.replace(" ", "");
        String palavraInvertida = "";
        for (int i = palavraSemEspaco.length()-1 ; i >= 0 ; i--) {
            palavraInvertida = palavraInvertida + palavraSemEspaco.charAt(i);
        }
        if (palavraInvertida.equalsIgnoreCase(palavraSemEspaco)) {
            return true;
        }
        else {
            return false;
        }
    }
}