import java.io.*;
import java.util.*;

/**
 * @author Andrew
 *
 */
public class BronteA {

    /**
     * @param args
     * @throws FileNotFoundException
     */
    public static void main(String[] args) throws FileNotFoundException {
        String file1 = "Jane Eyre Ch1.txt";
        String file2 = "Pride Prejudice Ch1.txt";        
        
        Map<String, Integer> file1Map = getCountMap(file1);
        System.out.println(sortTopCount(file1Map));
        Map<String, Integer> file2Map = getCountMap(file2);
        System.out.println(sortTopCount(file2Map));
        
        Map<String, Integer> differenceMap = compareMaps(file1Map, file2Map);
        System.out.println("the Top 10+ words appearing in Jane Eyre Ch 1 but not Pride and Prejudice Ch 1 are:");
        System.out.println(sortTopCount(differenceMap));
        
        

    }
    

    /**
     * @param map1
     * @param map2
     * @return
     */
    public static Map<String, Integer> compareMaps(Map<String, Integer> map1, Map<String, Integer> map2) {
        //System.out.println(map1);
        //System.out.println(map2);
        
        Map<String, Integer> differenceMap = new HashMap<String, Integer>();
        for(String key : map1.keySet()) {
            if(!map2.containsKey(key)) {
                differenceMap.put(key, map1.get(key));
            }
        }

        return differenceMap;
        
    }
    /**
     * @param map
     * @return
     */
    public static Map<Integer, Set<String>> sortTopCount(Map<String, Integer> map){
        Map<Integer, Set<String>> topCounts = new TreeMap<Integer, Set<String>>(Collections.reverseOrder());
        
        for(String key : map.keySet()) {
            if(!topCounts.containsKey(map.get(key))) {
                topCounts.put(map.get(key), new HashSet<String>());
                topCounts.get(map.get(key)).add(key);
            
            }else {
                topCounts.get(map.get(key)).add(key);
            }        
        }
        
        int order = 0;
        int nthKey = 0;
        
        for(Integer key : topCounts.keySet()) {
            Iterator<String> itr = topCounts.get(key).iterator();
            while(itr.hasNext()) {
                String temp = itr.next();
                order++;
            }
            if(order >= 10) {
                nthKey=key;
                break;          
            }  
        }
        
        for(int i = nthKey-1; i>0; i--) {
            topCounts.remove(i);
        }
        
        return topCounts;    
    }
    
    
    
    /**
     * @param fileName
     * @return
     * @throws FileNotFoundException
     */
    public static Map<String, Integer> getCountMap(String fileName) throws FileNotFoundException {
        Scanner in = new Scanner(new File(fileName));
        Map<String, Integer> wordCountMap = new HashMap<String, Integer>();
        int numOfWords = 0;
        int numOfUnique = 0;
        
        while(in.hasNext()) {
            String word = in.next();
            word = word.replaceAll("[^A-Z|^a-z|^0-9]", "");
            if(!Character.isUpperCase(word.charAt(0))) {
                numOfWords++;
                if(!wordCountMap.containsKey(word)) {
                    wordCountMap.put(word, 1);
                    numOfUnique++;
                }else {
                    int count = wordCountMap.get(word);
                    wordCountMap.put(word, count+1);
                }
            }
        }
        
        System.out.println(numOfWords);
        System.out.println(numOfUnique);
               
        return wordCountMap;
    }
}
