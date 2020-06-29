import java.awt.Point;

public class Line{
    private Point p1;
    private Point p2;

    public Line(Point p1, Point p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public Point getP1() {
        return p1;
    }

    public Point getP2() {
        return p2;
    }

    public String toString(Point p) {
        return "(" + p.x + ", " + p.y + ")";
    }

    public String toString() {
        return "[" + toString(p1) + ", " + toString(p2) + "]";
    }
}