import 'dart:io';
import 'dart:math';

readInput() {
    return File('input').readAsLinesSync().map((l) => l.split(" -> ")).toList();
}

var values = new Map();

findValueOf(String reg, List<List<String>> connections) {
    if(values.containsKey(reg)) {
        return values[reg];
    }
    String cn = connections.where((con) => con[1] == reg).toList()[0][0];
    
    RegExp regexOnlyNumber = new RegExp(r"^(\d+|\w+)$");
    List<RegExpMatch> onlyNumberMatches = regexOnlyNumber.allMatches(cn).toList();
    if(onlyNumberMatches.length > 0) {
        String value = onlyNumberMatches[0].group(0);
        int matchedValue = int.tryParse(value);
        if(matchedValue == null) {
            matchedValue = findValueOf(value, connections);
        }
        matchedValue = matchedValue % 65536;
        values[reg] = matchedValue;
        return matchedValue;
    }
    
    RegExp regexAnd = new RegExp(r"^(\d+|\w+) AND (\d+|\w+)$");
    List<RegExpMatch> andMatches = regexAnd.allMatches(cn).toList();
    if(andMatches.length > 0) {
        String left = andMatches[0].group(1);
        String right = andMatches[0].group(2);
        int ileft = int.tryParse(left);
        int iright = int.tryParse(right);
        if(ileft == null) {
            ileft = findValueOf(left, connections);
        }
        if(iright == null) {
            iright = findValueOf(right, connections);
        }
        int value = (ileft & iright) % 65536;
        values[reg] = value;
        return value;
    }
    
    RegExp regexOr = new RegExp(r"^(\d+|\w+) OR (\d+|\w+)$");
    List<RegExpMatch> orMatches = regexOr.allMatches(cn).toList();
    if(orMatches.length > 0) {
        String left = orMatches[0].group(1);
        String right = orMatches[0].group(2);
        int ileft = int.tryParse(left);
        int iright = int.tryParse(right);
        if(ileft == null) {
            ileft = findValueOf(left, connections);
        }
        if(iright == null) {
            iright = findValueOf(right, connections);
        }
        int value = (ileft | iright) % 65536;
        values[reg] = value;
        return value;
    }
    
    RegExp regexNot = new RegExp(r"^NOT (\d+|\w+)$");
    List<RegExpMatch> notMatches = regexNot.allMatches(cn).toList();
    if(notMatches.length > 0) {
        String match = notMatches[0].group(1);
        int imatch = int.tryParse(match);
        if(imatch == null) {
            imatch = findValueOf(match, connections);
        }
        imatch = (~imatch) % 65536;
        values[reg] = imatch;
        return imatch;
    }
    RegExp regexLshift = new RegExp(r"^(\d+|\w+) LSHIFT (\d+|\w+)$");
    List<RegExpMatch> lshiftMatches = regexLshift.allMatches(cn).toList();
    if(lshiftMatches.length > 0) {
        String left = lshiftMatches[0].group(1);
        String right = lshiftMatches[0].group(2);
        int ileft = int.tryParse(left);
        int iright = int.tryParse(right);
        if(ileft == null) {
            ileft = findValueOf(left, connections);
        }
        if(iright == null) {
            iright = findValueOf(right, connections);
        }
        int value = (ileft * pow(2, iright)) % 65536;
        values[reg] = value;
        return value;
    }
    RegExp regexRshift = new RegExp(r"^(\d+|\w+) RSHIFT (\d+|\w+)$");
    List<RegExpMatch> rshiftMatches = regexRshift.allMatches(cn).toList();
    if(rshiftMatches.length > 0) {
        String left = rshiftMatches[0].group(1);
        String right = rshiftMatches[0].group(2);
        int ileft = int.tryParse(left);
        int iright = int.tryParse(right);
        if(ileft == null) {
            ileft = findValueOf(left, connections);
        }
        if(iright == null) {
            iright = findValueOf(right, connections);
        }
        int value = (ileft ~/ pow(2, iright)) % 65536;
        values[reg] = value;
        return value;
    }
}

main() {
    List<List<String>> input = readInput();
    String output = "a";
    int firstRunAOutput = findValueOf(output, input);
    values = new Map();
    values['b'] = firstRunAOutput;
    int result = findValueOf(output, input);
    print(result);
}