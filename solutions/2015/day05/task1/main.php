<?php

function has_3_vovels($s) {
    $vovels = array('a', 'e', 'i', 'o', 'u');
    $count = 0;
    $s_array = str_split($s);
    foreach($s_array as $c) {
        if(in_array($c, $vovels)) {
            $count++;
        }
    }
    return $count >= 3;
}

function has_same_letter_twice_in_a_row($s) {
    for($i = 0; $i < strlen($s) - 1; $i++) {
        if($s[$i] == $s[$i + 1]) {
            return true;
        }
    }
    return false;
}

function has_no_bad_substrings($s) {
    $bad_words = array("ab", "cd", "pq", "xy");
    foreach($bad_words as $bw) {
        if(strpos($s, $bw) !== false) {
            return false;
        }
    }
    return true;
}

function is_nice($s) {
    return has_3_vovels($s) and has_same_letter_twice_in_a_row($s) and has_no_bad_substrings($s);
}
$handle = fopen("input", "r");
$nice_count = 0;
while(($line = fgets($handle)) !== false) {
    if(is_nice($line)) {
        $nice_count++;
    }
}    
fclose($handle);
echo $nice_count;
?>