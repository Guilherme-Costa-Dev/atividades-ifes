import java.util.ArrayList;

class Ex7 {
    public static void main(String[] args) {
        ArrayList<String> lista = new ArrayList<>();

        lista.add("chevrolet");
        for (int i = 0; i < 10; i++) {
            lista.add("teste");
        }

        for (String coisas : lista) {
            System.out.println(coisas);
        }
    }
}