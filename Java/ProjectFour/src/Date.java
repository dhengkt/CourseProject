// CSC 142
// Assignment #4 Birthday/Date
// Dilename:Data.java
// Date:12/12/2017
// HsinYu Chi(Katie)
// This program will create a data object, and using methods to 
// complete several things.

//Reflections:
// This assignment is both hard and easy to me.
// The fisrt eight methods are not that hard. I finished them really fast.
// However the hard part are the last two methods.
// I know how to create them without using the class.
// But, I don't know how to put them to the class I created.
// After I asking Tyler and Lyda for help, Tyler told me a easy way to do it.
// However, there is still some errors in there.
// This assignment took me over three hours to do since my logic was wrong at the beginning.
// Also, I'm not reallt familiar with classes and objects.

public class Date {
	private int year;
	private int month;
	private int day;


	public Date(int year, int month, int day) {
		this.year = year;
		this.month = month;
		this.day = day;

	}

	public int getYear() {//get the year from Date data.
		return this.year;
	}

	public int getMonth() {//get the month from Date data.
		return this.month;
	}

	public int getDay() {//get the day from Date data.
		return this.day;
	}

	public String toString() {//format the datas to string.
		return (this.year + "/" + this.month + "/" + this.day);
	}

	public boolean equals(Date d) {//check if the data is the same.
		//if the fields match, its the same date.
		if (d.getYear() == this.year) { 
			if (d.getMonth() == this.month) {
				if (d.getDay() == this.day) {
					return true;
				}
			}
		}
		
		return false;
	}

	public boolean isLeapYear() {//check if the year is a leap year.
		if (this.year % 4 == 0) {
			if (this.year % 100 == 0) {
				if (this.year % 400 == 0) {
					return true;
				} else {
					return false;
				}
			} else {
				return true;
			}
		} else {
			return false;
		}
	}

	public void nextDay() {//find the next day from the Date data.
		@SuppressWarnings("unused")
		int nextD = 0;
		@SuppressWarnings("unused")
		int nextY = 0;
		@SuppressWarnings("unused")
		int nextM = 0;
		
		if (isLeapYear()) {//if it is the leap year Feb will have 29 days.
			if (month == 2) {
				if (day == 29) {
					// Change the month and day by add one and replace to 1 because it's the next month.
					// the year doesn't change because it's not Dec.
					nextM = month + 1;
					nextD = 1;
					nextY = year;
				} else {
					// Change the day by adding one.
					// the year and month don't change because it's still in the same month and year.
					nextM = month;
					nextD = day + 1;
					nextY = year;
				}
			} else if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10
					|| month == 12) {//check if the month has 31 days.
				if (day >= 1 && day < 31) {
					// Change the day by adding one on it.
					// the month and year don't change becasue it's in the same month and year.
					nextM = month;
					nextD = day + 1;
					nextY = year;
				} else if (day == 31) {
					if (month == 12) {
						// Change the day by adding one. It's going to be the next year because it's Dec.
					    // So month will be Jan, and year has to plus one.
						nextM = 1;
						nextD = 1;
						nextY = year + 1;
					}
				}
			} else if (month == 4 || month == 6 || month == 9 || month == 11) {
				if (day >= 1 && day < 30) {
					// Change the day by adding one on it.
					// the month and year don't change becasue it's in the same month and year.
					nextM = month;
					nextD = day + 1;
					nextY = year;
				} else if (day == 30) {
					// Change the month by adding one on it. And it's going to be next month, 
					// so month has to add one.
					// The year doesn't change becasue it's in the same month and year.
					nextM = month + 1;
					nextD = 1;
					nextY = year;
				}
			}
		} else {//when the year isn't leap year.
			if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
				if (day >= 1 && day < 31) {
					// Change the day by adding one on it.
					// the month and year don't change becasue it's in the same month and year.
					nextM = month;
					nextD = day + 1;
					nextY = year;
				} else if (day == 31) {
					if (month == 12) {
						// Change the day by adding one. It's going to be the next year because it's Dec.
					    // So month will be Jan, and year has to plus one.
						nextM = 1;
						nextD = 1;
						nextY = year + 1;
					}
				}
			} else if (month == 4 || month == 6 || month == 9 || month == 11) {
				if (day >= 1 && day < 30) {
					// Change the day by adding one on it.
					// the month and year don't change becasue it's in the same month and year.
					nextM = month;
					nextD = day + 1;
					nextY = year;
				} else if (day == 30) {
					// Change the month by adding one on it. And it's going to be next month, 
					// so month has to add one.
					// The year doesn't change becasue it's in the same month and year.
					nextM = month + 1;
					nextD = 1;
					nextY = year;
				}
			} else if (month == 2) {
				if (day < 28 && day >= 1) {
					// Change the day by adding one.
					// the year and month don't change because it's still in the same month and year.
					nextM = month;
					nextD = day + 1;
					nextY = year;
				} else if (day == 28) {
					// Change the month and day by add one and replace to 1 because it's the next month.
					// the year doesn't change because it's not Dec.
					nextM = month + 1;
					nextD = 1;
					nextY = year;
				}
			}
		}
		
	}

	public int advanceTo(Date endDay) {
		int totalDay = 0;
		while (!(this.equals(endDay))) { //count the day while it's still not endDay.
			nextDay();
			totalDay++;
		}
		return totalDay;
	}
	
	public String getDayOfWeek() {
		String[] weekdays = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
		Date origin = new Date(1753, 1, 1);
		// Takes the distance between the two dates and divides by 7 to determine which day of the week it is
		String DayofWeek = weekdays[origin.advanceTo(this)%7]; 

		return DayofWeek;
	}
	
}
