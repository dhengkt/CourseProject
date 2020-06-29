import java.awt.Color;

public class WritingProgram {
	
	public static final int WIDTH = 600, HEIGHT = 600;
	
	public static void main(String[] args) {
		Marker redMarker = new Marker("Dry Erase", Color.RED, 16);
		// redMarker.setType("Dry Erase");
		// redMarker.setColor(Color.RED);
		// redMarker.setInk(96);
		redMarker.showInfo();
		redMarker.wrtie("Hello CSC 142!");
		redMarker.showInfo();
		
	}

}
