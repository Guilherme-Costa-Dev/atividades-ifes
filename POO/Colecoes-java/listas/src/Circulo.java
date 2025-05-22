import java.lang.Math;
public class Circulo {

	Ponto centro;
	double raio;
	
	public Circulo(Ponto centro, Double raio) {
		this.centro = centro;
		this.raio = raio;
	}

	double diametro(){
		return 2 * raio;
	}

	double area(){
		return raio * raio * Math.PI;
	}
	
	double perimetro(){
		return 2 * raio * Math.PI;
	}
}


