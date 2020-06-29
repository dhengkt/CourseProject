// CSC 142
// Assignment #4 Birthday/Date
// Dilename:DataClient.java
// Date:12/12/2017
// HsinYu Chi(Katie)
// This program will test all the methods I created in Data.java.
// It takes user inputs and constructs two Date objects from them, 
// then outputs the day the user was born on and how many days old they are.

import java.util.Scanner;

public class DateClient {

	public static void main(String[] args) {
		//Get the input from user.
		Scanner console = new Scanner (System.in);
		System.out.print("What is today's date (month day year)? ");
		int month = console.nextInt();
		int day = console.nextInt();
		int year = console.nextInt();
		Date today = new Date(year, month, day);
	
		//Get the birthday from user.
		System.out.print("What is your birthday (month day year)? ");
		int bDayMonth  = console.nextInt();
		int bDayDay  = console.nextInt();
		int bDayYear  = console.nextInt();
		Date bDay = new Date(bDayYear, bDayMonth, bDayDay);
		
		System.out.printf("You were born on %s, which was on a %s. \n", bDay.toString(), bDay.getDayOfWeek());
		if (bDay.isLeapYear()) {
			System.out.printf("%d was a leap year. \n", bDay.getYear());
		}
		System.out.printf("You are %d days old. \n", bDay.advanceTo(today));
		
		console.close();
		
	}
	
	
}
