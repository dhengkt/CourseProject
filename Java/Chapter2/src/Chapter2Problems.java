
public class Chapter2Problems {
	public static final int numofstars = 20;
			
	public static void main(String[] args) {
		
		printstars();
		//loop();
		
//		int x = 10;
//		int y = 20;
//		
//		System.out.println("x = " + x + "\t" + "y = " + y);
//		x++; // x = x + 1
//		y--; // y = y + 1
//		System.out.println("x = " + ++x + "\t" + "y = " + --y);
//		System.out.println("x = " + x + "\t" + "y = " + y);
//		
		
//		double a,b,d;
//		int salary = 82374;
//		int numofhours = 23;
//		double hourlyrate = 25.67;
//		char c = '\n';
//		char e = 'T';
//		boolean boolvalue = false;
		//double salary = 7584758.54;
//		System.out.println("You are making $" + salary + ".");
		
//		int totalscore = 323;
//		int maxscore = 350;
//		
//		System.out.println((int)4783+4837);
//		System.out.println((float)(-5454-434));
//		System.out.println("You got " + ((double)totalscore/maxscore) * 100);
//		System.out.println(10.0/3);
//		System.out.println(10 % 13);
//		System.out.println();	
		
	}
	
	private static void printstars() {
		
		for (int star =1; star <= numofstars; star++){
			System.out.print('*');
		}
		System.out.println();
	}
	
	private static void loop(){
		int max = 100;
		int sum = 0;
		for (int a = 1; a <= max; a = a +1){
			System.out.println(": Happy B'day!");
		}
		
	}

}
