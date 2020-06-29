
public class test {
	private String color;
	private double radius;
	
	public test(String c, double r) {
		super();
		color = c;
		radius = r;
	}
	
	public double getArea() {
		return Math.PI * Math.pow(radius, 2);
		
	}
	
	public double getRadius() {
		return radius;
		
	}
	
	public String toString() {
		return ( color + "\tcircle of radius" + radius + "\thas an area" + getArea() + "\tsq. units");
	}
	
	public static void main(String[] args) {
		Circle c = new Circle("Orange", 5);
		c.toString();
	}
	
}
