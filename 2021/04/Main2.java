import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;

public class Main2 {
    public static void main(String[] args) {
        try {
            ArrayList<Board> winners = new ArrayList<Board>();
            Scanner in = new Scanner(new FileInputStream("input.txt"));
            // Now we have a in Scanner
            ArrayList<Board> boards = new ArrayList<Board>(); // Will hold all boards in game
            String[] stringNumsToCall = in.nextLine().split(","); // Get numbers that will be called
            int[] numsToCall = new int[stringNumsToCall.length]; 
            int i = 0;
            // Get from strings to ints
            for (String s: stringNumsToCall) {
                numsToCall[i] = Integer.parseInt(s);
                i++;
            }
            String[] boardStringArray = new String[5]; // Empty string array to load with board strings
            int lineCount = 0;
            in.nextLine(); // Gobbles first blank line
            while (in.hasNextLine()) {
                String line = in.nextLine();
                if (line.equals("\n")) {
                    // Gobble blank lines
                } else if (lineCount < 5) {
                    // Load up Board String array
                    boardStringArray[lineCount] = line;
                    lineCount++;
                } else { 
                    // Makes and adds new board
                    boards.add(new Board(boardStringArray));
                    lineCount = 0; // Reset lineCount for next Board 
                }
            }
            boards.add(new Board(boardStringArray)); // Add the last board
            for (int num: numsToCall) {
            	for (Board b: boards) { 
            		b.call(num); // Call each number on each board
            		if (!(winners.contains(b))) { // Only add if it hasn't already won
            			if (b.isWinner()) {
            				winners.add(b);
                            if (winners.size() == boards.size()) {
                                int index = 0;
                                for (int number: numsToCall) {
                                    if (number == num) {
                                        break;
                                    }
                                    index++;
                                }
                                System.out.println(index);
                                System.out.println(winners.get(winners.size() - 1).getScore());
                                System.exit(0);
                            }
            			}
            		}
            	}
            }
        } catch (FileNotFoundException e) {
            System.out.println("No input.txt found");
        }
    }
}
    
