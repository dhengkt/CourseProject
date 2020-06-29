
public class Roof {
	private static final int HEIGHT = 15;
	public static void main(String[] args) {
		roof();
		System.out.println(3 * 4 + 2 * 3);

	}
	
	private static void roof() {
		int spaces = HEIGHT - 1;
		int middlespaces = 0;
		// line by line
		for (int line = 1; line <= HEIGHT; line++) {
			//front spaces
			for (int sp = 1; sp <= spaces; sp++) {
				System.out.print(' ');
			}
			//roof line
			System.out.print('/');
			//middle spaces
			for (int msp = 1; msp <= middlespaces; msp++) {
				System.out.print(' ');
			}
			//roof line
			System.out.print('\\');
			//end spaces
			for (int sp = 1; sp <= spaces; sp++) {
				System.out.print(' ');
			}
			--spaces;
			middlespaces = middlespaces + 2;
			System.out.println();
		}
	}

}
