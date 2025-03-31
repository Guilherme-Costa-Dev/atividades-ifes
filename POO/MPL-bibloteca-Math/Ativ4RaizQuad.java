import java.lang.Math;
public class Ativ4RaizQuad {
    public static void main(String[] args) {
        //declaracao das variaveis
        int num1 = 37;
        int num2 = 38;
        float result1 = 0;
        float sum = 0;

        //loop pra calcular todos as partes e ir somando o valor delas
        for (int i = 1 ; i<37 ; i++) {
            result1 = ((num1*num2)/i);
            num1--;
            num2--;
            sum += result1;
        }

        //calcular a raiz quadrada
        double result = Math.sqrt(sum);
        //print do resultado
        System.out.println(String.format("%.2f", result));
    }
}
