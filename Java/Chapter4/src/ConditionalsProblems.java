import java.util.Scanner;

public class ConditionalsProblems {
	
	static String[] months = new String[] {"January","February","March","April","May","June","July","August","September","October","November","December"};
	
	
	public static void main(String[] args) {
		
		Scanner console = new Scanner(System.in);
		System.out.print("Enter your birthday date(mm dd yyyy): ");
		int month = console.nextInt();
		int day = console.nextInt();
		int year = console.nextInt();
		
//		if (leapyear(year)) {
//			System.out.println(year + " is a leap year.");
//		}
//		else {
//			System.out.println(year + " is NOT a leap year.");
//		}
		
//		if(vailddate(year, month, day)) {
//			System.out.printf("%d/%d is a vaild date.", month, day);
//			seasons(month, day);
//		}
//		else {
//			System.out.printf("%d/%d is not a vaild date.", month, day);
//		}
		
//		nextDay(year, month, day);
		
		System.out.print("Enter an advance date(mm dd yyyy): ");
		int m = console.nextInt();
		int d = console.nextInt();
		int y = console.nextInt();
		advanceTo(year, month, day, y, m, d);
	
		
		console.close();
	}
	
	private static void advanceTo(int year, int month, int day, int y, int m, int d) {
		int leap = 0;
		int m2 = 0;
		int m30s = 0;
		int m31s = 0;
		int totalDays = 0;
		
		for (int i = year; i < y; i++) {
			if(leapyear(i)) {
				leap++;
			}
		}
		
		if (month < m) {
			for (int i = month; i < m; i++) {
				if(i == 1 || i == 3 || i == 5 || i == 7 || i == 8 || i == 10|| i == 12) {
					m31s++;
				}else if (i == 4 || i == 6 || i == 9 || i == 11) {
					m30s++;
				}else {
					m2++;
				}
			}
			
			if(leapyear(y)) {
				totalDays = (d - day) + (m30s * 30) + (m31s * 31) + (m2 * 29) + ((y-year-leap) * 365) + (leap * 366);
			}else {
				totalDays = (d - day) + (m30s * 30) + (m31s * 31) + (m2 * 28) + ((y-year-leap) * 365) + (leap * 366);
			}
		}else if (month > m) {
			for (int i = month; i < (Math.abs(m-month) + m); i++) {
				if(i == 1 || i == 3 || i == 5 || i == 7 || i == 8 || i == 10|| i == 12) {
					m31s++;
				}else if (i == 4 || i == 6 || i == 9 || i == 11) {
					m30s++;
				}else {
					m2++;
				}
			}
			if(leapyear(y)) {
				totalDays = (d - day) - ((m30s * 30) + (m31s * 31) + (m2 * 29)) + ((y-year-leap) * 365) + (leap * 366);
			}else {
				totalDays = (d - day) - ((m30s * 30) + (m31s * 31) + (m2 * 28)) + ((y-year-leap) * 365) + (leap * 366);
			}
		}else {
			if (leapyear(y)) {
				totalDays = (d - day) + ((y-year-leap) * 365) + (leap * 366);
			}else {
				totalDays = (d - day) + ((y-year-leap) * 365) + (leap * 366);
			}
		}
		
		System.out.println(totalDays);
		
	}

	public static boolean leapyear(int year) {
		if (year % 4 == 0) {
			if (year % 100 == 0) {
				if (year % 400 == 0) {
					return true;
				}
				else {
					return false;
				}
			}
			else {
				return true;
			}
		}
		else {
			return false;
		}
	}
	
	public static boolean vailddate(int year, int month, int day) {
		if (year > 0) {
			if (month >= 1) {
				if (month <= 12) {
					if (day >= 1) {
						if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10
								|| month == 12) {
							if (day <= 31) {
								return true;
							} else {
								return false;
							}
						} else if (month == 4 || month == 6 || month == 9 || month == 11) {
							if (day <= 30) {
								return true;
							} else {
								return false;
							}
						} else {
							if (leapyear(year)) {
								if (day <= 29)
									return true;
								else
									return false;
							} else {
								if (day <= 28)
									return true;
								else
									return false;
							}
						}
					} else {
						return false;
					}
				} else {
					return false;
				}
			} else {
				return false;
			}
		} else {
			return false;

		}
	}
	
	public static void nextDay(int year, int month, int day) {
		int nextD = 0;
		int nextY = 0;
		int nextM = 0;
		if (leapyear(year)) {
			if(month == 2) {
				if (day == 29) {
					nextM = month +1;
					nextD = 1;
					nextY = year;
				}else {
					nextM = month;
					nextD = day + 1;
					nextY = year;
				}
			}else if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10
					|| month == 12) {
				if(day >= 1 && day < 31) {
					nextM = month;
					nextD = day + 1;
					nextY = year;
				}else if(day == 31) {
					if (month == 12) {
						nextM = 1;
						nextD = 1;
						nextY = year + 1;
					}else {
						nextM = month + 1;
						nextD = day + 1;
						nextY = year;
					}
				}
			}else if(month == 4 || month == 6 || month == 9 || month == 11) {
				if(day >= 1 && day < 30) {
					nextM = month;
					nextD = day + 1;
					nextY = year;
				}else if (day == 30) {
					nextM = month + 1;
					nextD = 1;
					nextY = year;
				}
			}
		}else {
			if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10
					|| month == 12) {
				if(day >= 1 && day < 31) {
					nextM = month;
					nextD = day + 1;
					nextY = year;
				}else if(day == 31) {
					if (month == 12) {
						nextM = 1;
						nextD = 1;
						nextY = year + 1;
					}else {
						nextM = month +1;
						nextD = 1;
						nextY = year;
					}
				}
			}else if(month == 4 || month == 6 || month == 9 || month == 11) {
				if(day >= 1 && day < 30) {
					nextM = month;
					nextD = day + 1;
					nextY = year;
				}else if (day == 30) {
					nextM = month + 1;
					nextD = 1;
					nextY = year;
				}
			}else if (month == 2) {
				if (day < 28 && day >= 1) {
					nextM = month;
					nextD = day + 1;
					nextY = year;
				}else if (day == 28){
					nextM = month + 1;
					nextD = 1;
					nextY = year;
				}
			}
		}
		
		String msg = "";
		if (nextM == 1) {
			msg = months[0];
		}else if(nextM == 2) {
			msg = months[1];
		}else if (nextM == 3) {
			msg = months[2];
		}else if (nextM == 4) {
			msg = months[3];
		}else if (nextM == 5) {
			msg = months[4];
		}else if (nextM == 6) {
			msg = months[5];
		}else if (nextM == 7) {
			msg = months[6];
		}else if (nextM == 8) {
			msg = months[7];
		}else if (nextM == 9) {
			msg = months[8];
		}else if (nextM == 10) {
			msg = months[9];
		}else if (nextM == 11) {
			msg = months[10];
		}else if (nextM == 12) {
			msg = months[11];
		}
		System.out.println("The next day is " + msg + " " + nextD + ", " + nextY + ".");
	}
	
	public static void seasons(int month, int day) {
		String msg = "";
		if (month == 12) {
			if (day <= 20) {
				msg = "Fall";
			}
			else {
				msg = "Winter";
			}
		}
		else if (month == 9) {
			if (day >= 22) {
				msg = "Fall";
			}
			else {
				msg = "Summer";
			}
		}
		else if (month == 10) {
			msg = "Fall";
		}
		else if (month == 11) {
			msg = "Fall";
		}
		else if (month == 8) {
			msg = "Summer";
		}
		else if (month == 7) {
			msg = "Summer";
		}
		else if (month == 6) {
			if (day <= 19) {
				msg = "Spring";
			}
			else {
				msg = "Summer";
			}
		}
		else if (month == 5) {
			msg ="Spring";
		}
		else if (month == 4) {
			msg = "Spring";
		}
		else if (month == 3) {
			if (day >=20) {
				msg = "Spring";
			}
			else {
				msg = "Winter";
			}
		}
		else if (month == 2) {
			msg = "Winter";
		}
		else if (month == 1) {
			msg = "Winter";
		}
		System.out.println("");
		System.out.printf("%d/%d in 2017 is %s.", month, day, msg);
		
	}

}
