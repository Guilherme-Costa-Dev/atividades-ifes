import java.lang.Math;

public class Ponto {
    Double x;
    Double y;
   
    public Ponto(Double x, Double y){
        this.x = x;
        this.y = y;
    }

    Double dist(Ponto p){
        return Math.sqrt(Math.pow((p.x-x),2) + Math.pow((p.y-y),2));
    }

    public String toString(){
        String s = "Coordenada x: " + x + "\nCoordenada y: " + y + "\n";
        return s;
    }
}
