import java.awt.Color;

public class imageManipulation {

	public static void main(String[] args) {
		DrawingPanel window = new DrawingPanel("cry.png");
		applyFilter(window);
		flipHorizontally(window);
	}

	private static void flipHorizontally(DrawingPanel window){
		Color [][] pixels = window.getPixels();
		int topRow = 0, bottomRow = pixels.length - 1;
		while (topRow < bottomRow){
			for (int col = 0; col < pixels[0].length; col++){
				Color pixel = pixels[topRow][col];
				pixels[topRow][col] = pixels[bottomRow][col];
				pixels[bottomRow][col] = pixel;
			}
			window.setPixels(pixels);
			topRow++;
			bottomRow--;
		}
	}

	private static void applyFilter(DrawingPanel window) {
		Color [][] pixels = window.getPixels();
		for (int row = 0; row < pixels.length; row++){
			for (int col = 0; col < pixels[row].length; col++){
				Color pixel = pixels[row][col];
				double newR = 0.393 * pixel.getRed() + 0.769 * pixel.getGreen() + 0.189 * pixel.getBlue();
				double newG = 0.349 * pixel.getRed() + 0.686 * pixel.getGreen() + 0.168 * pixel.getBlue();
				double newB = 0.272 * pixel.getRed() + 0.534 * pixel.getGreen() + 0.131 * pixel.getBlue();
				int r = 0; int g = 0; int b = 0;
				if (newR > 255){
					r = 255;
				}else{
					r = (int)newR;
				}
				if (newG > 255){
					g = 255;
				}else{
					g = (int)newG;
				}
				if (newB > 255){
					b = 255;
				}else{
					b = (int)newB;
				}
//				double lum = (0.21 * pixel.getRed()) + (0.72 * pixel.getGreen()) + (0.07 * pixel.getBlue()); 
				Color newPixel = new Color (r, g, b);
				pixels[row][col] = newPixel;
			}
		}
		window.setPixels(pixels);
	}

}
