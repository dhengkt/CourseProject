
class Animal_Test {

	public static void main(String[] args) {

		// Create animals
		Animal Sinba = new Lion();
		Sinba.talk();
		// Test for toString.
		System.out.println(Sinba);

		// To increase the Lion's hunger.
		for (int i = 0; i < 3; i++) {
			Sinba.timePasses();
		}
		System.out.println("Sinba's hunger:" + Sinba.getHunger() + ".");
		Sinba.feed();
		System.out.println("Sinba's hunger:" + Sinba.getHunger() + ".");

		// Have a space between different animal's tests.
		System.out.println();
		Animal Martin = new Zebra();
		Martin.timePasses();
		Martin.talk();
		System.out.println(Martin);
		System.out.println("Martin's hunger:" + Martin.getHunger() + ".");
		Martin.feed();
		System.out.println("Martin's hunger:" + Martin.getHunger() + ".");

		// Have a space between different animal's tests.
		System.out.println();
		Animal Melman = new Giraffe();
		Melman.timePasses();
		Melman.talk();
		System.out.println(Melman);
		System.out.println("Melman's hunger:" + Melman.getHunger() + ".");
		Melman.feed();
		System.out.println("Melman's hunger:" + Melman.getHunger() + ".");

		// Have a space between different test.
		System.out.println();
		Animal[] K = new Animal[3];
		Zoo KT = new Zoo(K);

		// Test when the zoo is empty.
		KT.allTalk();
		System.out.println();
		KT.print();

		// Test when the zoo only has one animal.
		System.out.println();
		KT.addToCage(Melman);
		Melman.timePasses();
		Melman.timePasses();
		System.out.println("Melman's hunger unit is: " + Melman.getHunger() + ".");
		System.out.println();
		System.out.println("Let's feed him.");
		KT.feedAll();
		System.out.println("Melman's hunger unit is: " + Melman.getHunger() + ".");
		System.out.println();
		KT.allTalk();
		System.out.println();
		KT.print();

		// Test when the zoo has two animals.
		System.out.println();
		KT.addToCage(Sinba);
		Melman.timePasses();
		Melman.timePasses();
		Sinba.timePasses();
		Sinba.timePasses();
		Sinba.timePasses();
		System.out.println("Melman's hunger unit is: " + Melman.getHunger() + ".");
		System.out.println("Sinba's hunger unit is: " + Sinba.getHunger() + ".");
		System.out.println();
		System.out.println("Let's feed them all.");
		KT.feedAll();
		System.out.println("Melman's hunger unit is: " + Melman.getHunger() + ".");
		System.out.println("Sinba's hunger unit is: " + Sinba.getHunger() + ".");
		System.out.println();
		KT.allTalk();
		System.out.println();
		KT.print();

		// Test when the zoo has three animals.
		System.out.println();
		KT.addToCage(Martin);
		Melman.timePasses();
		Melman.timePasses();
		Sinba.timePasses();
		Sinba.timePasses();
		Martin.timePasses();
		Martin.timePasses();
		System.out.println("Melman's hunger unit is: " + Melman.getHunger() + ".");
		System.out.println("Sinba's hunger unit is: " + Sinba.getHunger() + ".");
		System.out.println("Martin's hunger unit is: " + Martin.getHunger() + ".");
		System.out.println();
		System.out.println("Let's feed them all.");
		KT.feedAll();
		System.out.println("Melman's hunger unit is now " + Melman.getHunger() + ".");
		System.out.println("Sinba's hunger unit is now " + Sinba.getHunger() + ".");
		System.out.println("Martin's hunger unit is now " + Martin.getHunger() + ".");
		System.out.println();
		KT.allTalk();
		System.out.println();
		KT.print();

	}
}

public abstract class Animal {
	private int hunger;

	public Animal() {
		this.hunger = 0;
	}

	public int getHunger() {
		return this.hunger;
	}

	public void timePasses() {
		this.hunger = hunger + 1;
	}

	public void feed() {
		this.hunger = 0;
	}

	abstract public void talk();

}

class Lion extends Animal {

	public Lion() {
		super();
	}

	@Override
	public void timePasses() {

		super.timePasses();

		// If the hunger is at least 3, print the sentence.
		if (getHunger() >= 3) {
			System.out.println("The Lion paces hungrily.");
		}

	}

	@Override
	public void talk() {
		System.out.println("Roar!");
	}

	public String toString() {
		return "Lion";
	}

}

class Zebra extends Animal {

	public Zebra() {
		super();
	}

	@Override
	public void talk() {
		System.out.println("The Zebra quietly chews.");
	}

	public String toString() {
		return "Zebra";
	}

}

class Giraffe extends Animal {// Another class by myself.

	public Giraffe() {
		super();
	}

	@Override
	public void talk() {
		System.out.println("The Giraffe walks slowly.");
	}

	public String toString() {
		return "Giraffe";
	}

}

class Zoo {
	private Animal[] cage;

	public Zoo(Animal[] array) {
		this.cage = array;
	}

	public String toString() {

		String a = "";
		if (cage[0] != null) {
			a = cage[0].toString();
			for (int i = 1; i < cage.length; i++) {
				if (cage[i] != null) {
					a += "\n" + cage[i];
				}
			}
		}
		return a;
	}

	public void print() {
		System.out.println("The zoo contains the following:");
		if (this.toString() != "") {
			System.out.println(this);
		}
	}

	public void addToCage(Animal animal) {
		for (int i = 0; i < cage.length; i++) {
			if (cage[i] == null) {
				cage[i] = animal;
				break;
			}
		}
	}

	public void feedAll() {
		for (int i = 0; i < cage.length; i++) {
			if (cage[i] != null) {
				cage[i].feed();
			}
		}
	}

	public void allTalk() {
		for (int i = 0; i < cage.length; i++) {
			if (cage[i] != null) {
				cage[i].talk();
			}
		}
	}

}
