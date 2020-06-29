
public class GroceryList {
	private GroceryItem[] list;
	private static final int SIZE = 10;

	public GroceryList() {
		list = new GroceryItem[SIZE];
	}

	public boolean add(GroceryItem item) {
		boolean done = false;

		for (int i = 0; i < list.length && !done; i++) {
			if (list[i] == null) {
				list[i] = item;
				return done = true;
			}
		}
		return done;
	}

	public double getTotalCost() {
		double total = 0.0;
		for (int i = 0; i < list.length; i++) {
			if (list[i] != null) {
				total += list[i].getTotalPrice();
			}
		}
		return total;
	}

	public String toString() {
		String result = "";
		for (int i = 0; i < list.length; i++) {
			if (list[i] != null) {
				result += list[i].toString() + "\n";
			}
		}
		return result;
	}

}
