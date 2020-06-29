
public class Egg2 {

	public static void main(String[] args) {
		egg();
		line();
		egg();
		line();
		eggbottom();
		eggtop();
		line();
		eggbottom();

	}
	
	public static void egg() {
		System.out.println("  _______");
		System.out.println(" /       \\");
		System.out.println("/         \\");
		System.out.println("\\         /");
		System.out.println(" \\_______/");
	}
	
	public static void line() {
		System.out.println("-\"-'-\"-'-\"-");
	}
	
	public static void eggtop() {
		System.out.println("  _______");
		System.out.println(" /       \\");
		System.out.println("/         \\");
	}
	
	public static void eggbottom() {
		System.out.println("\\         /");
		System.out.println(" \\_______/");
	}

}
