public class Pessoa {
    String nome;
    int idade;
    String celular;
    String email;

    public Pessoa (String nome, int idade, String celular, String email) {
        this.nome = nome;
        this.idade = idade;
        this.celular = celular;
        this.email = email;
    }

    public String toString(){
        return "Nome -> " + nome + "\n" +
                "Idade -> " + idade + "\n" +
                "Telefone -> " + celular + "\n" +
                "Email -> " + email + "\n"
        ;
    }
}
