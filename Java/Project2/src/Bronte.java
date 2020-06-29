import java.io.File;
import java.io.FileNotFoundException;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;
import java.util.Iterator;
import java.util.LinkedHashMap;


public class Bronte {

	
	public static void main(String[] args) throws FileNotFoundException {
		
		Map<String, Integer> bronte = readFile("Jane Eyre Ch1.txt");
		Map<String, Integer> austen = readFile("Pride Prejudice Ch1.txt");
		System.out.println(bronte);
		int total = 0;
		for(int freq: bronte.values()) {
			total += freq;
		}

		System.out.println(total);
		System.out.println(bronte.size());
		Map<String,Integer> newMap = inAButNotB(bronte, austen);
		System.out.println(getTop10(bronte));
		System.out.println(getTop10(austen));
		System.out.println(getTop10(newMap));

	}

	//This metohd read the file from main, and create a Map<String, Integer> with the words and its count.
	//output should be like {and=3, back=2, you=8} 
	public static Map<String, Integer> readFile(String filename) throws FileNotFoundException{

		Map<String, Integer> countWord = new HashMap<String, Integer>();

		Scanner input = new Scanner(new File(filename));

		while(input.hasNext()) {

			String word = input.next().toLowerCase().replaceAll("[^a-z|^0-9]", "");

			if(countWord.containsKey(word)) {

				countWord.put(word, countWord.get(word)+1);
			}else {
				countWord.put(word, 1);
			}

		}

		return countWord;

	}
	
	//This method find the union word that is in Map bronte but not in Map Austen.
	//
	//
	public static Map<String, Integer> inAButNotB(Map<String, Integer> a,Map<String, Integer> b){
		Map<String, Integer> newMap = new HashMap<String,Integer>();
		for(String fA : a.keySet()) {
			if(!b.containsKey(fA)) {
				newMap.put(fA, a.get(fA));
			}
		}
		return newMap;
	} 

	public static Map<String,Integer> getTop10( Map<String, Integer> countWord) {

		Map<String,Integer> top10 = new LinkedHashMap<String, Integer>();

		Set<Integer> freq = new TreeSet<Integer>(Collections.reverseOrder());
		for(int f : countWord.values()) {
			freq.add(f);
		}
		Iterator<Integer> iterator = freq.iterator();
		int count=0;
		while(iterator.hasNext() && count < 10) {
			int frequency = iterator.next();
			for(String word : countWord.keySet()) {
				if(frequency == countWord.get(word)) {
					top10.put(word, countWord.get(word));
				}
			}
			count++;
		}
		return top10;


	}





}
