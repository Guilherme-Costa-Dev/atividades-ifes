import java.util.Scanner;
public class Tarefa4String {
    public static void main(String[] args) {
        genLosango(11);
    }

    public static void genLosango(int num){
        String abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String los = "";

        for (int i = 0 ; i<=num/2 ; i++) {
            for (int j = 10 ; j>i ; j--) {
                los += " ";
            }
            if (i == 0) {
                for (int j = 0; j <= i; j++) {
                    los += abc.charAt(j);
                }
            }
            else{
                for (int j = 0 ; j <= i*2 ; j++) {
                    los += abc.charAt(j);
                }
            }
            los = los.substring(5);
            System.out.println(los);
            los = "";
        }

        for (int i = 1 ; i<=num/2 ; i++) {
            for (int j = 0 ; j<5 ; j++) {
                los += " ";
            }
            for (int j = 0 ; j<i ; j++) {
                los += " ";
            }
            if (i == num) {
                for (int j = 10; j <= i; j--) {
                    los += abc.charAt(j);
                }
            }
            else{
                for (int j = 10 ; j >= i*2 ; j--) {
                    los += abc.charAt(j);
                }
            }
            los = los.substring(5);
            System.out.println(los);
            los = "";
        }
    }
}
