
//Hello Professor Hu,
//I have question at the reverseOrder method.
//In the video you set the if(!mapIntToString.containsKey(mapStringToInt.values(s))) {
//				mapIntToString.put(mapStringToInt.get(s), s);
//			}
//But it'll has error with the mapStringToInt.values(s)
//I commented the part that has error in the method.
//I think it's because in mapStringToInt the key and value are different,
//so it's not the right type?
//Also, I got really different number of the words.
//I'm not sure if I did anything wrong in the readFile method.

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Test {

	public static void main(String[] args) throws FileNotFoundException {

		// Create two Maps for two text files calling the method readFile(filename)
		Map<String, Integer> bronte = readFile("Jane Eyre Ch1.txt");
		Map<String, Integer> austen = readFile("Pride Prejudice Ch1.txt");

		System.out.println(bronte);
		Map<Integer, String> reverseBronte = reverseOrder(bronte);
		System.out.println(reverseBronte);

		// Remove the words in Map Austen but not in Bronte.
		// In this part, I use the idea that Professor Hu showed in the video,
		// using Set to remove the intersect keys in Map bronte.
		// bronte's key set: {and, back, you, there, me}
		// austen's key set: {you, me, i, there, no}
		// result should be like: {and, back}
		// Create two Sets to store the key(string) in both bronte and austen.
		// Set<String> bronteSet = new HashSet<String>(bronte.keySet());
		// Set<String> austenSet = new HashSet<String>(austen.keySet());
		// //removeAll(object) will remove all the object that is in the specific set.
		// //In this case, it will remove all the austenSet's object that are also in
		// bronteSet.
		// //For example, austenSet contains {you, me, i, there, no} and
		// //bronteSet contains {and, back, you, there, me}, so
		// bronteSet.removeAll(austenSet) will
		// //remove {you, me, there} from bronteSet.
		// bronteSet.removeAll(austenSet);

	}

	// This metohd read the file from main, and create a Map<String, Integer> with
	// the words and its count.
	// output should be like {and=3, back=2, you=8, there=1, me=5}
	// Also print out the information about this file.
	public static Map<String, Integer> readFile(String filename) throws FileNotFoundException {

		Map<String, Integer> countWord = new HashMap<String, Integer>();

		Scanner input = new Scanner(new File(filename));

		// This is for counting the total word in the file.
		int wordCounts = 0;

		while (input.hasNext()) {

			String word = input.next().toLowerCase().replaceAll("[^a-z|^0-9]", "");

			if (countWord.containsKey(word)) {
				countWord.put(word, countWord.get(word) + 1);
				wordCounts++;
			} else {
				countWord.put(word, 1);
				wordCounts++;
			}

		}

		System.out.println("read " + wordCounts + " in file " + filename + ", and contains " + countWord.size()
				+ " unique words ");

		return countWord;

	}

	// This method reverse the Map<String, Integer> to Map<Integer, String>
	// input : {and=3, back=2, you=8, there=1, me=5}
	// output : { 8=you , 5=me, 3=and, 2=back, 1=there}
	public static Map<Integer, String> reverseOrder(Map<String, Integer> input) {

		Set<String> stringSet = new HashSet<String>(input.keySet());
		Map<Integer, String> output = new TreeMap<Integer, String>(Collections.reverseOrder());

		// for(String s: stringSet) {
		// if(!mapIntToString.containsKey(mapStringToInt.values(s))) {
		// mapIntToString.put(mapStringToInt.get(s), s);
		// }
		//
		// }

		return output;
	}

	// This method prints out the top10 words in the Map that pass through.
	public static void printTop10(Map<Integer, String> input) {

		int total = 0;
		Set<Integer> freq = new TreeSet<Integer>(Collections.reverseOrder());

		Iterator<Integer> iterator = freq.iterator();

		while (iterator.hasNext() && total < 10) {

		}

	}
}
