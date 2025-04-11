public class asteriscosAtiv3B {
    public static void main(String[] args) {
        String ast = "";
        for (int i = 10 ; i>=0 ; i--) {
            for (int j = 0 ; j<i ; j++) {
                ast+="*";
            }
            System.out.println(ast);
            ast = "";
        }
    }
}
