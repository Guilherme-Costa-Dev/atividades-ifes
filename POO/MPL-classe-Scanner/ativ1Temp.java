import java.util.Scanner;
public class ativ1Temp{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Double temp = scanner.nextDouble();
        scanner.close();
        Double far = celToFar(temp);
        Double kel = celToKel(temp);
        System.out.println(far);
        System.out.println(kel);
    }

    public static Double celToFar(Double temp){
        return (Double) ((temp*1.8)+32);
    }

    public static Double celToKel(Double temp) {
        return (temp+273.15);
    }
}