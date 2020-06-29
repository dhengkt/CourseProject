import java.awt.*;

public class practiceitProblems {

	public static void main(String[] args) {
		DrawingPanel panel = new DrawingPanel(200, 200);
	    Graphics pen = panel.getGraphics();
	    for(int x = 1; x <= 4; x++) {
	    	pen.drawRect((x*20), (x*20), (200-40*x), (200-(40*x)));
	    }
	}

}
