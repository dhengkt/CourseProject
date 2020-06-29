import java.awt.Color;
import java.awt.Graphics;

public class Chapter3GGraphicsProblems {
	
	public static final int WIDTH = 800, HEIGHT = 800;
	public static void main(String[] args) {

		DrawingPanel window = new DrawingPanel(WIDTH,HEIGHT);
		window.setBackground(Color.LIGHT_GRAY);
		Graphics pen = window.getGraphics();
//		drawsomethings(pen);
		drawGraphPaper(pen, 40);
		drawCircles(window,pen,40);
	}
	
	public static void drawGraphPaper(Graphics pen, int step) {
		pen.setColor(Color.BLUE);
		for (int x1 = 40; x1 < WIDTH; x1 = x1 + step) {
			pen.drawLine(x1, 0, x1, HEIGHT);
		}
		
		for (int y1 = 40; y1 < HEIGHT; y1 = y1 + step) {
			pen.drawLine(0, y1, WIDTH, y1);
		}
	}
	
	public static void drawCircles(DrawingPanel windows, Graphics pen, int i) {
		pen.setColor(Color.BLACK);
		for (int y = 0; y < WIDTH; y = y + i) {
			for (int x = 0; x < HEIGHT; x = x + i) {
				pen.drawOval(x, y, i, i);
				windows.sleep(50);
			}
		}
	}
	
	public static void drawsomethings(Graphics pen) {
		pen.drawLine(50, 50, 600, 600);
//		pen.drawOval(600, 600, 100, 100);
		pen.setColor(Color.PINK);
//		pen.drawRect(600, 600, 100, 100);
		pen.fillRect(600, 600, 100, 100);
		pen.setColor(Color.ORANGE);
	}

}
