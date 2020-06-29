//CSC 142
//Assignment #3 validateISBN
//HsinYu Chi(Katie)
//Date: November 29 2017
//File name: validateISBN.java

//This program will get ISBN numbers from users, and check if there is any invalid situation.
//Users can input the ISBN whenever with or without the dashes.

//Reflections paragraph:
//I think I struggled a lot at the check sum part. I couldn't figure out that how to locate
//the number from string. I searched on Google and some programming web sites to look for the methods.
//Also, I discuss the logic problems with classmate when we have problems on it.
//I like this assignment because I learn more about ISBN, and it's fun to write a program from zero to
//finish it by myself(and some helps from Google or classmate). Most of the time I need help on condition.
//Sometimes it's confusing that which kind of condition I should use. The best part of assignment is
//when I try to run my codes. At the beginning, there were a lot of struggling and bugs. I found that
//fixing those bugs is kind of fun to do. It feels really good when I finally fun the entire code without
//those bugs.

import java.util.Scanner;

public class validateISBN {

	public static void main(String[] args) {
		
		Scanner cs = new Scanner(System.in);
		String isbn;
		System.out.println("This program will validate the ISBN number from user input.");
		//get the ISBN from user
		System.out.print("Enter the ISBN(type q to quit): ");
		isbn = cs.nextLine();
		
		while(!isbn.equalsIgnoreCase("q")){
			
			countDashes(isbn); //check if it has too many or few dashes.
			if(!(checkPosition(isbn)) && !(checksequence(isbn))){
				//make sure the position and there isn't sequence of dashes in ISBN.
				checkDigits(isbn); //check the length and the sum of ISBN.
			}
			System.out.print("Enter another ISBN(type q to quit): "); //tells user to enter another ISBN.
			isbn = cs.nextLine(); //get the next ISBN from users.
		}
		System.out.println("Thank you for using this program.");
		cs.close();
	}

	private static boolean checkAlphabet(String newisbn, String isbn) {
		for (int u = 0; u < isbn.length(); u++) {//using loop to check each character in String isbn.
			if((Character.isLetter(isbn.charAt(u))) && isbn.charAt(u) != 'X') {
				//if the character is letter and it is not 'X',
				//tells user it is invalid ISBN.
				System.out.println(isbn + " is invalid because it has wrong digit.");
				u = isbn.length();
				return true;
			}
		}
		return false;
	}

	private static void checkDigits(String isbn) {
		String newisbn = isbn.replaceAll( "-", ""); //remove the dashes.
		
		if(newisbn.length() < 10) {//check if the length is too short.
			System.out.println(isbn + " is invalid because it has too few digits.");
		}else if(newisbn.length() > 10){//check if the length is too long.
			System.out.println(isbn + " is invalid because it has too many digits.");
		}else if(!(checkAlphabet(newisbn,isbn)) && (((findDash(isbn) + newisbn.length()) == 13 || ((findDash(isbn) + newisbn.length()) < 13 )&& 
				!((checksequence(isbn)) && !((checkPosition(isbn))))))){
			//if isbn pass the alphabet, length, sequence and position check,
			//program will start to check the sum.
			CheckISBN10(newisbn, isbn);
		}
		
	}
	


	private static boolean checksequence(String isbn) {
		
		for(int i = 0; i <isbn.length(); i++) {
			//using loop to run through each character.
			if(isbn.charAt(i) == '-' && isbn.charAt(i+1) == '-') {
				//check if the following character is the same.
				System.out.println(isbn + " is invalid because it has sequential dashes.");
				return true;
			}
		}
		return false;
		
	}

	private static boolean checkPosition(String isbn) {
		
		if(isbn.charAt(0) == '-') {//check if the first character is dash.
			System.out.println(isbn + " is invalid because it starts with dashes.");
			return true;
		}else if(isbn.charAt(isbn.length()-1) == '-') {//check if the last character is dash.
			System.out.println(isbn + " is invalid because it ends with dashes.");
			return true;
		}
		return false;
	}

	private static void countDashes(String isbn) {
		
		int dash = findDash(isbn);
		
		if (dash > 3) {//check if the dash is over three.
			System.out.println(isbn + " is invalid because it has too many dashes.");
		}else if(dash > 0 && dash < 3) {//check if the dash is less than 3 but greater than 0.
			System.out.println(isbn + " is invalid because it has not enought dashes.");
		}
	}

	private static int findDash(String isbn) {
		
		int dash = 0;
		for (int i = 0; i < isbn.length(); i++) {//count the dash.
			if(isbn.charAt(i) == '-') {
				dash++;
			}
		}
		return dash;
	}

	private static void CheckISBN10(String newisbn, String isbn){

		// sum the digits by times 10, 9, ...,1
		int sum = 0;
		String subIsbn;

		for (int d = 0; d < 10; d++){
			subIsbn = newisbn.substring(d, d+1);
			if (d < 9 || !subIsbn.equals("X")){
				sum += Integer.parseInt(subIsbn) * (10-d);
			}else{
				sum += 10;
			}
		}
		
		if(sum % 11 == 0) {
			System.out.println(isbn + " is a valid ISBN.");
		}else {
			System.out.println(isbn + " is invalid because of wrong check sum.");
		}
	}
}
