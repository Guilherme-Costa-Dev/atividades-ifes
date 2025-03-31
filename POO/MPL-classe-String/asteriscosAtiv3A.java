public class asteriscosAtiv3A {
    public static void main(String[] args) {
        String ast = "";
        for (int i = 1 ; i<=10 ; i++) {
            for (int j = 1 ; j<=i ; j++) {
                ast += "*";
            }
            System.out.println(ast);
            ast = "";
        }
    }
}
