import java.util.*;

public class triangles {

	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		triangleValidate(console);
		
	}

	public static void triangleValidate(Scanner console) {
		
		// Get the input from user.
		System.out.print("Enter the sides of trangle: ");
		
		int a = console.nextInt();
		int b = console.nextInt();
		int c = console.nextInt();
		
		// Set the string for output.
		String msg = "Not a triangle.";
		boolean goodTriangle = false;

		// Test the triangle sides.
		if (a < (b + c)) {
			if (b < (c + a)) {
				if (c < (b + a)) {
					msg = "It's a triangle\n";
					goodTriangle = true;
				} 
			} 
		} 
		System.out.println(msg);
		if (goodTriangle) {
			triangleType(a, b, c);
		}
	}
	
	public static void triangleType(int a, int b, int c) {
		
	}

}
