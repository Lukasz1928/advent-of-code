<?php

function count_appearances($s, $pair) {
    $p = 0;
    $count = 0;
    while(true) {
        $idx = strpos($s, $pair, $p);
        if($idx === false) {
            break;
        }
        $p = $idx + 2;
        $count++;
    }
    return $count;
}

function has_pair_of_letters_twice($s) {
    $pairs = array();
    $i = 0;
    while($i < strlen($s) - 1) {
        $pair = substr($s, $i, 2);
        if(!in_array($pair, $pairs) ) {
            array_push($pairs, $pair);
        }
        $i++;
    }
    foreach($pairs as $pair) {
        if(count_appearances($s, $pair) >= 2) {
            return true;
        }
    }
    return false;
}

function has_repeating_letter_with_gap($s) {
    for($i = 0; $i < strlen($s) - 2; $i++) {
        if($s[$i] == $s[$i + 2]) {
            return true;
        }
    }
    return false;
}

function is_nice($s) {
    return has_pair_of_letters_twice($s) and has_repeating_letter_with_gap($s);
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