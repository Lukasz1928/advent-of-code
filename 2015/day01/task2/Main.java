package task2;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = null;
        try {
            in = new Scanner(new FileReader("input"));
        }
        catch(FileNotFoundException e) {
            // won't happen
        }
        String input = in.nextLine();
        int floor = 0;
        int result = 0;
        for(int i = 0; i < input.length(); i++) {
            floor += (input.charAt(i) == '(' ? 1 : -1);
            if(floor == -1) {
                result = i + 1;
                break;
            }
        }
        System.out.println(result);
    }
}
