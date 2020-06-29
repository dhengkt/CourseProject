import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FindFirstName {

	public static void main (String[] args) throws FileNotFoundException {
		Scanner fileInput = new Scanner (new File("mobydick.txt"));
		getName();
		findName(fileInput);
	}

	private static String getName(){
		Scanner firstname = new Scanner (System.in);
		String nameinput = console.next();
		return nameinput
	}

	private static void findName(Scanner fileInput){

	}
}