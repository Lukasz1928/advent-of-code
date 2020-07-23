import System.IO

countLetter :: String -> Char -> Int
countLetter str c = length $ filter (==c) str

has_n_same_letters :: String -> Int -> Bool
has_n_same_letters str n = length (filter (== n) (map (countLetter str) ['a'..'z'])) > 0

count_ns :: [String] -> Int -> Int
count_ns lst n = length $ filter (==True) (map (\str -> has_n_same_letters str n) lst)

main = do
    handle <- openFile "input" ReadMode
    contents <- hGetContents handle
    let ids = lines contents
    let twos = count_ns ids 2
    let threes = count_ns ids 3
    let result = twos * threes
    print result
    hClose handle
