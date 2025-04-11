public class Pessoa {
    String nome;
    int idade;
    Double peso, altura;
    char genero;

    public double imc() {
        return peso/(altura*altura);
    }

    /*
    public double bt() {

    } 
     */
}
