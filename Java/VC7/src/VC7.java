import java.util.*;

public class VC7 {

	public static void main(String[] args) {
//		for(int i = 0; i <= 6; i++) {
//			countBinary(i);
//		}
		waysToClimb(1);
	}

	public static void printDown(int n) {
		if(n == 1) {
			System.out.print(1);
		}
		else {
			System.out.print(n + ", ");
			printDown(n-1);
		}
	}

	public static int factorial(int n) {
		if(n == 0) {
			return 1;
		}else {
			return n * factorial(n-1);
		}
	}

	public static void countBinary(int n) {
		countBinary(n, "");
	}
	
	public static void countBinary(int n, String s) {
		if(n == 0) {
			System.out.println(s);
		}
		else {
			countBinary(n-1, s + "0");
			countBinary(n-1, s + "1");
		}
	}
	
	public static void waysToClimb(int n) {
		ArrayList<Integer> steps = new ArrayList<Integer>();
		waysToClimb(n, steps);
	}
	
	public static void waysToClimb(int n, ArrayList<Integer> steps) {
		int sum = 0;
		for(int i = 0; i < steps.size(); i++) {
			sum += steps.get(i);
		}
		if(sum > n) {
		}
		if(sum == n) {
			System.out.println(steps);
		}
		else {
			steps.add(1);
			waysToClimb(n-1, steps);
			steps.remove(steps.size()-1);
			steps.add(2);
			waysToClimb(n-2, steps);
			steps.remove(steps.size()-1);
		}
	}

}
