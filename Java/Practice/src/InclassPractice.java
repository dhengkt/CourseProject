
public class InclassPractice {

	public static void main(String[] args) {
		double result = 0.0;
		for (int k = 0; k <= 1000000; k++) {
			result = result + (Math.pow(-1.0, k))/(2.0*k+1.0);
		}
		System.out.println(result*4);
		System.out.println(Math.PI);
	}
	
}
