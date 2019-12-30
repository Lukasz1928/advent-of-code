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
        int result = input.chars().mapToObj(c -> (char)c).mapToInt(c -> (c == '(' ? 1 : -1)).sum();
        System.out.println(result);
    }
}
