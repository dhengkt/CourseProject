
public class SpaceNeedle {

	public static final int SIZE = 8;

	public static void main(String[] Args) {
		
		// Draw the needle of space needle
		printNeedle();

		// Draw top half of space needle head
		printDomeOrBase();

		// Draw middle of space needle head
		printCollar();

		// Draw lower half of space needle head
		printBowl();

		// Draw neck of space needle
		printNeedle();

		// Draw middle of space needle
		printMidPart();

		// Draw bottom of space needle
		printDomeOrBase();
		printCollar();

	}

	// Draw space needle spire. The loops here control the space and
	// the number of "||" that in a line.
	// The number of lines is equal to the size.
	public static void printNeedle() {

		for (int i = 1; i <= SIZE; i++) {

			for (int j = 1; j <= (3 * SIZE); j++) {
				System.out.print(" ");
			}

			System.out.print("||");

			for (int j = 1; j <= (3 * SIZE); j++) {
				System.out.print(" ");
			}

			System.out.println();

		}

	}

	// Draw top half of space needle head
	// I separate the head to "__/", ":", "||", and "\__".
	// The things change in each line is ":", so I use a loop to control ":".
	public static void printDomeOrBase() {

		for (int line = 1; line <= SIZE; line++) {

			for (int i = 1; i <= ((3 * SIZE) - (3 * line)); i++) {
				System.out.print(" ");
			}

			System.out.print("__/");

			for (int i = 1; i <= ((3 * line) - (3)); i++) {
				System.out.print(":");
			}

			System.out.print("||");

			for (int i = 1; i <= ((3 * line) - (3)); i++) {
				System.out.print(":");
			}

			System.out.print("\\__");

			System.out.println();
		}

	}

	// Draw middle of space needle head
	// The loops in here control the number of lines and number of '"' in each line.
	public static void printCollar() {

		System.out.print("|");

		for (int i = 1; i <= 6 * SIZE; i++) {
			System.out.print("\"");

		}

		System.out.print("|");

		System.out.println();

	}

	// Draw lower half of space needle head
	// This shape changes "/\" in different size, so the loop is for number of "/\" and
	// the number of line.
	public static void printBowl() {

		for (int line = 1; line <= SIZE; line++) {

			for (int i = 1; i <= (2 * line) - 2; i++) {
				System.out.print(" ");
			}

			System.out.print("\\_");

			for (int j = 1; j <= (((3 * SIZE) + 1) - (2 * line)); j++) {
				System.out.print("/\\");
			}

			System.out.print("_/");

			System.out.println();

		}

	}

	// Draw middle of space needle, which looks like "|%%||%%|". 
	// Because the shape only change "%" here, I separate "|%%||%%|" to "|", "%", and "||".
	// So it's easier for me to control the number of "%" in different size.
	public static void printMidPart() {

		for (int line = 1; line <= (SIZE * 4); line++) {

			for (int j = 1; j <= (SIZE + (SIZE + 1)); j++) {
				System.out.print(" ");
			}

			System.out.print("|");

			for (int x = 1; x <= (SIZE - 2); x++) {
				System.out.print("%");
			}

			System.out.print("||");

			for (int x = 1; x <= (SIZE - 2); x++) {
				System.out.print("%");
			}

			System.out.print("|");

			System.out.println();

		}

	}

}