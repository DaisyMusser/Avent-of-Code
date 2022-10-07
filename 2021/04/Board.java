import java.util.ArrayList;

/* Represents a bingo board */
public class Board {
    private Square[][] contents = new Square[5][5]; // Contents of the board
    private int lastCall;
    private int winningCall;

    /* Contrustor 
     * @param input - list of strings read from the input file
     */
    public Board(String[] bInput) { 
        // First make deep string list
        int[][] deepIntList = new int[5][5];
        String[] lineList = new String[5];
        for (int row = 0; row < 5; row++) {
            lineList = mySplit(bInput[row]);
            for (int col = 0; col < 5; col++) {
                deepIntList[row][col] = Integer.parseInt(lineList[col]); 
            }
        }
        // Make squares and fill up contents
        for (int row = 0; row < 5; row ++) {
            for (int col = 0; col < 5; col++) {
                contents[row][col] = new Square(deepIntList[row][col]);
            }
        }
    }

    /* Runs a call on a given number */
    public void call(int number) {
        lastCall = number;
        // Mark everything that matches
        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                contents[row][col].check(number);
            }
        }
    }

    /* Updates winner and returns it 
     * ~Very~ untested
     */
    public boolean isWinner() {
        // Check across
        int col = 0;
        for (int row = 0; row < 5; row++) {
            if (contents[row][col].isMarked()) { // Only walk across row if the first is marked
                for (col = 1; col < 5; col++) { // Start at 2nd square bc above line already checks first
                    if (!contents[row][col].isMarked()) { // Bail if you hit something unmarked
                        return checkVertical();
                    } else if (col == 4) { // We got one!
                        winningCall = lastCall;
                        return true;
                    }
                }
            }
        }
        return checkVertical();
    }

    /* Helper checks for vertical wins */
    private boolean checkVertical() {
        int row = 0;
        for (int col = 0; col < 5; col++) {
            if (contents[row][col].isMarked()) { // Only walk across row if the first is marked
                for (row = 1; row < 5; row++) { // Start at 2nd square bc above line already checks first
                    if (!contents[row][col].isMarked()) { // Bail if you hit something unmarked
                        return false;
                    } else if (row == 4) { // We got one!
                        winningCall = lastCall;
                        return true;
                    }
                }
            }
        }
        return false;
    }

    /* Gets the score of a board. Socre is:
     * sum of all unmarked numbers
     * times the winning call (lastCall)
     */
    public int getScore() {
        int sum = 0;
        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                if (!(contents[row][col].isMarked())) {
                    sum += contents[row][col].getNumber();
                }
            }
        }
        return sum * winningCall;
    }

    /* Getter for lastCall */
    public int getLastCall() {
        return lastCall;
    }

    /* Getter for contents */
    public Square[][] getContents() {
        return contents;
    }
    
    /* Helper to get string list from line without white space 
     * Seems to work!
     */
    private static String[] mySplit(String input) {
        String[] lineList = new String[]{"","","","",""};
        int c = 0;
        int n = 0;
        for (int i = 0; i < 14; i++) {
            if ((i != 2) && (i != 5) && (i != 8) && (i != 11)) { // If it's not a gap
                if (c == 2) { 
                    c = 0;
                    n++;
                }
                if (!(input.charAt(i) == ' ')) { // And not a space anyway 
                    lineList[n] += String.valueOf(input.charAt(i));
                    }
                c++; // c is incemented for every non gap
                }
            }
        return lineList;
    }

    /*
	// A little testing
    public static void main(String[] args) {
        String[] snag = mySplit(" 4 28 36  9 38");
	    for (String s: snag) {
            System.out.println(s);
        }        
	}
	*/	

}
