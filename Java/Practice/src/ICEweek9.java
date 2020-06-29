import java.util.Scanner;

public class ICEweek9 {
	// which I didn't submit it TAT

	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		nameofMonths(console);
		numbers();

	}

	private static void numbers() {
		for (int i = 0; i < 6; i ++) {
			double [] nums = {};
			nums[i] = 1.1 + (1.1*i);
			System.out.println(nums);
		}
		
	}

	private static void nameofMonths(Scanner console) {
		System.out.print("How many months: ");
		int numofmonths = console.nextInt();
		int [] temps = new int [numofmonths];
		for (int i = 0; i < temps.length; i++){
			System.out.println("Enter the month: ");
			//String monthtemp = console.next();
		}
		
	}

}
