import java.util.ArrayList;

class Ex1 {
    public static void main(String[] args) {
        ArrayList<String> lista = new ArrayList<>();
        
        lista.add("chevrolet");
        for (int i = 0 ; i<10 ; i++){
            lista.add("teste");
        }

        System.out.println(lista);
    }
}