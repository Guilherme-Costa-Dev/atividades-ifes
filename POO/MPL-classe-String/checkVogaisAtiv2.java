import java.util.Scanner;

public class checkVogaisAtiv2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite uma palavra: ");
        String palavra = scanner.nextLine();
        scanner.close();

        System.out.println("Tem "+countVogais(palavra)+" vogais");
    }

    public static int countVogais(String palavra) {
        int num = 0;

        for (int i = 0 ; i<palavra.length() ; i++) {
            if (String.valueOf(palavra.charAt(i)).equals("a")) {
                num++;
            }
            else{
                if (String.valueOf(palavra.charAt(i)).equals("e")) {
                    num++;
                }
                else{
                    if (String.valueOf(palavra.charAt(i)).equals("i")) {
                        num++;
                    }
                    else{
                        if (String.valueOf(palavra.charAt(i)).equals("o")) {
                            num++;
                        }
                        else{
                            if (String.valueOf(palavra.charAt(i)).equals("u")) {
                                num++;
                            }
                        }
                    }
                }
            }
        }
        return num;
    }
}
