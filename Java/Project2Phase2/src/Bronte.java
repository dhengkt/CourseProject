import java.io.*;
import java.util.*;

public class Bronte {

	public static void main(String[] args) throws FileNotFoundException {

		// Read the file "Jane Eyre Ch1.txt" and print out the information.
		Map<String, Integer> bronte = readFile("Jane Eyre Ch1.txt");
		Map<Integer, Set<String>> reverseBronte = reverseOrder(bronte);
		printTop10(reverseBronte);

		System.out.println();

		// Read the file "Pride Prejudice Ch1.txt" and print out the information.
		Map<String, Integer> austen = readFile("Pride Prejudice Ch1.txt");
		Map<Integer, Set<String>> reverseAusten = reverseOrder(austen);
		printTop10(reverseAusten);

		System.out.println();

		// Remove the words in Map bronte that also in Map austen.
		Map<String, Integer> newbronte = comparedMaps(bronte, austen);
		Map<Integer, Set<String>> newBronte = reverseOrder(newbronte);
		System.out.println("The Top 10+ words appearing in Jane "
				+ "Eyre Ch 1 but not Pride and Prejudice Ch 1 are:");
		printTop10(newBronte);
		
		System.out.println();
		// Test the CompleteFiles.
		Map<String, Integer> comBro = readFile("CompleteBronte.txt");
		Map<Integer, Set<String>> reverseComBro = reverseOrder(comBro);
		printTop10(reverseComBro);
		
		System.out.println();
		Map<String, Integer> comAus = readFile("CompleteAusten.txt");
		Map<Integer, Set<String>> reverseComAus = reverseOrder(comAus);
		printTop10(reverseComAus);
		
		System.out.println();
		Map<String, Integer> newComBro = comparedMaps(comBro, comAus);
		Map<Integer, Set<String>> newcomBro = reverseOrder(newComBro);
		System.out.println("The Top 10+ words appearing in CompleteBronte "
				+ "but not in CompleteAusten are:");
		printTop10(newcomBro);
	}

	// This method read the file from main, and create a Map<String, Integer> with the words and its count.
	// output should be like {and=3, back=2, you=8, there=1, me=5}
	// Also print out the information about this file.
	public static Map<String, Integer> readFile(String filename) throws FileNotFoundException {

		Map<String, Integer> countWord = new HashMap<String, Integer>();
		Scanner input = new Scanner(new File(filename));

		// wordCounts and numOfUnique count the total number of words and unique words.
		int wordCounts = 0;
		int numOfUnique = 0;

		while (input.hasNext()) {
			// I put the wordCounts++ in the wrong place, so I moved it outside the if()
			String word = input.next();
			wordCounts++;
			// I found a bug about the string in complete file, so I added another condition word.length() > 0.
			if (!Character.isUpperCase(word.charAt(0)) && word.length() > 0) {
				word = word.toLowerCase().replaceAll("[^A-Z|^a-z|^0-9]", "");
				if (!countWord.containsKey(word)) {
					countWord.put(word, 1);
					numOfUnique++;
				} else {
					int count = countWord.get(word);
					countWord.put(word, count + 1);
				}
			}

		}

		System.out.println("In file " + filename + " has total " + wordCounts + 
				" words and " + numOfUnique + " unique words.");

		return countWord;
	}

	// This method remove the intersection words in two maps by using Set's method removeAll()
	// bronte's key set: {and, back, you, there, me}
	// austen's key set: {you, me, i, there, no}
	// result should be like: {and, back}
	public static Map<String, Integer> comparedMaps(Map<String, Integer> map1, Map<String, Integer> map2) {
		
		Map<String, Integer> differenceMap = new HashMap<String, Integer>();
		Set<String> bronteSet = new HashSet<String>(map1.keySet());
		Set<String> austenSet = new HashSet<String>(map2.keySet());
		bronteSet.removeAll(austenSet);
		// Goes through the string in bronteSet, and get the value(frequency) from the original Map, which
		// is map1. Put them into the new Map differenceMap.
		for (String key : bronteSet) {
			differenceMap.put(key, map1.get(key));
		}

		return differenceMap;
	}

	// This method reverse the Map<String, Integer> to Map<Integer, Set<String>>
	// input : {and=3, back=2, you=8, there=3, me=5}
	// output : {8=[you], 3=[and, me], 2=[back], 1=[there]}
	public static Map<Integer, Set<String>> reverseOrder(Map<String, Integer> inputMap) {
		
		Map<Integer, Set<String>> reverse = new TreeMap<Integer, Set<String>>(Collections.reverseOrder());
		// Using the Set in the Map so that I can save multiple word with the same frequency.
		for (String key : inputMap.keySet()) {
			if (!reverse.containsKey(inputMap.get(key))) {
				// reverse should be like : {3=[]}
				reverse.put(inputMap.get(key), new HashSet<String>());
				// add the words in it like :{3=[and]}
				reverse.get(inputMap.get(key)).add(key);

			} else {
				// If it already has the Set in the value, just put another word in it.
				// reverse: {3=[and, me]}
				reverse.get(inputMap.get(key)).add(key);
			}
		}

		return reverse;
	}
	// This method prints out the top10 words in the Map that pass through.
	public static void printTop10(Map<Integer, Set<String>> sortedMap) {

		// To track the ranking and save the rank 10's frequency.
		int order = 0;
		int tenth = 0;

		// Runs through the number of frequency in passed Map.
		for (Integer freq : sortedMap.keySet()) {
			// Set the stringSet for passed Map to iterator.
			Iterator<String> itr = sortedMap.get(freq).iterator();
			// While itr has the next element AND order is less than 10, run this part.
			while (itr.hasNext() && order <= 10) {
				// Set itr's element to be the string temp, or it won't run to the next step.
				String temp = itr.next();
				// Add one to the order, and set the tenth number to be the freq.
				order++;
				tenth = freq;
			}
		}
		
		// The method just find the first nine higher frequency in the passed Map,
		// I have to remove the items that are outside the top 10.
		// sortedMap : {8=[you], 3=[and, me], 2=[back], 1=[there]}
		// output : {8=[you], 3=[and, me]} //pretend we only need top 3.
		for (int i = tenth - 1; i > 0; i--) {
			sortedMap.remove(i);
		}
		// Print out the result.
		System.out.println("Top 10 words list is: " + sortedMap);
	}
}
