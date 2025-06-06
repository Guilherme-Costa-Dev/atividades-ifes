import java.time.LocalDate;

public class CartaoCredito {
    String numero;
    String titular;
    String banco;
    int codigo;
    LocalDate emissao;
    LocalDate validade;

    public CartaoCredito(String numero, String titular, String banco, int codigo, LocalDate emissao, LocalDate validade){
        this.numero = numero;
        this.titular = titular;
        this.banco = banco;
        this.codigo = codigo;
        this.emissao = emissao;
        this.validade = validade;
    }

    public String toString() {
        return "Numero -> " + numero + "\n" +
                "Titular -> " + titular + "\n" +
                "Banco -> " + banco + "\n" +
                "Código -> " + codigo + "\n" +
                "Emissão -> " + emissao + "\n" +
                "Validade -> " + validade;
    }

    public boolean isValid(LocalDate emissao, LocalDate validade, LocalDate data){
        if ((data.isAfter(emissao) || data.isEqual(emissao)) && (data.isBefore(validade) || data.isEqual(validade))) {
            return true;
        } 
        return false;
    }
}
