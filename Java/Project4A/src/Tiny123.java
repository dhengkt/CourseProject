import java.util.*;

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

	// creates a 9x9 sheet of cells “R<1..9>C<1..9>”
	public Sheet() {
		this.rows = new LinkedList<SheetRow>();
		for (int i = 1; i <= 9; i++) {
			this.rows.add(new SheetRow(i));
		}
	}

	// inserts row at 0-based index
	public void insertRow(int row) {
		this.rows.add(row, new SheetRow(row));
	}

	// deletes row at 0-based index
	public void deleteRow(int row) {
		this.rows.remove(row);
	}

	// inserts col at 0-based index “R…C<col>” in each row
	public void insertCol(int col) {
		Iterator<SheetRow> itr = this.rows.iterator();
		int count = 0;
		while (itr.hasNext()) {
			itr.next().addCell(col, "R" + count + "C" + col);
			count++;
		}
	}

	// deletes col at 0-based index in each row
	public void deleteCol(int col) {
		Iterator<SheetRow> itr = this.rows.iterator();
		int count = 0;
		while (itr.hasNext()) {
			itr.next().removeCell(col);
			count++;
		}
	}

	// sets String value
	public void setValue(int row, int col, String s) {
		this.rows.get(row).setValue(col, s);
	}

	@Override
	public String toString() {
		String rst = "";
		for (SheetRow row : this.rows) {
			rst += "\n" + row.toString();
		}
		return rst;
	}
}

class SheetRow {
	private LinkedList<String> cells;

	// creates 9 column of cells “R<row>C<1..9>”
	public SheetRow(int row) {
		LinkedList<String> list = new LinkedList<String>();
		for (int i = 1; i <= 9; i++) {
			list.add("R" + row + "C" + i);
		}

		this.cells = list;
	}

	// adds 0-based col to this row
	public void addCell(int index, String s) {
		this.cells.add(index, s);
	}

	// removes 0-based col from this row
	public void removeCell(int index) {
		this.cells.remove(index);
	}

	// sets value at col
	public void setValue(int cell, String s) {
		this.cells.set(cell, s);
	}

	@Override
	public String toString() {
		String rst = "";
		for (String cell : this.cells) {
			rst += String.format("%-8s", cell);
		}
		return rst;
	}
}