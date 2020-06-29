import java.awt.*;

public class practiceGraphics {

	public static final int WIDTH = 800, HEIGHT = 800;
	public static void main(String[] args) {
		DrawingPanel window = new DrawingPanel(WIDTH,HEIGHT);
		Graphics pen = window.getGraphics();
		drawthings(window, pen, 20);
	}
	
	public static void drawthings(DrawingPanel windows, Graphics pen, int d) {
		pen.setColor(Color.GRAY);
		pen.drawLine(0, 0, WIDTH/2, HEIGHT);
		pen.drawLine(WIDTH/2, HEIGHT, WIDTH, 0);
		int x1 = 0, x2 = WIDTH, y = 0;
		for (int line = 1; line <= HEIGHT/d; line++) {
			pen.drawLine(x1, y, x2, y);
			x1 += d/2;
			x2 -= d/2;
			y = y + d;
		}
	}
}
