
public class Inclass {

	public static void main(String[] args) {
		practice();
//		System.out.println("\"hello 42 \"" + 2 + 4);

	}
	
	private static void practice() {
		for (int line = 1; line <= 5; line++) {
		    for (int k = 1; k <= line; k++) {
		        System.out.print('*');
		}
		    System.out.println();
		}
		for (int l = 1; l <=5; l++) {
			for (int j = 5; j >= l; j--) {
				System.out.print('*');
			}
			System.out.println();
		}
	}

}
