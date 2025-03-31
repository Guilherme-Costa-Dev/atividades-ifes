import java.util.Scanner;
public class Tarefa4String {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite a largura do losango: ");
        int num = scanner.nextInt();
        String los = genLosango(num);
        System.out.println(los);
        scanner.close();
    }

    public static String genLosango(int num){
        String abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String los = "";

        for (int i = num ; i >= 0 ; i--) {
            for (int j = 1 ; j <=(num/2) ; j++) {
                los += "test ";
            }
            System.out.println(los);
        }
        return los;
    }
}
