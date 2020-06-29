public class Circle {
	private String color;
	private double radius;
	
	public Circle(String c, double r) {
		super();
		color = c;
		radius = r;
	}
	
	public Circle(double r) {
		radius = r;
	}
	
	public double getRadius() {
		return radius;
	}
	
	public double getArea() {
		return Math.PI * Math.pow(radius, 2);
	}
	
	public String toString(double area) {
		return ( color + "\tcircle of radius" + radius + "\thas an area" + area + "\tsq. units" );
	}
	
	public static void main(String[] args) {
		Circle c = new Circle("Orange", 5);
		c.getRadius();
		c.getArea();
		System.out.println(c.toString());
	}
}
