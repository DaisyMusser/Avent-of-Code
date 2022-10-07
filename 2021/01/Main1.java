import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class Main1 {
    public static void main(String[] args) {
        try {
            Scanner in = new Scanner(new FileInputStream("input.txt"));
            //Scanner has been made for input file
            int curDepth = 0;
            int preDepth = 0;
            int counter = 0;
            int increased = 0;
            while (in.hasNextLine()) {
                if (counter == 0) {
                    preDepth = Integer.parseInt(in.nextLine());
                } else {
                    //Read in current depth
                    curDepth = Integer.parseInt(in.nextLine());
                    //Compare to previous depth
                    if (curDepth > preDepth) {
                        increased++;
                    }
                    //Update previous depth for next pass
                    preDepth = curDepth;
                }
                counter++;
            }
            //Print out number of increased depths
            System.out.println(increased);
        } catch (Exception e) {
            System.out.println("Cannot find file");
            System.exit(1);
        }
    }
}
    
