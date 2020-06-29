import java.util.Scanner;

public class InClassExercise6 {

	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		System.out.print("Enter the age: ");
		int age = console.nextInt();
		String fare = "";
		if (age <= 11) {
			fare = "$1";
		}
		else if (age >= 65) {
			fare = "$2";
		}
		else {
			fare = "$3";
		}
		System.out.println("The bus fare is " + fare + ".");
		console.close();
	}

}
