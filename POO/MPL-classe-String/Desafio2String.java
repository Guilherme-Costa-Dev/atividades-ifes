import java.util.Scanner;

public class Desafio2String{
    public static void main(String[] args){
        Scanner teclado = new Scanner(System.in);
        System.out.println("Digite um texto: ");
        String texto = teclado.nextLine();
        teclado.close();
        String word = "";

        for (int i = 0; i < texto.length(); i++){
            if (String.valueOf(texto.charAt(i)).equals(" ")) {
                if (word.length() >= 4) {
                    System.out.println(word);
                }
                word = "";
            } else {
                word += texto.charAt(i);
            } 
        }
        if (word.length() >= 4) {
            System.out.println(word);
        }
    }
}