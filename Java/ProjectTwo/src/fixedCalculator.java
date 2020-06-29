import java.util.Scanner; //import that Scanner so that method can use it.

// This program is meant to perform simple mathematical calculations
// However, it has several bugs... (11, more or less)
// Your job is to debug the program so that it works as intended

public class fixedCalculator {

	public static void main(String[] args) {
		boolean done = false;
		Scanner console = new Scanner (System.in);
		while (!done){
			displayMenu();
			//Deleted the comment sign in order to display the menu.
			String selection = getUsersSelection(console);
			done = processSelection(selection, console);
		}
		System.out.println("Thank you for using this program");
	}

	private static boolean processSelection(String selection, Scanner console) {
		boolean done = false;
		if (!selection.equalsIgnoreCase("Q")){
			//Changed the 'E' to 'Q' so that users can leave the program
			if (selection.equalsIgnoreCase("U")){
				calculateResults(console);
				// Deleted the result because caluclateResults() doesn't return things
				// after the method finish.
			}
			else if (selection.equalsIgnoreCase("H")){
				//nothing to do here...let the code loop around one more time
			}
			else{
				System.out.println("Incorrect entry...try again!");
			}
		}
		else {
			done = true;
		}
		return done;
	}

	//NOTE: the method header below is fine -- it contains NO BUG!
	private static void calculateResults(Scanner console) {
		// I think there was a typing mistake here.
		// It was 'caluculateResults', so I changed it to 'calculateResults'.
		displayCalculatorInstructions();
		double operand1 = console.nextDouble();
		char operator = console.next().charAt(0);
		double operand2 = console.nextDouble();
		double result = 0.0; // Changed the int to double because it returns double value.
		boolean isOperatorValid = true;
		if (operator == '+'){
			result = operand1 + operand2;
		}
		else if (operator == '-'){
			result = operand1 - operand2;
			// Added a semicolon, and changed '+' to '-'.
		}
		else if (operator == '*'){
			result = operand1 * operand2;
		}
		else if (operator == '/'){
			if (operand2 != 0.0){
				result = operand1 / operand2;
				// Changed the '\' to '/'.
			}
			else {
				result = Double.NaN;
			}
		}
		else if (operator == '^'){
			result = Math.pow(operand1, operand2);
		}
		else {
			isOperatorValid = false;
		}
		if (isOperatorValid){
			System.out.printf("%.2f %.2c %f = %f\n", operand1, operator, operand2, result);
			// Changed the println statement to printf. And I set them round to two decimal places, 
			// but not the result.
		}
	}

	private static void displayCalculatorInstructions() {
		System.out.println("Enter a mathematical expression to evaluate");
		System.out.println("Valid operations are: +, -, /, *, ^ for power");
		System.out.println("Expression are entered with spaces between the values and operator");
		System.out.println("Here is the valid format:");
		System.out.println("\t<value><space><operator><space><value>");
		System.out.print("Your expression: ");
	}
	

	private static String getUsersSelection(Scanner console) {
		String selection = console.next();
		return selection;
	}

	private static void displayMenu() {
		System.out.println("Enter one these options:");
		System.out.println("\tH for Help");
		System.out.println("\tU for using calculator");
		System.out.println("\tQ for exiting this program");
		System.out.print("Your selection: ");
	}

}