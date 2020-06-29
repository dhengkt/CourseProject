import java.util.Scanner;

public class Chapter3Problems {
	public static void main(String[] args) {
		//input
		System.out.println("Enter your name: ");
		Scanner console = new Scanner(System.in);
		String name = console.nextLine();
		//process
		String reverseName = reverse(name);
		//output
		System.out.println(reverseName);
		
//		for (int index = 0; index <= (name.length()-1); index++) {
//			System.out.print(name.charAt(index));
//		}
//		System.out.println();		
//		for (int index = (name.length()-1); index >= 0; index--) {
//			reverseName = reverseName + name.charAt(index);
////			System.out.print(name.charAt(index));
//		}
//		System.out.println(reverseName);
		console.close();
	}
	
	public static String reverse(String s) {
		String r = "";
		for (int index = (s.length()-1); index >= 0; index--) {
			r = r + s.charAt(index);
		}
		return r;
	}
}
