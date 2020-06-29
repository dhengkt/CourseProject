
public class GroceryItem {
	private String name;
	private int quantity;
	private double price;
	
	public GroceryItem(String n, int q, double p) {
		super();
		name = n;
		quantity = q;
		price = p;
	}
	
	public String getName() {
		return name;
		
	}
	
	public void setName(String n) {
		name = n;
	}
	
	public int getQuantity() {
		return quantity;
		
	}
	
	public void setQuantity(int q) {
		quantity = q;
	}
	
	public double getTotalPrice() {
		return price * quantity;
		
	}
	
	public void setPrice(double p) {
		price = p;
	}
	
	public String toString() {
		return ( name + "\t" + quantity + "\t$" + price);
	}
	
}
