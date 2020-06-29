
public class VC2 {

	public static void main(String[] args) {
		
		Vehicle v = new Vehicle(1999,"Handa","Civic","Blue");
		
		System.out.println(v);
		
		v.repaint("White");
		
		System.out.println(v);
		
		Car dc1 = new Car(2018, "Audi", "TT", "Sliver", "uberBlack");
		
		System.out.println(dc1);
		
		Vehicle dc2 = new Car(2018, "Audi", "TT", "Sliver", "uberBlack");
		
		System.out.println(dc2);
		
		dc2.printColor();
		v.printColor();
		
//		Car dc3 = new Vehicle(2018, "Audi", "TT", "Sliver");
	}

}
