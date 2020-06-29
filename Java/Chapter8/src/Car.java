import java.awt.Color;

public class Car {
	//data members
	private Color color;
	private int fuel;
	private String type;
	private String brand;

	public Car (String b, String t, Color c, int i){
		setBrand(b);
		setType(t);
		setColor(c);
		setInk(i);
	}

	public void setType(String t){
		type = t;
	}

	public void setBrand(String b){
		brand = b;
	}
	
	public void setColor(Color c){
		color = c;
	}

	public void setColor(int r, int g, int b){
		if (r >= 0 && r <= 255 && g >= 0 && g <= 255 && b >= 0 && b <= 255){
			color = new Color (r, g, b);
		}
		else{
			color = Color.BLACK;
		}
	}

	public void setInk(int amount){
		if (amount >= 0 && amount <= 100){
			fuel = amount;
		}
		else{
			fuel = 100;
		}
	}
	public void showInfo() {
		System.out.println("Brand: " + brand + "Type: " + type + "Color: " + color + "fuel: " + fuel + "%");
	}
}
