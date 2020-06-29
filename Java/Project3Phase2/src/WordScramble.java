import java.io.*;
import java.util.*;

public class WordScramble {

	public static void main(String[] args) throws FileNotFoundException {

		// Create the dictionary and read the file.
		Dictionary dic = new Dictionary("dictionary.txt");
		Scanner input = new Scanner(new File("input.txt"));

		while (input.hasNext()) {
			// Set the started time.
			long timeStart = System.nanoTime();
			String startWord = input.next();
			String endWord = input.next();
			// Call wordScramble() to search.
			wordScramble(dic, startWord, endWord);
			// Reset the used words.
			dic.resetUsed();
			// Set the end time.
			long timeEnd = System.nanoTime();
			double timeSpent = timeEnd - timeStart;
			// Print the time spent.
			System.out.printf("%.2fms%n", timeSpent / 1000000);
			System.out.println();
		}
	}

	// Doing the actual search.
	public static void wordScramble(Dictionary dic, String start, String end) {
		boolean isFound = false;
		// Stack []
		Stack<String> wordS = new Stack<String>();
		// Queue with Stack [[]]
		Queue<Stack<String>> wordQ = new LinkedList<Stack<String>>();
		// [dear]
		wordS.push(start);
		// [[dear]]
		wordQ.add(wordS);

		int max = wordS.size();
		String topWord = "";

		while (!wordQ.isEmpty()) {
			// [dear]
			Stack<String> tempS = wordQ.remove();
			topWord = tempS.peek();

			if (topWord.equals(end)) {
				System.out.println("Found it!");
				// [[dear, fear]] the shortest path.
				System.out.println(tempS);
				wordQ.clear();
				isFound = true;
			} else {
				Iterator<String> itr = dic.wordsAreOffByOneF(topWord).iterator();
				while (itr.hasNext()) {
					// Add the ladder to data structure.
					@SuppressWarnings("unchecked")
					Stack<String> cloneS = (Stack<String>) tempS.clone();
					cloneS.push(itr.next());
					wordQ.add(cloneS);
				}
			}
		}
		if (isFound == false) {
			System.out.println("Not found!");
		}
	}
}

class Dictionary {
	private Set<String> dicSet = new HashSet<String>();
	private Queue<String> usedWords = new LinkedList<String>();

	// Constructor
	public Dictionary(String fileName) throws FileNotFoundException {

		File f = new File(fileName);
		Scanner in = new Scanner(f);
		while (in.hasNext()) {
			String word = in.next();
			this.dicSet.add(word);
		}
	}

	// Reset the usedWords.
	public void resetUsed() {
		this.usedWords.clear();
	}

	// Test if the word is one letter off.
	public boolean testWords(String word1, String word2) {
		boolean isOneOff = false;
		int diffNumOfLetter = 0;

		if (word1.length() == word2.length()) {
			for (int i = word1.length() - 1; i >= 0; i--) {
				// Compare each character in the word1 & word2
				if (word1.charAt(i) != word2.charAt(i)) {
					diffNumOfLetter++;
				}
			}
			if (diffNumOfLetter <= 1) {
				isOneOff = true;
			} else {
				isOneOff = false;
			}
		}
		return isOneOff;
	}

	// This one read through all words in dictionary.
	public Queue<String> wordsAreOffByOne(String word) {
		Queue<String> q = new LinkedList<String>();

		for (String key : this.dicSet) {
			if (testWords(word, key) && this.dicSet.contains(key) && !this.usedWords.contains(key)) {
				q.add(key);
				this.usedWords.add(key);
			}
		}
		return q;
	}

	// This one replace the character one by one.
	public Queue<String> wordsAreOffByOneF(String word) {

		Queue<String> q = new LinkedList<String>();
		for (int i = 0; i < word.length(); i++) {
			// In Ch4.3 from book, character's integer value a = 97 and so on, so z = 122.
			for (int j = 97; j <= 122; j++) {
				// Use substring() to change each character in word.
				String motifiedWord = (word.substring(0, i)) + (char) j + word.substring(i + 1, word.length());
				if (this.dicSet.contains(motifiedWord) && !this.usedWords.contains(motifiedWord)) {
					q.add(motifiedWord);
					this.usedWords.add(motifiedWord);
				}
			}
		}

		return q;
	}

}