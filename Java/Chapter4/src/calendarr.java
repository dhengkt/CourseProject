import java.util.Scanner;

public class calendarr {
	public static void main(String arg[]) {
		int id, im, iy;
		Scanner ip = new Scanner(System.in);
		System.out.print("Enter DD MM YYYY : ");
		id = ip.nextInt();
		im = ip.nextInt();
		iy = ip.nextInt();
		System.out.print("\n");

		int totalDays = 0, leapYearDays = 366, ordinaryYearDays = 365, y = iy - 1, day = 0;
		int totalDaysOfGivenYear, totalDaysUptoGivenMonth = 0, totalDaysEntire;
		int leapYearCount = 0;
		// calculate the number of leap and non leap years
		for (int i = 0; i <= y; i++) {
			if ((i % 4 == 0) && (i % 100 != 0) || (i % 400 == 0)) {
				leapYearCount++;
			}
		}
		int ordinaryYearCount = y - leapYearCount;
		//int totalDaysUptoPreviousYear = 0;
		int totalDaysUptoPreviousYearCount = (leapYearCount * leapYearDays) + (ordinaryYearCount * ordinaryYearDays);
		System.out.print("Odd Days Leap Year and Ordinary Year : " + leapYearCount + " " + ordinaryYearCount + "\n");

		//String[] months = new String[] { "January", "February", "March", "April", "May", "June", "July", "August",
		//		"September", "October", "November", "December" };
		int[] monthDates = new int[] { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
		String[] weekDays = new String[] { "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
				"Friday" };

		if ((iy % 4 == 0) && (iy % 100 != 0) || (iy % 400 == 0)) {
			monthDates[2] = 29;
			System.out.println("It is Leap Year");
		} else
			System.out.println("It is Ordinary Year");

		for (int i = 1; i <= monthDates.length; i++) {
			totalDays = totalDays + monthDates[i - 1];
		}
		for (int j = 1; j < im; j++) {
			totalDaysUptoGivenMonth = totalDaysUptoGivenMonth + monthDates[j];

		}
		totalDaysOfGivenYear = totalDaysUptoGivenMonth + id;

		System.out.println("Total Days Upto Given Months : " + totalDaysOfGivenYear + "\nTotal Days of given year :  "
				+ iy + " : " + totalDays);

		System.out.println("Total Count : " + totalDaysUptoPreviousYearCount);

		totalDaysEntire = totalDaysUptoPreviousYearCount - totalDays + totalDaysOfGivenYear;
		// totalDaysEntire = totalDaysUptoPreviousYearCount+ totalDaysOfGivenYear;
		System.out.println("Overall Total Days : " + totalDaysEntire);

		/*
		 * //day = (365+366-totalDays+totalDaysUptoPreviousYearCount)%7;
		 * 
		 * for(int k=0;k<=y;k++) {
		 * 
		 * day = (totalDaysEntire%7);
		 * 
		 * 
		 * 
		 * System.out.println(day+"\n"+weekDays[day]+"\n\n"); }
		 */

		day = (totalDaysEntire % 7);

		System.out.println(day + "\n" + weekDays[day] + "\n\n");
		ip.close();
	}
	

}