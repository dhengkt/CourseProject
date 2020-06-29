import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.Scanner;

public class ProcessMobyDick {

	public static void main(String[] args) throws FileNotFoundException {
		Scanner fileInput = new Scanner (new File("mobydick.txt"));
		PrintStream fileOutput = new PrintStream ("Gfilsh.txt");
		processFile(fileInput, fileOutput);

	}

	private static void processFile(Scanner fileInput, PrintStream fileOutput){
		while(fileInput.hasNextLine()){
			String line = fileInput.nextLine();
			Scanner lineInput = new Scanner (line);
			while (lineInput.hasNext()){
				String word = lineInput.next();
				if (!word.equalsIgnoreCase("whale"))
					fileOutput.print(word + " ");
				else{
					if (word.equals("WHALE"))
						fileOutput.print("GOLDFISH" + " ");
					else if (word.equals("whale"))
						fileOutput.print("goldfish" + " ");
				}
			}
			fileOutput.println();
			lineInput.close();
		}
		fileInput.close();
		fileOutput.close();
	}

}
