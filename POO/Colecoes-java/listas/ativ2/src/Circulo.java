import java.lang.Math;
public class Circulo {

	double raio;
	
	public Circulo(Double raio) {
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


