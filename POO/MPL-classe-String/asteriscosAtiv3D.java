public class asteriscosAtiv3D {
    public static void main(String[] args) {
        String ast = "";
        for (int i = 10 ; i>0 ; i--) {
            for (int j = 0 ; j<i ; j++){
                ast+=" ";
            }
            for (int j = 10 ; j>=i ; j--) {
                ast+="*";
            }
            System.out.println(ast);
            ast="";
        }
    }
}
