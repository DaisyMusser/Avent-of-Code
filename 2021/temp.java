import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;

public class RENAME {
    public static void main(String[] args) {
        try {
            Scanner in = new Scanner(new FileInputStream("input.txt"));
            while (in.hasNextLine()) {
            }
        } catch (FileNotFoundException e) {
            System.out.println("No input.txt found");
        }
    }
}
    
