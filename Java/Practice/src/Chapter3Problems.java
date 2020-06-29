
public class Chapter3Problems {

	public static void main(String[] args) {
		int height = 16;
		int width = 10;
//		drawPicture(height, width);
		System.out.println("Area is " + area(height, width));
	}
	
	public static int area (int height, int width) {
		int area = height * width;
		return area;
	}
	public static void drawPicture(int height, int width) {
		height = height + 10;
		width = width + 20;
		for (int i = 1; i <= height; i++) {
			for (int j = 1; j <= width; j++) {
				System.out.print('~');
			}
			System.out.println();
		}
	}

}
