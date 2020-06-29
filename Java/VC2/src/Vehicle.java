
public class Vehicle {

	int year;
	String make;
	String model;
	String color;
	
	public Vehicle(int year, String make, String model, String color) {
		super();
		this.year = year;
		this.make = make;
		this.model = model;
		this.color = color;
	}
	
	public int getYear() {
		return year;
	}
	
	public void setYear(int year) {
		this.year = year;
	}
	
	public String getMake() {
		return make;
	}
	
	public void setMake(String make) {
		this.make = make;
	}
	
	public String getModel() {
		return model;
	}
	
	public void setModel(String model) {
		this.model = model;
	}
	
	public String getColor() {
		return color;
	}
	
	public void setColor(String color) {
		this.color = color;
	}
	
	/* This is the part I added for the polymorphism,
	 * but I'm not sure if this is correct.
	 */
	public void printColor() {
		System.out.printf("The color is %s.\n", getColor());
	}
	
	@Override
	public String toString() {
		return "Vehicle Katie [year=" + year + ", make=" + make + ", color=" + color + "]";
	}
	
	public void repaint(String color) {
		this.color = color;
	}

}

class Car extends Vehicle{
	
	String uberClass;

	public Car(int year, String make, String model, String color, String uberClass) {
		super(year, make, model, color);
		this.uberClass = uberClass;
	}

	@Override
	public String toString() {
		return "Car [uberClass=" + uberClass + ", year=" + year + ", make=" + make + ", model=" + model + ", color="
				+ color + "]";
	}
	
	
	
}
