/* 
 * 
 */
class Publication_Test {
	public static void main(String[] args) {

		// Test the Book class.
		Publication b1 = new Book("Disney-Hyperion", 448, 11.99, "The Trials of Apollo Book Three The Burning Maze",
				"Rick Riordan");
		System.out.println("B1's original info: \n" + b1.toString() + ".");
		System.out.println();
		// Test the setters.
		System.out.println("Change the publisher, number of page, price, title, and author for the book.");
		b1.setPublisher("Broadway Books");
		b1.setNumOfPage(500);
		b1.setPrice(12.00);
		b1.setTitle("The KT");
		// Had to use typecasting because the type is publication.
		((Book) b1).setAuthor("Peter Parker");
		// Test the getters.
		System.out.println("The publisher has changed to " + b1.getPublisher() + ".");
		System.out.println("The page has changed to " + b1.getNumOfPage() + ".");
		System.out.printf("The price has changed to $" + String.format("%.2f", b1.getPrice()) + ".\n");
		System.out.println("The title has changed to " + b1.getTitle() + ".");
		System.out.println("The author has changed to " + ((Book) b1).getAuthor() + ".");
		System.out.println("B1's NEW info: \n" + b1.toString());

		// Print a space line to start the new test.
		System.out.println();

		// Test the Magazine class.
		Publication m1 = new Magazine("Meredith Corporation", 45, 12.50, "TIME", "monthly");
		System.out.println("M1's original info: \n" + m1.toString() + ".");
		System.out.println();
		System.out.println("Change the publisher, number of page, price, title, and unit for the magazine.");
		m1.setPublisher("Disney-Hyperion");
		m1.setNumOfPage(50);
		m1.setPrice(15.00);
		m1.setTitle("People");
		((Magazine) m1).setUnit("weekly");
		System.out.println("The publisher has changed to " + m1.getPublisher() + ".");
		System.out.println("The page has changed to " + m1.getNumOfPage() + ".");
		System.out.printf("The price has changed to $" + String.format("%.2f", m1.getPrice()) + ".\n");
		System.out.println("The title has changed to " + m1.getTitle() + ".");
		System.out.println("The author has changed to " + ((Magazine) m1).getUnit() + ".");
		System.out.println("M1's NEW info: \n" + m1.toString() + ".");

		// Print a space line to start the new test.
		System.out.println();

		// Test the KidsMagazine class.
		Publication km1 = new KidsMagazine("National Geographic Partners LLC", 25, 5.60,
				"National Geographic Little Kids", "monthly", 3, 6);
		System.out.println("Km1's original info: \n" + km1.toString() + ".");
		System.out.println();
		System.out.println(
				"Change the publisher, number of page, price, title, unit, and age range for the kid magazine.");
		km1.setPublisher("Disney-Hyperion");
		km1.setNumOfPage(34);
		km1.setPrice(15.00);
		km1.setTitle("People's Kids");
		((KidsMagazine) km1).setUnit("bi-weekly");
		((KidsMagazine) km1).setMinAge(4);
		((KidsMagazine) km1).setMaxAge(8);
		System.out.println("The publisher has changed to " + km1.getPublisher() + ".");
		System.out.println("The page changed to " + km1.getNumOfPage() + ".");
		System.out.printf("The price has changed to $" + String.format("%.2f", km1.getPrice()) + ".\n");
		System.out.println("The title has changed to " + km1.getTitle() + ".");
		System.out.println("The author has changed to " + ((KidsMagazine) km1).getUnit() + ".");
		System.out.println("KM1's NEW info: \n" + km1.toString());

		// Print a space line before start the new test.
		System.out.println();

		// Create the array of publication.
		Publication[] collection = new Publication[8];

		// Create the collection.
		collection[0] = new Book("Disney-Hyperion", 448, 11.99, "The Trials of Apollo Book Three The Burning Maze",
				"Rick Riordan");
		collection[1] = new Magazine("Meredith Corporation", 45, 12.50, "TIME", "monthly");
		collection[2] = new KidsMagazine("National Geographic Partners LLC", 25, 5.60,
				"National Geographic Little Kids", "monthly", 3, 6);
		collection[3] = new Book("Broadway Books", 400, 8.79, "Ready Player One: A Novel", "Ernest Cline ");
		collection[4] = new Book("Geek & Sundry", 356, 11.53, "The Punch Escrow", "Tal M. Klein");
		collection[5] = new Book("Matthew Mather ULC", 346, 5.99, "Darknet", "Matthew Mather");
		collection[6] = new Magazine("Hearst Magazines", 46, 2.50, "Elle", "monthly");
		collection[7] = new KidsMagazine("National Geographic Partners LLC", 25, 5.60, "National Geographic Kids",
				"monthly", 6, 12);

		// Print the whole information of each publication in the array.
		for (int i = 0; i < 8; i++) {
			System.out
			.println("The information of publication " + (i + 1) + " is: \n" + collection[i].toString() + ".");
		}

		// Add a blank line here.
		System.out.println();

		// Test the setter.
		// Create the arrays of publisher, numOfPage, price, and title.
		String[] publisher = { "Broadway Books", "Disney-Hyperion", "Marvel", "Disney-Hyperion", "Matthew Mather ULC",
				"Geek & Sundry", "National Geographic Partners LLC", "Hearst Magazines" };
		int[] numOfPage = { 400, 46, 26, 488, 366, 345, 65, 30 };
		double[] price = { 12.45, 3.45, 11.22, 9.56, 16.32, 5.87, 1.99, 2.99 };
		String[] title = { "Spider-Man", "Spider-Man: Homecoming", "Harry Potter", "Hunger Game", "Ready Player One",
				"Me Before You", "The End", "Bye" };

		//Use loop to change each collection's publisher, numOfPage, price, and title.
		for (int j = 0; j < 8; j++) {
			collection[j].setPublisher(publisher[j]);
			collection[j].setNumOfPage(numOfPage[j]);
			collection[j].setPrice(price[j]);
			collection[j].setTitle(title[j]);

		}

		// Test the setters in subclass.
		for (int i = 0; i < 8; i++) {
			// If the object is book, changes its author to Spider-Man.
			if (collection[i] instanceof Book) {
				((Book) collection[i]).setAuthor("Spider-Man");
				// If the object is magazine, changes its unit to bi-weekly.
			} else if (collection[i] instanceof Magazine) {
				((Magazine) collection[i]).setUnit("bi-weekly");
				// If the magazine is also a kids magazine, changes its min and max age to 9 and
				// 12.
				if (collection[i] instanceof KidsMagazine) {
					((KidsMagazine) collection[i]).setMinAge(9);
					((KidsMagazine) collection[i]).setMaxAge(12);
				}

			}
		}

		// Test the getters.
		for (int i = 0; i < 8; i++) {
			System.out.println("The publisher of publication " + (i + 1) + " has changed to "
					+ collection[i].getPublisher() + ".");
			System.out.println("The number of page of publication " + (i + 1) + " has changed to "
					+ collection[i].getNumOfPage() + ".");
			System.out.println("The price of publication " + (i + 1) + " has changed to $"
					+ String.format("%.2f", collection[i].getPrice()) + ".");
			System.out.println(
					"The title of publication " + (i + 1) + " has changed to " + collection[i].getTitle() + ".");
			// Test the getters in subclass.
			// Test each publication and print out the different information.
			if (collection[i] instanceof Book) {
				System.out.println("The author of publication " + (i + 1) + " has changed to "
						+ ((Book) collection[i]).getAuthor() + ".");
			} else if (collection[i] instanceof Magazine) {
				System.out.println("The unit of publication " + (i + 1) + " has changed to "
						+ ((Magazine) collection[i]).getUnit() + ".");
				if (collection[i] instanceof KidsMagazine) {
					System.out.println("The age range of publication " + (i + 1) + " has changed to "
							+ ((KidsMagazine) collection[i]).getMinAge() + " to "
							+ ((KidsMagazine) collection[i]).getMaxAge() + ".");
				}
			}
			// Add a line before the loop runs the next time.
			System.out.println();
		}

		// Print the NEW information out.
		for (int k = 0; k < 8; k++) {
			System.out
			.println("The NEW information of publication " + (k + 1) + " is: \n" + collection[k].toString() + ".");
			// Print the type of the publication out.
			if (collection[k] instanceof Book) {
				System.out.println("Publication " + (k + 1) + " is a book.");
			} else if (collection[k] instanceof KidsMagazine) {
				System.out.println("Publication " + (k + 1) + " is a kids magazine.");
			} else {
				System.out.println("Publication " + (k + 1) + " is a magazine.");
			}
			System.out.println();
		}
	}

}

public abstract class Publication {

	// Create the fields.
	private String publisher;
	private int numOfPage;
	private double price;
	private String title;

	public Publication(String publisher, int numOfPage, double price, String title) {
		this.publisher = publisher;
		this.numOfPage = numOfPage;
		this.price = price;
		this.title = title;
	}

	public String getPublisher() {
		return this.publisher;
	}

	public void setPublisher(String publisher) {
		this.publisher = publisher;
	}

	public int getNumOfPage() {
		return this.numOfPage;
	}

	public void setNumOfPage(int numOfPage) {
		this.numOfPage = numOfPage;
	}

	public double getPrice() {
		return this.price;
	}

	public void setPrice(double price) {
		this.price = price;
	}

	public String getTitle() {
		return this.title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	@Override
	// For the price part, I use String.format to make sure it show two decimal
	// places.
	public String toString() {
		return "Publisher: " + this.publisher + ", page: " + this.numOfPage + "," + " price: $"
				+ String.format("%,.2f", this.price) + ", title: " + this.title;
	}

}

class Magazine extends Publication {

	// Magazine has a new field unit.
	private String unit;

	public Magazine(String publisher, int numOfPage, double price, String title, String unit) {
		super(publisher, numOfPage, price, title);
		this.unit = unit;
	}

	public String getUnit() {
		return this.unit;
	}

	public void setUnit(String unit) {
		this.unit = unit;
	}

	@Override
	// Call the toString from the superclass Publication first, and add additional
	// information.
	public String toString() {
		return super.toString() + ", unit: " + this.unit;
	}

}

class Book extends Publication {

	// Book has a new feild author.
	private String author;

	public Book(String publisher, int numOfPage, double price, String title, String author) {

		super(publisher, numOfPage, price, title);
		this.author = author;
	}

	public String getAuthor() {
		return this.author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}

	@Override
	// Call the toString from the superclass Publication first, and add additional
	// information.
	public String toString() {
		return super.toString() + ", author: " + this.author;
	}

}

class KidsMagazine extends Magazine {

	// Kids magazine has a new feild ageRange.
	private int minAge;
	private int maxAge;

	public KidsMagazine(String publisher, int numOfPage, double price, String title, String unit, int min, int max) {
		super(publisher, numOfPage, price, title, unit);
		this.minAge = min;
		this.maxAge = max;
	}

	public int getMinAge() {
		return this.minAge;
	}

	public void setMinAge(int minAge) {
		this.minAge = minAge;
	}

	public int getMaxAge() {
		return this.maxAge;
	}

	public void setMaxAge(int maxAge) {
		this.maxAge = maxAge;
	}

	@Override
	// Call the toString from the superclass Magazine first, and add additional
	// information.
	public String toString() {
		return super.toString() + String.format(", min age: %d, max age: %d", this.minAge, this.maxAge);
	}

}
