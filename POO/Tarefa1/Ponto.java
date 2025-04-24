public class Ponto{
    double x;
    double y;

    public Ponto (double x, double y){
        this.x = x;
        this.y = y;
    }

    public double calcDist(Ponto destino){
        double dist = Math.sqrt(Math.pow(destino.x-x, 2) + Math.pow(destino.y-y, 2));
        return dist;
    }
}

