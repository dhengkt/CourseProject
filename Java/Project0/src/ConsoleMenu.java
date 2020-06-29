//CSC 143
//HsinYu Chi(Katie)
//Project0 CSC 142 Review

//Hello Professor Hu,
//I have question. My program won't remember the order if I finish ordering from coffee and jump to tea.
//Is ther a way to combine to arrays? Or I should add each item in the array one by one?
//And, my getPrices method doesn't work. I don't know where should I put them.
//My code is working before getting to the price part.

import java.util.Scanner;

public class ConsoleMenu {

	// Create the menu for coffee and tea.
	//private static String[] teaMenu = { "Green Tea", "Black Tea", "Ice Tea" };
	private static String[] coffeeMenu = { "Mocha", "Latte", "Espresso" };

	public static void main(String[] args) {

		// This boolean is for checking if the user finished thier ordering.
		boolean done = false;
		Scanner console = new Scanner(System.in);

		// While done is false program will continue running.
		while (!done) {
			displaymainMenu();// method for display the mainmenu.
			String selection = getUsersSelection(console);// Get the user selection from console.
			done = processSelection(selection, console);
		}
		System.out.println("Thank you for using this program");// Display the sentence when user finish.

	}

	private static void displayCoffeeMenu() {

		System.out.println();

		// Using loop to display all items from coffee menu.
		for (int i = 0; i < coffeeMenu.length; i++) {
			char fl = coffeeMenu[i].charAt(0);// Get the first letter from each item.
			System.out.printf("\"%s\" for %s.", fl, coffeeMenu[i]);// Display the menu like "M" for Mocha.
			System.out.println();
		}
		System.out.println("\"X\" for previous menu.");
		System.out.print("Your selection:");
	}

	private static void displaymainMenu() {

		// Display the main menu.
		System.out.println("Select one the following:");
		System.out.println("\"C\" for Coffee.");
		System.out.println("\"T\" for Tea.");
		System.out.println("\"H\" for Help.");
		System.out.println("\"Q\" to Quit.");
		System.out.print("Your selection:");

	}

	private static String getUsersSelection(Scanner console) {
		// Program will get user imput mulitple times, so create a method to get the
		// imput.
		String selection = console.next();
		return selection;
	}

	private static boolean processSelection(String selection, Scanner console) {
		//String[] UsersOrders = {};
		String[] CoffeeOrders = {};
		//String[] TeaOrders = {};
		//double total = 0;
		//double ctotal = 0;
		//double ttotal = 0;

		boolean done = false;

		if (!selection.equalsIgnoreCase("Q")) {
			if (selection.equalsIgnoreCase("C")) {// if user choose c, process to get coffee items.
				CoffeeOrders = getCoffeeOrders(console);
			} else if (selection.equalsIgnoreCase("T")) {// if user choose t, process to get tea items.
				//TeaOrders = getTeaOrders(console);
			} else if (selection.equalsIgnoreCase("H")) {
				// print the helping guide to user.
			} else {
				System.out.println("Incorrect entry...try again!");
				System.out.println();
			}

			// UsersOrders = getFullOrders(CoffeeOrders,TeaOrders);

			// ctotal = getCoffeePrice(CoffeeOrders);
			// ttotal = getTeaPrice(TeaOrders);

			// Print out the order user have now.
			System.out.println("The orders you have right now: ");
			for (int i = 0; i < CoffeeOrders.length; i++) {
				System.out.print(CoffeeOrders[i] + " ");
			}
			System.out.println();
			System.out.println();
		} else {
			done = true;
		}
		return done;
	}

//	private static double getCoffeePrice(String[] coffeeOrders) {
//		char[] firstletter = {};
//		double prices = 0;
//		double total = 0;
//
//		for (int i = 0; i <= coffeeOrders.length; i++) {
//			firstletter[i] = coffeeOrders[i].charAt(0);
//		}
//
//		for (int x = 0; x <= firstletter.length; x++) {
//			if (firstletter[x] == 'M' || firstletter[x] == 'm') {
//				prices = 3.65;
//			} else if (firstletter[x] == 'L' || firstletter[x] == 'l') {
//				prices = 3.45;
//			} else if (firstletter[x] == 'E' || firstletter[x] == 'e') {
//				prices = 2.65;
//			}
//
//			total += prices;
//		}
//		return total;
//	}

//	private static String[] getTeaOrders(Scanner console) {
//
//		System.out.print("How many orders do you have?");
//		int ordernum = console.nextInt();
//
//		String[] UsersTeaItems = new String[ordernum];
//		int number = 0;
//
//		displayTeaMenu();
//		String selection = getUsersSelection(console);
//
//		for (int i = 0; i <= number; i++) {
//			if (!selection.equalsIgnoreCase("X")) {
//				if (selection.equalsIgnoreCase("G")) {
//					UsersTeaItems[i] = "Green Tea";
//					number++;
//					System.out.print("What is your next selection?");
//					selection = getUsersSelection(console);
//				} else if (selection.equalsIgnoreCase("B")) {
//					UsersTeaItems[i] = "Black Tea";
//					number++;
//					System.out.print("What is your next selection?");
//					selection = getUsersSelection(console);
//				} else if (selection.equalsIgnoreCase("I")) {
//					UsersTeaItems[i] = "Ice Tea";
//					number++;
//					System.out.print("What is your next selection?");
//					selection = getUsersSelection(console);
//				} else {
//					System.out.println("Incorrect entry...try again!");
//					System.out.print("What is your next selection?");
//					selection = getUsersSelection(console);
//				}
//			}
//		}
//
//		return UsersTeaItems;
//	}

//	private static void displayTeaMenu() {
//		System.out.println();
//		for (int i = 0; i < teaMenu.length; i++) {
//			char fl = teaMenu[i].charAt(0);
//			System.out.printf("\"%s\" for %s.", fl, teaMenu[i]);
//			System.out.println();
//		}
//		System.out.println("\"X\" for previous menu.");
//		System.out.print("Your selection:");
//
//	}

	private static String[] getCoffeeOrders(Scanner console) {

		System.out.print("How many orders do you have?");
		int ordernum = console.nextInt();

		String[] UsersCoffeeItems = new String[ordernum];
		int number = 0;

		displayCoffeeMenu();
		String selection = getUsersSelection(console);

		for (int i = 0; i <= number; i++) {
			if (!selection.equalsIgnoreCase("X")) {
				if (selection.equalsIgnoreCase("M")) {
					UsersCoffeeItems[i] = "Mocha";//put the order into the array.
					number++;
					System.out.print("What is your next selection?");//after user select one, ask them another one.
					selection = getUsersSelection(console);
				} else if (selection.equalsIgnoreCase("L")) {
					UsersCoffeeItems[i] = "Latte";
					number++;
					System.out.print("What is your next selection?");
					selection = getUsersSelection(console);
				} else if (selection.equalsIgnoreCase("E")) {
					UsersCoffeeItems[i] = "Espresso";
					number++;
					System.out.print("What is your next selection?");
					selection = getUsersSelection(console);
				} else {
					System.out.println("Incorrect entry...try again!");
					System.out.print("What is your next selection?");
					selection = getUsersSelection(console);
				}
			}
		}
		System.out.println();
		return UsersCoffeeItems;

	}

}
