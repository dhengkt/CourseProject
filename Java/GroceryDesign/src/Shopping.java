
public class Shopping {

	public static void main(String[] args) {

		GroceryList myList = new GroceryList();
		myList.add(new GroceryItem("Eggs", 24, 0.25));
		myList.add(new GroceryItem("Beef", 6, 5.27));
		myList.add(new GroceryItem("Coke", 6, 0.99));
		myList.add(new GroceryItem("Bread", 2, 3.29));
		
		System.out.println(myList);
		System.out.println("The above items will cost you $" + myList.getTotalCost());
	}

}
