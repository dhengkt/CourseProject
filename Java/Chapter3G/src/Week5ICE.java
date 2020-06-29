import java.awt.*;

public class Week5ICE {

	public static void main(String[] args) {
		DrawingPanel window = new DrawingPanel (200, 200);
		Graphics pen = window.getGraphics();
		pen.setColor(Color.PINK);
		pen.fillOval(20, 20, 160, 160);
		pen.setColor(Color.GRAY);
		pen.fillRect(40, 60, 40, 40);
		pen.fillRect(120, 60, 40, 40);
		pen.drawLine(80, 80, 120, 80);
		pen.drawOval(80, 120, 40, 40);
		
	}

}
