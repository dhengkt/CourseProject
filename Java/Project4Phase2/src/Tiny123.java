import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;

public class Tiny123 {
	public static void main(String[] args) {
		Sheet sht = new Sheet();

		System.out.println("Initial State");
		System.out.println(sht + "\n");

		sht.insertRow(0);
		System.out.println("Insert Row 0");
		System.out.println(sht + "\n");

		sht.deleteRow(8);
		System.out.println("Delete Row 8");
		System.out.println(sht + "\n");

		sht.insertCol(0);
		System.out.println("Insert Col 0");
		System.out.println(sht + "\n");

		sht.deleteCol(6);
		System.out.println("Delete Col 6");
		System.out.println(sht + "\n");

		for (int row = 1; row <= 3; row++) {
			for (int col = 1; col <= 3; col++) {
				sht.setValue(row, col, "" + ((row - 1) * 3 + col));
			}
		}
		System.out.println("Fill 3x3 array");
		System.out.println(sht + "\n");

		sht.insertRow(2);
		sht.insertRow(4);
		sht.insertCol(2);
		sht.insertCol(4);
		System.out.println("Insert Row 2,4, Col 2,4");
		System.out.println(sht + "\n");

		for (int i = 10; i >= 6; i--) {
			sht.deleteRow(i);
			sht.deleteCol(i);
		}
		System.out.println("Delete Row 10-6, Col 10-6");
		System.out.println(sht + "\n");

		for (int i = 0; i <= 5; i++) {
			sht.deleteRow(0);
			sht.deleteCol(0);
		}
		System.out.println("Delete Row 0x6, Col 0x6");
		System.out.println(sht + "\n");
	}

}

class Sheet {
	private LinkedList<SheetRow> rows;

	/*
	 * Contructor
	 * Creates a 9x9 sheet of cells “R<1..9>C<1..9>”
	 */
	public Sheet() {
		this.rows = new LinkedList<SheetRow>();
		for (int i = 1; i <= 9; i++) {
			this.rows.add(new SheetRow(i));
		}
	}

	/*
	 * Inserts row at 0-based index
	 * @param int row
	 */
	public void insertRow(int row) {
		this.rows.add(row, new SheetRow(row));
	}

	/*
	 * Deletes row at 0-based index
	 * @param int row
	 */
	public void deleteRow(int row) {
		this.rows.remove(row);
	}

	/*
	 *  Inserts col at 0-based index “R…C<col>” in each row
	 *  @param int col
	 */
	public void insertCol(int col) {
		Iterator<SheetRow> itr = this.rows.iterator();
		int count = 0;
		while (itr.hasNext()) {
			itr.next().addCell(col, "R" + count + "C" + col);
			count++;
		}
	}

	/*
	 * Deletes col at 0-based index in each row
	 * @param int col
	 */
	public void deleteCol(int col) {
		Iterator<SheetRow> itr = this.rows.iterator();
		int count = 0;
		while (itr.hasNext()) {
			itr.next().removeCell(col);
			count++;
		}
	}

	/*
	 * set string value
	 * @param int row, int col, String s
	 */
	public void setValue(int row, int col, String s) {
		this.rows.get(row).setValue(col, s);
	}

	/*
	 * print out the whole sheet
	 * @return
	 */
	@Override
	public String toString() {
		LinkedList<Integer> sums = new LinkedList<Integer>();
		String rst = "";

		// Read through each rows
		for (SheetRow row : this.rows) {
			// Set string str to be the whole line
			// str = "R1C0 1 2 3 R1C4 R1C5 R1C7 R1C8 R1C9 Sum = 6"
			String str = row.toString();
			LinkedList<String> tempRow = new LinkedList<String>();
			// Read through the whole string, and breaks it down to following.
			// s1 = "R1C0", "1", "2", "3", "R1C4", "R1C5", "R1C7", "R1C8", "R1C9", "Sum",
			// "=", "6"
			Scanner sc1 = new Scanner(str);

			// Add them to the LinkedList tempRow
			// tempRow = ["R1C0", "1", "2", "3", "R1C4", "R1C5", "R1C7", "R1C8", "R1C9",
			// "Sum", "=", "6"]
			while (sc1.hasNext()) {
				tempRow.add(sc1.next());
			}
			// Close the scanner first.
			sc1.close();

			// Modify the size of LinkedList sums, and put 0 in each node first.
			// sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			if (sums.isEmpty()) {
				for (int i = 0; i < tempRow.size(); i++) {
					sums.add(i, 0);
				}
			}

			// Scanner each node in tempRow, and only add integers to sums.
			for (int j = 0; j < tempRow.size(); j++) {
				// Another scanner to read each node.
				Scanner sc2 = new Scanner(tempRow.get(j));
				int value = 0;

				// If the node contains integer, set value to be that integer.
				if (sc2.hasNextInt()) {
					value = sc2.nextInt();
				}
				// Add the value to sum, and put it into LinkedList sums.
				// Close the scanner sc.
				int sum = sums.get(j) + value;
				sums.set(j, sum);
				sc2.close();
			}
			// This is original toString.
			rst += "\n" + row;
		}

		// Add a new String to store the sum.
		String rstSum = "";

		// Run through the sums, and add the String value to rstSum.
		// sums.size() has to -2 because the last two items are not need.
		// "Sum" "=" "6" become [..., 0, 0, 0]
		// It's not a part of the colum we need to count sum.
		for (int k = 0; k < sums.size() - 2; k++) {
			rstSum += String.format("%-8s", "Sum=" + sums.get(k));
		}
		return rst + "\n" + rstSum;
	}
}

class SheetRow {
	private LinkedList<String> cells;

	/*
	 * Contructor
	 * Creates 9 column of cells “R<row>C<1..9>”
	 * @param int row
	 */
	public SheetRow(int row) {
		LinkedList<String> list = new LinkedList<String>();
		for (int i = 1; i <= 9; i++) {
			list.add("R" + row + "C" + i);
		}

		this.cells = list;
	}

	/*
	 * Adds 0-based col to this row
	 * @param int index, String s
	 */
	public void addCell(int index, String s) {
		this.cells.add(index, s);
	}
	
	/*
	 * removes 0-based col from this row
	 * @param int index
	 */
	public void removeCell(int index) {
		this.cells.remove(index);
	}

	/*
	 * sets value at col
	 * @param int cell, String s
	 */
	public void setValue(int cell, String s) {
		this.cells.set(cell, s);
	}

	/*
	 * print out each row
	 * @return
	 */
	@Override
	public String toString() {
		String rst = "";
		int sum = 0;

		for (String cell : this.cells) {
			// Create a scanner to read each item.
			Scanner sc = new Scanner(cell);
			// If it's integer, add it to the sum.
			while (sc.hasNextInt()) {
				sum += sc.nextInt();
			}
			sc.close();
			rst += String.format("%-8s", cell);
		}
		return rst + "Sum = " + sum;
	}
}