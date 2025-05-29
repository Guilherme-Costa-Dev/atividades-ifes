import java.lang.Math;

public class Eq2g {
    double a, b, c;

    //constructor
    public Eq2g(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    //calcular quantidade de raizes
    public int quantRaizes() {
        double delta = Math.pow(b, 2) -4*a*c;
        if (delta > 0) {
            return 2;
        }
        if (delta == 0) {
            return 1;
        } else {
            return 0;
        }
    }

    //calcular a raiz1
    public double raiz1() {
        return (-b + Math.sqrt(Math.pow(b, 2) -4*a*c))/(2*a);
    }
    
    //calcula a raiz2
    public double raiz2() {
        return (-b - Math.sqrt(Math.pow(b, 2) -4*a*c))/(2*a);
    }

    //calcular o valor de y em funcao de um x
    public double fdex(double x) {
        return a * Math.pow(x, 2) + b * x + c;
    }

    //calcula o valor minimo ou maximo da funcao
    public double min_max() {
        double xv = -b / (2 * a);
        return a * Math.pow(xv, 2) + b * xv + c;
    }
}
