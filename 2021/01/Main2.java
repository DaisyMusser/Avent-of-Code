import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;

public class Main2 {
    public static void main(String[] args) {
        try {
            Scanner in = new Scanner(new FileInputStream("input1.txt"));
            //Scanner has been made for input file
            ArrayList<Integer> inputArray = new ArrayList<Integer>();
            //Very slopply read input into massive array
            while (in.hasNextLine()) {
                inputArray.add(Integer.parseInt(in.nextLine()));
            }
            //Make sum list
            int[] sumList = new int[inputArray.size() - 2];
            for (int i = 0; i < inputArray.size() - 2; i++) {
               int sum = inputArray.get(i) + inputArray.get(i + 1) + inputArray.get(i + 2);
               sumList[i] = sum;
            }
            int curD = 0;
            int preD = 0;
            int count = 0;
            for (int i = 0; i < inputArray.size() - 2; i++) {
                if (i == 0) { //on first pass only:
                    preD = sumList[0];
                } else {
                    curD = sumList[i];
                    if (curD > preD) {
                        count++;
                    }
                    preD = curD;
                }
            }
            System.out.println(count); //Print the answer yay :)
        } catch (Exception e) {
            System.out.println("Cannot find file");
            System.exit(1);
        }
    }
}
    
