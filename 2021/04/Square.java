
/* Represents squares on a bingo board */
public class Square {
    private int number;
    private boolean marked;

    /* Constructor */
    public Square(int number) {
        this.number = number;
        marked = false;
    }

    /* Getter for number */
    public int getNumber() {
        return number;
    }

    /* Getter for marked */
    public boolean isMarked() {
        return marked;
    }

    /* Checks a square agaisnt number passed in, marks if needed 
     * @param number - number that was called
     */ 
    public void check(int number) {
        if (this.number == number) {
            marked = true;
        }
    }
}

