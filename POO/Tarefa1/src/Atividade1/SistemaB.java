package src.Atividade1;

public class SistemaB {
    public static void main(String[] args) {
        //a area e: x * (x+8) = 1680
        //distribuindo o x: x^2 + 8x = 1680
        //passando pro outro lado: x^2 + 8x - 1680 = 0

        //criacao do objeto
        Eq2g funcao = new Eq2g(1, 8, -1680);
        
        //calulo da largura (x)
        double largura = funcao.raiz1();
        if (funcao.quantRaizes() == 2) {
            double largura2 = funcao.raiz2();
            if (largura2 > largura) {
                largura = largura2;
            }
        }

        //calculo da area
        double comprimento = largura + 8;
        double area = largura * comprimento;

        //exibir as informacoes
        System.out.println();
        System.out.println("EMPRESA C");
        System.out.println("================");
        System.out.printf("Area: %.2fcm²\n", area);
        System.out.printf("Largura: %.2fcm\n", largura);
        System.out.printf("Comprimento: %.2fcm\n", comprimento);
        System.out.println();
    }    
}
