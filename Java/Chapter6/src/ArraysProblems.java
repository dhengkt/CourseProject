import java.util.List;

public class ArraysProblems {

	public static void main(String[] args) {
		int [][] jaggedArray = new int[4][];
		jaggedArray [0] = new int[7];
		jaggedArray [1] = new int[4];
		jaggedArray [2] = new int[6];
		jaggedArray [3] = new int[11];
		loadJaggedData(jaggedArray);
		
		
//		int [] [] twodimarray = new int [10][5];
//		loadData(twodimarray);
		System.out.println();
		
		
//		String str = "Seulrene is real";
//		int [] counts = countVowels(str);
//		System.out.print("{");
//		for (int i = 0; i <counts.length; i++) {
//			System.out.print(counts[i] + ", ");
//		}
//		System.out.print("}");
	}

	private static void loadJaggedData(int[][] jaggedArray) {
		for (int row = 0; row < jaggedArray.length; row++){
			for(int col = 0; col < jaggedArray[row].length; col++){
				jaggedArray [row][col] = (int)(Math.random()*6)+1;
			}
		}
		
	}

	private static void loadData(int[][] twodimarray){
		for (int row = 0; row < twodimarray.length; row++){
			for(int col = 0; col < twodimarray[0].length; col++){
				twodimarray [row][col] = (int)(Math.random()*6)+1;
			}
		}
	}

	private static int[] countVowels(String str) {
		int [] counts = new int [5];
		for (int i = 0; i < str.length(); i++){
			char ch = str.charAt(i);
			if (ch == 'a' || ch == 'A'){
				// Counts of a's is ar location zero
				counts[0] = counts[0] + 1;
			}
			else if (ch == 'e' || ch == 'E'){
				counts[1] = counts[1] + 1;
			}
			else if (ch == 'i' || ch == 'I'){
				counts[2] = counts[2] + 1;
			}
			else if (ch == 'o' || ch == 'O'){
				counts[3] = counts[3] + 1;
			}
			else if (ch == 'u' || ch == 'U'){
				counts[4] = counts[4] + 1;
			}
			else{

			}
		}
		return counts;
	}

}
