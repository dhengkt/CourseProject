import java.util.Scanner;

public class TheElevator {

	public static int user = 0; 
    public static int user2 = 0;
    public static int elevator = 0;

    public static void main(String[] args) {
    	
        Scanner cs = new Scanner (System.in);
        user = getUsersFloor(cs);
        elevator = getElevator();
        verifyFloor(user,elevator);
        
    }

	private static void verifyFloor(int usr, int elva) {
		
		
		
	}

	private static int getElevator() {
		
		elevator = (int)(Math.random()*7);
		return elevator;
	}

	private static int getUsersFloor(Scanner cs) {
		System.out.print("Which floor is it? ");
		user = cs.nextInt();
		return user;
	}
	
	

}
