import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Iterator;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Main main = new Main();
        int solution = main.solve();
        System.out.println(solution);
    }

    public int solve() {
        String data = readInput();
        Object json = parseInput(data);
        return sum(json);
    }

    private boolean hasRedValue(JSONObject o) {
        Iterator<String> it = o.keys();
        while(it.hasNext()) {
            Object obj = o.get(it.next());
            if(obj.getClass() == String.class && ((String)obj).equals("red")) {
                return true;
            }
        }
        return false;
    }

    private int sum(Object o) {
        if(o.getClass() == JSONArray.class) {
            JSONArray j = (JSONArray)o;
            int json_sum = 0;
            for(int i = 0; i < j.length(); i++) {
                json_sum += sum(j.get(i));
            }
            return json_sum;
        }
        else if(o.getClass() == JSONObject.class) {
            JSONObject j = (JSONObject)o;
            if(hasRedValue(j)) {
                return 0;
            }
            int json_sum = 0;
            Iterator<String> it = j.keys();
            while(it.hasNext()) {
                Object obj = j.get(it.next());
                json_sum += sum(obj);
            }
            return json_sum;
        }
        else if(o.getClass() == Integer.class) {
            return (Integer)o;
        }
        return 0;
    }

    private Object parseInput(String input) {
        try {
            return new JSONObject(input);
        }
        catch(JSONException e) {
            // wrong json format for JSONObject
        }
        try {
            return new JSONArray(input);
        }
        catch(JSONException e) {
            // wrong json format for JSONArray
        }
        return new JSONObject();
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
