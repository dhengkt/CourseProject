import java.util.Scanner;

public class problems {

	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		System.out.print("How many days' temperatures? ");
		int numofdays = console.nextInt();
		int [] temps = new int [numofdays];
		getData(temps,console);
		double avg = findAverage(temps);
		int num = findDaysAboveAvg(temps,avg);
		System.out.printf("Average of all temperatures is %.1f.\n", avg);
		System.out.println(num + " days are above average.");
	}

	public static void getData(int [] temps, Scanner console){

		for (int i = 0;i < temps.length; i++) {
			System.out.printf("Day %d's high temp: ",(i+1));
			int daytemp = console.nextInt();
			temps [i] = daytemp;
		}
	}

	public static double findAverage(int [] temps){

		int total =0;

		for (int i = 0; i < temps.length;i++){
			total += temps[i];
		}
		return ((float)(total)/temps.length);
	}

	public static int findDaysAboveAvg(int [] temps, double avg){

		int num = 0;
		
		for (int i=0; i<temps.length; i++){
			if (temps[i] > avg){
				num++;
			}
			else{
			}
		}
		return num;
	}

}
