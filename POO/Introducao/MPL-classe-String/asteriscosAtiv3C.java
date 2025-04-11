public class asteriscosAtiv3C {
    public static void main(String[] args) {
        String ast = "";
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j <= i; j++) {
                ast += " ";
            }
            for (int j = 10; j > i; j--) {
                ast += "*";
            }
            System.out.println(ast);
            ast = "";
        }
    }
}
