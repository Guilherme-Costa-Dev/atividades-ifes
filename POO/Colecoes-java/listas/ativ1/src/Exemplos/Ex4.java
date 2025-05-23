import java.util.ArrayList;

class Ex4 {
    public static void main(String[] args) {
        ArrayList<String> lista = new ArrayList<>();

        lista.add("chevrolet");
        for (int i = 0; i < 10; i++) {
            lista.add("teste");
        }

        lista.remove(0);

        System.out.println(lista);
    }
}
