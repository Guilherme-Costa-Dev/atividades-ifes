import java.util.Scanner;

public class Tarefa4String {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite a largura: ");
        int num = scanner.nextInt();
        genLosango(num);
        scanner.close();
    }

    public static void genLosango(int num) {
        String abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String los = "";
        num--;

        for (int i = 0; i <= num / 2; i++) {
            for (int j = num; j > i; j--) {
                los += " ";
            }
            if (i == 0) {
                for (int j = 0; j <= i; j++) {
                    los += abc.charAt(j);
                }
            } else {
                for (int j = 0; j <= i * 2; j++) {
                    los += abc.charAt(j);
                }
            }
            los = los.substring(num / 2);
            System.out.println(los);
            los = "";
        }

        for (int i = 1; i <= num / 2; i++) {
            for (int j = 0; j < num / 2; j++) {
                los += " ";
            }
            for (int j = 0; j < i; j++) {
                los += " ";
            }
            if (i == num) {
                for (int j = num; j <= i; j--) {
                    los += abc.charAt(j);
                }
            } else {
                for (int j = num; j >= i * 2; j--) {
                    los += abc.charAt(j);
                }
            }
            los = los.substring(num / 2);
            System.out.println(los);
            los = "";
        }
    }
}