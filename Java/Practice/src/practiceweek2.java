
public class practiceweek2 {

	public static void main(String[] args) {
//		loop();
		practiceit();
	}
	
//	private static void loop() {
//		for (int i =1 ; i <= 2 ; i++) {
//			for (int j = 1; j <= 3; j++) {
//				for (int k = 1; k <= 4; k++) {
//					System.out.print("*");
//				}
//				System.out.print("!");
//			}
//			System.out.println();
//		}
//	}
	
	private static void practiceit() {
		for (int line = 1; line <= 5; line++) {
//		    for (int j = 1; j <= (-1 * line + 5); j++) {
//		        System.out.print(" ");
//		    }
		    for (int k = 1; k <= line; k++) {
		        System.out.print(line);
		}
		    System.out.println();
		}
	}
}
