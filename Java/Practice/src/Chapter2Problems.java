
public class Chapter2Problems {
	public static final int numofLts = 10;
	public static final int numofRts = 10;
	public static int numofStars = 100;
	public static final int numoflines = 10;

	public static void main(String[] args) {
//		printLinesOfStars();
		printPattern();
	}
	
	public static void printPattern() {
		for (int i = 1; i <= numoflines; i++) {
			//printing the '<'
			for (int ch1 = 1; ch1 <= numofLts ; ch1++) {
				System.out.print('<');
			}
			//printing the '*'
			for (int ch2 = 1; ch2 <= numofStars; ch2++) {
				System.out.print('*');
			
			}
			//printing the '>'
			for (int ch3 = 1; ch3 <= numofRts; ch3++) {
				System.out.print('>');
			}
			numofStars = numofStars - 10;
			System.out.println();
		}
	}
	
//	public static void printLinesOfStars(){
//		for (int j = 1; j <= numoflines; j++){
//			for (int star = 1; star <= numofstars; star++){
//				System.out.print('*');
//			}
//			System.out.println();
//			}
//		}
	}



//	private static void printLinesOfStars() {
//		for (int j = 1; j <= numoflines; j++) {
//			printStars();
//		}
//	}
//
//	private static void printStars() {
//		for (int star = 1; star <= numofstars; star++) {
//			System.out.print('*');
//		}
//		System.out.println();
//	}

