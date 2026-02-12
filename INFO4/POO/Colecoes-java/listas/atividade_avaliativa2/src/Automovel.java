public class Automovel {
    String placa;
    String modelo;
    int quantidade_de_passageiros;
    double peso_fabrica;
    int quantidade_litros_gasolina;

    public Automovel (String placa, String modelo, int quantidade_de_passageiros, double peso_fabrica, int quantidade_litros_gasolina) {
        this.modelo = modelo;
        this.placa = placa;
        this.peso_fabrica = peso_fabrica;
        this.quantidade_de_passageiros = quantidade_de_passageiros;
        this.quantidade_litros_gasolina = quantidade_litros_gasolina;
    }

    public double pesoTotal(double peso_fabrica, int quantidade_de_passageiros, int quantidade_litros_gasolina){
        return peso_fabrica+(quantidade_de_passageiros*75)+(quantidade_litros_gasolina*0.75);
    }

    public String toString(){
        return "Placa: "+placa+"\n"+
                "Modelo: "+modelo+"\n"+
                "Quantidade de passageiros: "+quantidade_de_passageiros+"\n"+
                "Quantidade de litros de gasolina: "+quantidade_litros_gasolina+"\n"+
                "Peso de fabrica: "+peso_fabrica+"\n"+
                "Peso total: "+pesoTotal(peso_fabrica, quantidade_de_passageiros, quantidade_litros_gasolina);
    }
}
