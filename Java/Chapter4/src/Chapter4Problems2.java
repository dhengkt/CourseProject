import java.util.*;

public class Chapter4Problems2 {

	public static void main(String[] args) {
		// Scanner console = new Scanner (System.in);
		// char ch = console.next().charAt(0);
		// System.out.println(ch);
		// console.close();
		//
		// int i = 4736;
		// double d = 434.43434;
		// String s = "These are some great values";
		// char c = 'K';
		// String outputStr = String.format("%S:%n%5d, %n$%.2f, %n%c %%", s, i, d, c);
		// System.out.println(outputStr);
		//
		// System.out.printf("The total is: $%,f%n", d);

		// System.out.printf("%S %d, $%.2f, and %c", s, i, d, c);
		Scanner console = new Scanner(System.in);
		System.out.println("Please enter the number of interger: ");

		int numoftime = console.nextInt();
		int minvalue = Integer.MAX_VALUE, maxvalue = Integer.MIN_VALUE;

		for (int times = 1; times <= numoftime; times++) {
			System.out.print("Enter value " + times + ": ");
			int value = console.nextInt();
			if (value < minvalue) {
				minvalue = value;
			}
			if (value > maxvalue) {
				maxvalue = value;
			}
		}
		System.out.println("Min value entered: " + minvalue + "\tmax value entered: " + maxvalue);
		console.close();
	}

}
