import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class Main1 {
    public static void main(String[] args) {
        try {
            Scanner in = new Scanner(new FileInputStream("input1.txt"));
            int pos = 0;
            int dep = 0;
            while (in.hasNextLine()) {
                String line = in.nextLine();
                if (line.contains("forward")) {
                    // update pos
                    pos = pos + Character.getNumericValue(line.charAt(line.length() - 1));
                } else if (line.contains("up")) {
                    // decrease dep
                    dep = dep - Character.getNumericValue(line.charAt(line.length() - 1));
                } else if (line.contains("down")) {
                    // increase dep
                    dep = dep + Character.getNumericValue(line.charAt(line.length() - 1));
                } else {
                    System.out.print("Cannot handle this line: \n" + line);
                    System.exit(1);
                }
            }
            System.out.println(pos * dep); // Print answer!
        } catch (FileNotFoundException e) {
            System.out.print("File not found.");
            System.exit(1);
        }
    }
}
