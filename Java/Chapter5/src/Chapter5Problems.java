import java.util.Scanner;

public class Chapter5Problems {

	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		System.out.printf("The sum of those numbers is %d.",sumofNums(console));
		Speed(console);
		tossCoin(1000000);
		rollDice(10);
		rolltwoDices(10);
		rollDiceToThree12();
		rollDiceThree12InARoll();
		console.close();
	}
	
	private static void rollDiceThree12InARoll() {
		int dice1 = (int)(Math.random()*6+1);
		int dice2 = (int)(Math.random()*6+1);
//		int roll1 = 0; int roll2 = 0; int roll3 = 0;
//		int count12s = 0;
		while ((dice1+dice2) != 12) {
			dice1 = (int)(Math.random()*6+1);
			dice2 = (int)(Math.random()*6+1);
		}
		
	}

	private static void rollDiceToThree12() {
		int dice1 = (int)(Math.random()*6+1);
		int dice2 = (int)(Math.random()*6+1);
		int count12s = 0;
		int counts = 1;
		while (count12s != 3) {
			System.out.println("Dice 1 + Dice 2 = " + (dice1+dice2));
			if (dice1+dice2 == 12) {
				++count12s;
			}
			dice1 = (int)(Math.random()*6+1);
			dice2 = (int)(Math.random()*6+1);
			++counts;
		}
		System.out.println("It took " + counts + " rolls to roll a total of 12.");
		
	}

	private static void rolltwoDices(int time) {
		int sum7 = 0;
		for (int i = 1; i <= time; i++) {
			int dice1 = (int)(Math.random()*6+1);
			int dice2 = (int)(Math.random()*6+1);
			if(dice1 + dice2 == 12) {
				++sum7;
			}
		}
		System.out.println("The 7 came up " + sum7 + " times.");
		
	}

	private static void rollDice(int time) {
		int face6 = 0; int face5 = 0; int face4 = 0;
		int face3 = 0; int face2 = 0; int face1 =0;
		for (int i = 1; i <= time; i++) {
			int roll = (int)(Math.random()*6)+1;
			if (roll == 6) {
				++face6;
			}else if (roll == 5) {
				++face5;
			}else if(roll == 4) {
				++face4;
			}else if (roll == 3) {
				++face3;
			}else if (roll == 2) {
				++face2;
			}else {
				++face1;
			}
		}
		System.out.println("The face 6 came up " + face6 + " times.");
		System.out.println("The face 5 came up " + face5 + " times.");
		System.out.println("The face 4 came up " + face4 + " times.");
		System.out.println("The face 3 came up " + face3 + " times.");
		System.out.println("The face 2 came up " + face2 + " times.");
		System.out.println("The face 1 came up " + face1 + " times.");
	}

	private static void tossCoin(int times) {
		int tails = 0;
		for (int i =1; i <= times; i++) {
			int toss = (int)(Math.random()*6);
			if (toss < 0.5) {
				++tails;
			}
		}
		System.out.println("Tails: " + tails);
		System.out.println("Heads: " + (times-tails));
		
	}

	private static void Speed(Scanner console) {
		System.out.println("Enter speed: ");
		int speed = console.nextInt();
		
		while(!(speed >= 25) || !(speed <= 60)) { //speed in range 25 - 60 inclusive
			System.out.println("Try again...enter speed: ");
			speed = console.nextInt();
		}
		System.out.println("Thank you for driving safely!");
	}

	private static int sumofNums(Scanner console) {
		System.out.print("Enter values >= 0 (-ve val to exit): ");
		
		int number = console.nextInt();
		int b = 0;
		
		while (number >= 0) {
			b += number;
			System.out.print("Enter values >= 0 (-ve val to exit): ");
			number = console.nextInt();
		}
		return b;
	}

}
