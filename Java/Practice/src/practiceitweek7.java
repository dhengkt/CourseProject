import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class practiceitweek7 {
    public static void main(String[] args) throws FileNotFoundException{
        File infile = new File("example.txt");
        Scanner input = new Scanner(infile);
        countWords(input);
    }

    // Counts total lines and words in the input scanner.
    public static void countWords(Scanner input) {
        int lineCount = 0;
        int wordCount = 0;
        while(input.hasNextLine()){
            lineCount++;
            String line = input.nextLine();
            Scanner lineinput = new Scanner (line);
            while(lineinput.hasNext()){
                wordCount++;
            }
            lineinput.close();
        }
        input.close();
        System.out.println("Lines: " + lineCount);
        System.out.println("Words: " + wordCount);
    }
}