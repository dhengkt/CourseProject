import java.util.*;

public class MakeUp {

	public static void main(String[] args) {

		// Problem 1 dataStructureAdvice()
		System.out.println("What is the question? " + "Static list of fixed ints, access by random index");
		String advice = dataStructureAdvice();
		System.out.println("Suggestion: " + advice);
		System.out.println();

		System.out.println("What is the question? "
				+ "Unknown number of Social Security numbers, look up specific random numbers");
		String ad = dataStructureAdvice();
		System.out.println("Suggestion: " + ad);
		System.out.println();

		System.out.println(
				"What is the question? " + "Scores by inning for a single baseball team recorded during a game");
		String su = dataStructureAdvice();
		System.out.println("Suggestion: " + su);
		System.out.println();

		// I'm not sure how could I present problem 2 here.

		// Problem 3 matchPets
		Map<String, String> inven = new HashMap<String, String>();
		Set<String> requ = new HashSet<String>();
		inven.put("Retriever", "Bob");
		inven.put("Collie", "Fred");
		inven.put("Calico", "Ginger");
		requ.add("Collie");
		requ.add("Retriever");

		Map<String, String> newInven = matchPets(inven, requ);
		System.out.println("This is the result from the quiz.");
		System.out.println(newInven);

		System.out.println();

		// More complicated one.
		Map<String, String> dogList = new HashMap<String, String>();
		Set<String> dogNeedsBath = new HashSet<String>();
		Set<String> dogGonnaPickUp = new HashSet<String>();
		// dogList: {"Alaskan Malamute"="Austin", "Shiba Inu"="Memo", "French Bulldog"="Bean"}
		dogList.put("Alaskan Malamute", "Austin");
		dogList.put("Shiba Inu","Memo");
		dogList.put("Poodle","Miru");
		dogList.put("French Bulldog","Bean");
		dogList.put("Pug","Knife");
		dogList.put("Corgi","Zoey");
		dogList.put("Dachshund","Kiki");
		// dogNeedsBath: {"Poodle", "Pug", "Corgi"}
		dogNeedsBath.add("Poodle");
		dogNeedsBath.add("Pug");
		dogNeedsBath.add("Corgi");
		// dogGonnaPickUp: {Pug","Dachshund", "Shina Inu"}
		dogGonnaPickUp.add("Pug");
		dogGonnaPickUp.add("Dachshund");
		dogGonnaPickUp.add("Shiba Inu");
		// bath should return {"Poodle"="Miru", "Pug"="Knife", "Corgi"="Zoey"} Not sure about order.
		Map<String, String> bath = matchPets(dogList, dogNeedsBath);
		// pick should return {"Pug"="Knife", "Dachshund"="Kiki", "Shiba Inu"="Memo"} Not sure about order.
		Map<String, String> pick = matchPets(dogList, dogGonnaPickUp);
		System.out.println("This is the result from problem created by me.");
		System.out.println(bath);
		System.out.println(pick);

	}

	// Getting the user's options to choose the best data structure.
	public static String dataStructureAdvice() {
		String answer = "";

		// Check number of data first. Map or others.
		System.out.println("One or two pieces of data? 1/2");
		Scanner cs = new Scanner(System.in);
		int piece = cs.nextInt();
		if (piece == 1) {
			// Check if the data has duplicate.
			System.out.println("Duplicates? Y/N");
			// Create a separate method to get users' answer.
			String an = getUsersSelection(cs);
			if (an.equalsIgnoreCase("Y")) {
				// Check if users know the number of data.
				System.out.println("Static size? Y/N");
				an = getUsersSelection(cs);
				if (an.equalsIgnoreCase("Y")) {
					answer = "Array";
				} else if (an.equalsIgnoreCase("N")) {
					// Check if users need to add/delete data in the middle or beginning.
					System.out.println("Adding/deleting data in the beginning/middle? Y/N");
					an = getUsersSelection(cs);
					if (an.equalsIgnoreCase("Y")) {
						answer = "LinkedList";
					} else if (an.equalsIgnoreCase("N")) {
						answer = "ArrayList";
					}
				}
			} else if (an.equalsIgnoreCase("N")) {
				// Check if the data needs to be sorted.
				System.out.println("Sorted data? Y/N");
				an = getUsersSelection(cs);
				if (an.equalsIgnoreCase("Y")) {
					answer = "TreeSet";
				} else {
					answer = "HashSet";
				}
			}
		} else if (piece == 2) {
			// Check if the data needs to be sorted.
			System.out.println("Sorted data? Y/N");
			String s = getUsersSelection(cs);
			if (s.equalsIgnoreCase("Y")) {
				answer = "TreeMap";
			} else {
				answer = "HashMap";
			}
		}

		return answer;
	}

	// Get user imput mulitple times, so create a method to get the input.
	private static String getUsersSelection(Scanner console) {
		String answer = console.next();
		return answer;
	}

	// Problem 3
	public static Map<String, String> matchPets(Map<String, String> inventory, Set<String> requests) {
		Map<String, String> newInven = new TreeMap<>();
		// Run through each requests breed.
		for (String Breed : requests) {
			// Check if inventory contains it.
			if (inventory.containsKey(Breed)) {
				// Add it to the new Map newInven, and remove from the original.
				newInven.put(Breed, inventory.get(Breed));
				inventory.remove(Breed);
			}
		}
		return newInven;
	}
}

// Problem 2
abstract class Animal {
	private String name;
	private int population;

	// Contructor
	public Animal(String name, int population) {
		this.name = name;
		this.population = population;
	}

	// Getter for population
	public int getPopulation() {
		return this.population;
	}
	
	// Getter for name
	public String getName() {
		return this.name;
	}

	// Setter for population
	public void setPopulation(int population) {
		this.population = population;
	}
	
	// Setter for name
	public void setName(String name) {
		this.name = name;
	}

	// abstract method for other subclasses
	abstract void eat(Animal a);

	// abstract method for other subclasses
	abstract void reproduce();

}

class Salmon extends Animal {

	public Salmon(int population) {
		super("Orca", population);
	}

	// Reproduce Salmon's population
	@Override
	public void reproduce() {
		this.setPopulation((int) (this.getPopulation() * 0.3 + this.getPopulation()));
	}

	// Eat other animal.
	@Override
	public void eat(Animal a) {
	}

}

class Shark extends Animal {

	public Shark(int population) {
		super("Shark", population);
	}

	@Override
	public void eat(Animal a) {
		// Only eat other animal when it's Salmon
		if (a instanceof Salmon) {
			a.setPopulation(a.getPopulation() - this.getPopulation());
		}
	}

	@Override
	public void reproduce() {
		// Increasing its population by 10%
		this.setPopulation((int) (this.getPopulation() * 0.1 + this.getPopulation()));
	}
}

class Orca extends Animal {

	public Orca(int population) {
		super("Orca", population);
	}

	@Override
	public void eat(Animal a) {
		// Only eat animal if it's Shark and Orca's population is at least three
		if (a instanceof Shark && this.getPopulation() >= 3) {
			a.setPopulation(a.getPopulation() - 1);
			// If animal is Salmon, eat them by Orca's population times 5
		} else if (a instanceof Salmon) {
			a.setPopulation((a.getPopulation() - this.getPopulation() * 5));
		}
	}

	// Reproduce Orca's population by decreasing 1
	@Override
	public void reproduce() {
		this.setPopulation(this.getPopulation() - 1);
	}

	class Ecosystem {
		public void main(String[] arg) {
			ArrayList<Animal> eco = new ArrayList<Animal>();

			// Add Shark, Salmon, and Orca into ecosystem.
			eco.add(new Shark(5));
			eco.add(new Salmon(100));
			eco.add(new Orca(10));

			// Run the test for ten years.
			for (int years = 0; years <= 10; years++) {
				System.out.println("year " + years);

				Iterator<Animal> it = eco.iterator();
				while (it.hasNext()) {
					Animal a = it.next();
					if (a.getPopulation() <= 0) {
						it.remove();
					}

					// Eat each animal in the ecosystem.
					for (Animal food : eco) {
						a.eat(food);
					}

					// Reproduce.
					a.reproduce();
				}
				System.out.println();
			}
		}
	}
}