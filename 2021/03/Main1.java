import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class Main1 {
    public static void main(String[] args) {
        try {
            Scanner in = new Scanner(new FileInputStream("input.txt"));
            int[] countOnes = new int[]{0,0,0,0,0,0,0,0,0,0,0,0}; // Int list for keeping track of how many 1s 
            int lineCount = 0; // Keep track of number of lines
            while (in.hasNextLine()) {
                lineCount++; 
                String line = in.nextLine(); 
                for (int i = 0; i < 12; i++) { // Step through countOnes
                    countOnes[i] += Integer.parseInt(String.valueOf(line.charAt(i)));
                }
            }
            String x = ""; // more frequent bit 
            String y = ""; // less frequent bit
            for (int i = 0; i < 12; i++) {
                if (countOnes[i] > lineCount / 2) { // if more than half of bits where 1
                   x += 1; 
                   y += 0;
                } else {
                   x += 0;
                   y += 1;
                }
            }
            System.out.println(x); // These are right
            System.out.print(y);
        } catch (FileNotFoundException e) {
            System.out.println("No input file.");
            System.exit(1);
        }
    }
    
    /*
     * Helper function parses binary from a String
     * Doesn't work at all ~
     */
    private static int readByte(String s) {
        int decValue = 0;
        for (int i = 0; i < s.length(); i++) {
            decValue += (10 ^ i) * Integer.parseInt(String.valueOf(s.charAt(s.length() - 1 - i)));
        }
        return decValue;
    }
}
