import java.util.Scanner;

public class Chapter4Problems {

	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		System.out.println("Enter values of a, b, and c: ");
		int x = console.nextInt();
		int y = console.nextInt();
		coordinate(x,y);
		int a = console.nextInt();
		int b = console.nextInt();
		int c = console.nextInt();
		findtheroots(a, b, c);
		console.close();
	}
	
	public static void coordinate(int X, int Y) {
		String msg = "";
		if (X > 0){
			if (Y > 0) {
				msg = "It's in QI.";
			}
			else if ( Y < 0) {
				msg = "It's in QIV.";
			}
			else if (Y == 0) {
				msg = "It's on x-axis.";
			}
		}
		else if (X < 0) {
			if (Y > 0) {
				msg = "It's in QII.";
			}
			else if (Y < 0) {
				msg = "It's in QIII.";
			}
			else if (Y == 0) {
				msg = "It's on x-axis.";
			}
		}
		else if (X == 0) {
			if (Y == 0) {
				msg = "It's on central opint.";
			}
			else if (Y > 0) {
				msg = "It's on y-axis.";
			}
			else if (Y < 0) {
				msg = "It's on y-axis.";
			}
		}
		System.out.print(msg);
	}

	public static void findtheroots(int A, int B, int C) {
		int discriminant = B*B - 4*A*C;
		
		if (discriminant >= 0) {
			double root1 = (-B + Math.sqrt(discriminant))/(2*A);
			if (discriminant < 0) {
				double root2 = (-B - Math.sqrt(discriminant))/(2*A);
				System.out.println("There are two roots, they are " + root1 +
						" and " + root2);
			}
			else {
				System.out.println("There is one root, it is " + root1);
			}
		}
		else {
			System.out.println("Roots are imaginary.");
		}
	}
}
