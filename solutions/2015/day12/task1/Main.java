import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        Main main = new Main();
        int solution = main.solve();
        System.out.println(solution);
    }

    public int solve() {
        String data = readInput();
        Pattern pattern = Pattern.compile("-?\\d+");
        Matcher matcher = pattern.matcher(data);
        List<String> matches = new ArrayList<>();
        while(matcher.find()) {
            matches.add(matcher.group());
        }
        return matches.stream().map(Integer::parseInt).reduce(0, Integer::sum);
    }

    private String readInput() {
        String filename = "input";
        File file = new File(filename);
        Scanner scanner;
        String input = "";
        try {
            scanner = new Scanner(file);
            scanner.useDelimiter("\\Z");
            input = scanner.next();
        }
        catch(FileNotFoundException e) {
            // nothing
        }
        return input;
    }
}
