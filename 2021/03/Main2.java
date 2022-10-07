import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;

public class Main2 {
    public static void main(String[] args) {
        try {
            Scanner in = new Scanner(new FileInputStream("input.txt"));
            ArrayList<String> xOpp = new ArrayList<String>();
            ArrayList<String> yOpp = new ArrayList<String>();
            while (in.hasNextLine()) {
                String line = in.nextLine();
                xOpp.add(line);
                yOpp.add(line);
            }
            // do for most common (x)
            // problem in here somewhere...
            int pass = 0;
            while (xOpp.size() > 1) {
                String commons = findCommons(xOpp); // commons made from xOpp here
                ArrayList<String> keepers = new ArrayList<String>(); // keepers made new and null here
                for (String s: xOpp) { // do for every line of xOpp
                    if (s.charAt(pass) == commons.charAt(pass)) {
                        keepers.add(s);
                    }
                }
                xOpp = keepers;
                pass++;
            }
            String x = xOpp.get(0);
            // now do for least common (y)
            pass = 0;
            while (yOpp.size() > 1) {
                String commons = findUncommons(yOpp);
                // need to compare first char to most common char (find here bc it changes fuck)
                ArrayList<String> keepers = new ArrayList<String>();
                for (String s: yOpp) {
                    if (s.charAt(pass) == commons.charAt(pass)) {
                        keepers.add(s);
                    }
                }
                yOpp = keepers;
                pass++;
            }
            String y = yOpp.get(0);
            System.out.print(x + "\n" + y);


        } catch (FileNotFoundException e) {
            System.out.println("No input.txt found");
        }
    }

    /* So modular: takes a list of strings, returns a string with the most common number for each bit
     * fixed string length of 12 is fine.
     * Confirmed works like Main1.java
     * Helper
     */
    private static String findCommons(ArrayList<String> input) {
        String commons = "";
        final int S_LENGTH = input.get(0).length(); // string length
        final int I_LENGTH = input.size(); // input file length
        int[] countOnes = new int[S_LENGTH];
        for (int i = 0; i < S_LENGTH; i++) {
        	countOnes[i] = 0;
        }
        for (String s: input) { // do for every string from input
            for (int i = 0; i < S_LENGTH; i++) { // add each digit of the string to countOnes' bit
                countOnes[i] += Integer.parseInt(String.valueOf(s.charAt(i)));
            }
        }
        // Now we have a lovely countOnes
        float half = (float) I_LENGTH / 2;
        for (int i: countOnes) {
            if (i >= half) { // I think this is right?? if == we do a 1
                commons += 1; // Reads this as a string, java is cool
            } else {
                commons += 0;
            }
        }
        return commons;
    }

    /* So modular: takes a list of strings, returns a string with the most common number for each bit
     * fixed string length of 12 is fine.
     * Confirmed works like Main1.java
     * Helper
     */
    private static String findUncommons(ArrayList<String> input) {
        String commons = "";
        final int S_LENGTH = input.get(0).length(); // string length
        final int I_LENGTH = input.size(); // input file length
        int[] countOnes = new int[S_LENGTH];
        for (int i = 0; i < S_LENGTH; i++) {
        	countOnes[i] = 0;
        }
        for (String s: input) { // do for every string from input
            for (int i = 0; i < S_LENGTH; i++) { // add each digit of the string to countOnes' bit
                countOnes[i] += Integer.parseInt(String.valueOf(s.charAt(i)));
            }
        }
        // Now we have a lovley countOnes
        float half = (float) I_LENGTH / 2;
        for (int i: countOnes) {
            if (i >= half) { // I think this is right?? if == we do a 1
                commons += 0; // Reads this as a string, java is cool
            } else {
                commons += 1;
            }
        }
        return commons;
    }
}

