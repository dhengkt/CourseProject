import java.awt.Color;

public class Marker {
	
	//data members
	private String type;
	private Color color;
	private int ink;

	public Marker (String t, Color c, int i){
		setType(t);
		setColor(c);
		setInk(i);
	}

	public void wrtie(String text){
		if (text.length() <= ink){
			System.out.println("Imagine this getting printed in " + color + "..." + text);
			ink -= text.length();
		}
		else{
			System.out.println("Imagine this getting printed in " + color + "..." + text.substring(0, ink));
		}
	}

	public void setType(String t){
		type = t;
	}

	public void setColor (Color co){
		color = co;
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
			ink = amount;
		}
		else{
			ink = 100;
		}
	}
	public void showInfo() {
		System.out.println("Type: " + type + "\tColor: " + color + "\tink: " + ink + "%");
	}
}
