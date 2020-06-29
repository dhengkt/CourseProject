import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class InClassExerciseW8 {

	public static void main(String[] args) throws FileNotFoundException {
		File infile = new File("SID");
		Scanner inputfile = new Scanner (infile);
		while (inputfile.hasNextInt()) {
			int sid = inputfile.nextInt();
			System.out.println("Your student ID number is " + sid + ".");
		}
		inputfile.close();

	}

}
